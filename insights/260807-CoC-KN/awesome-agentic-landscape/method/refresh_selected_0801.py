#!/usr/bin/env python3
"""Refresh the 26 editorial Awesome projects without changing the selection."""

from __future__ import annotations

import csv
import os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import clickhouse_connect
import requests
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[4]
CSV_PATH = ROOT / "insights" / "260807-CoC-KN" / "awesome-agentic-landscape" / "interactive" / "awesome_agentic_landscape_projects.csv"


def setup() -> dict[str, str]:
    for path in (ROOT / ".env", ROOT.parent / "agentic-ai-landscape" / "scripts" / ".env"):
        if path.exists():
            load_dotenv(path, override=False)
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        os.environ.pop(key, None)
    token = (os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN") or "").strip()
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "coc-keynote-awesome"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch(name: str, headers: dict[str, str]) -> dict:
    response = requests.get(f"https://api.github.com/repos/{name}", headers=headers, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> None:
    headers = setup()
    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    with ThreadPoolExecutor(max_workers=10) as executor:
        items = list(executor.map(lambda row: fetch(row["repo_name"], headers), rows))

    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        os.environ.pop(key, None)
    ids = ",".join(str(int(row["repo_id"])) for row in rows)
    client = clickhouse_connect.get_client(
        host=os.getenv("CLICKHOUSE_HOST"), port=8123,
        username=os.getenv("CLICKHOUSE_USER"), password=os.getenv("CLICKHOUSE_PASSWORD"),
    )
    event_rows = client.query(f"""
        SELECT repo_id,
               countIf(type = 'WatchEvent'),
               uniqExactIf(actor_id, type IN ('IssuesEvent','IssueCommentEvent','PullRequestEvent','PullRequestReviewEvent','PullRequestReviewCommentEvent')),
               uniqExactIf(toYYYYMM(created_at), type IN ('IssuesEvent','IssueCommentEvent','PullRequestEvent','PullRequestReviewEvent','PullRequestReviewCommentEvent'))
        FROM opensource.events
        WHERE platform='GitHub' AND repo_id IN ({ids})
          AND created_at >= '2026-05-01' AND created_at < '2026-08-02'
        GROUP BY repo_id
    """).result_rows
    events = {int(repo_id): (int(watch), int(participants), int(months)) for repo_id, watch, participants, months in event_rows}
    rank_rows = client.query(f"""
        SELECT repo_id, toYYYYMM(created_at), round(sum(openrank), 2)
        FROM opensource.global_openrank
        WHERE platform='GitHub' AND type='Repo' AND repo_id IN ({ids})
          AND created_at >= '2026-05-01' AND created_at < '2026-08-01'
        GROUP BY repo_id, toYYYYMM(created_at)
    """).result_rows
    ranks: dict[int, dict[str, float]] = {}
    for repo_id, month, value in rank_rows:
        ranks.setdefault(int(repo_id), {})[str(month)] = float(value)

    for row, item in zip(rows, items):
        repo_id = int(item["id"])
        row["repo_id"] = str(repo_id)
        row["repo_name"] = item["full_name"]
        row["html_url"] = item["html_url"]
        row["description"] = item.get("description") or ""
        row["stars_current"] = str(item.get("stargazers_count") or 0)
        row["pushed_at"] = item.get("pushed_at") or ""
        row["language"] = item.get("language") or ""
        row["license"] = (item.get("license") or {}).get("spdx_id") or "NOASSERTION"
        watch, participants, months = events.get(repo_id, (0, 0, 0))
        row["watch_events_visible_3m"] = str(watch)
        row["participants_3m"] = str(participants)
        row["activity_months"] = str(months)
        values = ranks.get(repo_id, {})
        row["openrank_202605"] = str(values.get("202605", 0))
        row["openrank_202606"] = str(values.get("202606", 0))
        row["openrank_202607"] = str(values.get("202607", 0))
        row["openrank_3m"] = str(round(sum(values.get(month, 0) for month in ("202605", "202606", "202607")), 2))
        row["github_snapshot_date"] = "2026-08-01"
        row.pop("openrank_202604", None)

    fields = list(rows[0])
    temporary = CSV_PATH.with_suffix(".csv.tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(CSV_PATH)
    print(f"refreshed={len(rows)} snapshot=2026-08-01")


if __name__ == "__main__":
    main()
