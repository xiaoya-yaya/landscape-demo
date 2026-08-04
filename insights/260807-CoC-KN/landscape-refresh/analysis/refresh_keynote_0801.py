#!/usr/bin/env python3
"""Refresh the keynote project table to the agreed 2026-08-01 snapshot.

OpenRank uses the complete 2026-07 monthly value. GitHub repository metadata
uses the current REST API response, which the keynote intentionally labels as
the 2026-08-01 snapshot because the few-day difference is immaterial here.
"""

from __future__ import annotations

import csv
import json
import os
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import clickhouse_connect
import requests
from dotenv import load_dotenv


REPO_ROOT = Path(__file__).resolve().parents[4]
CSV_PATH = REPO_ROOT / "data" / "agentic-ai-projects.csv"
QUALITY_PATH = REPO_ROOT / "insights" / "260807-CoC-KN" / "landscape-refresh" / "data" / "csv_refresh_quality_2026-08-01.json"
SNAPSHOT_DATE = "2026-08-01"
MONTHS = [
    "2025-08", "2025-09", "2025-10", "2025-11", "2025-12", "2026-01",
    "2026-02", "2026-03", "2026-04", "2026-05", "2026-06", "2026-07",
]

WATCHLIST = [
    {
        "repo_id": "1266212515",
        "repo_name": "omnigent-ai/omnigent",
        "landscape_action": "omit",
        "selection_reason": "6 月创建后，7 月 OpenRank 升到 32.65；meta-harness 与 agent governance 值得继续跟踪。",
        "selection_caveat": "Coding harnesses 与 framework 两区已经很满，先观察外部采用和持续协作，再决定替换谁。",
        "trend_signal": "new",
        "trend_signal_reason": "2026-06-11 创建，6—7 月 OpenRank 29.98 → 32.65。",
    },
    {
        "repo_id": "1246459259",
        "repo_name": "MoonshotAI/kimi-code",
        "landscape_action": "omit",
        "selection_reason": "新出现的开源 coding agent，5—7 月 OpenRank 保持可见。",
        "selection_caveat": "Agentic coding 已有 12 个项目，先观察独立能力与持续协作，不因品牌或短期热度直接加 logo。",
        "trend_signal": "new",
        "trend_signal_reason": "2026-05-22 创建，5—7 月 OpenRank 12.26 / 27.50 / 19.27。",
    },
    {
        "repo_id": "1300902838",
        "repo_name": "xai-org/grok-build",
        "landscape_action": "omit",
        "selection_reason": "7 月中旬发布后快速进入 GitHub Trending，是本轮必须进入观察池的 coding harness。",
        "selection_caveat": "项目历史不足三周，7 月 OpenRank 尚无有效值；先不挤入已经拥挤的 Agentic coding 主图。",
        "trend_signal": "new",
        "trend_signal_reason": "2026-07-14 创建，短期 attention 很强，持续协作尚待验证。",
    },
    {
        "repo_id": "1271113810",
        "repo_name": "vercel/eve",
        "landscape_action": "omit",
        "selection_reason": "以 markdown、sandbox 和 workflow 组织 agent framework，7 月 OpenRank 升到 12.88。",
        "selection_caveat": "与 Vercel AI SDK 及现有 code-first frameworks 有谱系重叠，先保留为替换候选。",
        "trend_signal": "new",
        "trend_signal_reason": "2026-06-16 创建，6—7 月 OpenRank 5.68 → 12.88。",
    },
]


def direct_network_setup() -> None:
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        os.environ.pop(key, None)


def github_headers() -> dict[str, str]:
    token = (os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN") or "").strip()
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "communityovercode-keynote-refresh",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def github_metadata(repo_id: int, fallback: str) -> dict[str, Any]:
    for endpoint in (f"repositories/{repo_id}", f"repos/{fallback}"):
        response = requests.get(
            f"https://api.github.com/{endpoint}",
            headers=github_headers(),
            timeout=30,
        )
        if response.status_code == 200:
            item = response.json()
            return {
                "repo_id": int(item["id"]),
                "repo_name": item.get("full_name") or fallback,
                "description": item.get("description") or "",
                "stars": int(item.get("stargazers_count") or 0),
                "forks": int(item.get("forks_count") or 0),
                "open_issues": int(item.get("open_issues_count") or 0),
                "license": (item.get("license") or {}).get("spdx_id") or "NOASSERTION",
                "archived": str(bool(item.get("archived"))).lower(),
                "pushed_at": item.get("pushed_at") or "",
                "language": item.get("language") or "",
                "created_at": (item.get("created_at") or "")[:10],
                "topics": ",".join(item.get("topics") or []),
                "github_status": "ok",
            }
        if response.status_code != 404:
            time.sleep(1)
    return {"repo_id": repo_id, "repo_name": fallback, "github_status": f"http_{response.status_code}"}


def query_opendigger(repo_ids: list[int]) -> tuple[dict[int, dict[str, float]], dict[int, int], list[dict[str, Any]]]:
    client = clickhouse_connect.get_client(
        host=(os.getenv("CLICKHOUSE_HOST") or "").strip(),
        port=8123,
        username=os.getenv("CLICKHOUSE_USER"),
        password=os.getenv("CLICKHOUSE_PASSWORD"),
    )
    ids = ",".join(str(value) for value in repo_ids)
    openrank_rows = client.query(f"""
        SELECT repo_id, formatDateTime(created_at, '%Y-%m') AS month, round(sum(openrank), 2)
        FROM opensource.global_openrank
        WHERE platform = 'GitHub' AND type = 'Repo'
          AND repo_id IN ({ids})
          AND created_at >= '2025-08-01' AND created_at < '2026-08-01'
        GROUP BY repo_id, month
    """).result_rows
    openrank: dict[int, dict[str, float]] = {}
    for repo_id, month, score in openrank_rows:
        openrank.setdefault(int(repo_id), {})[str(month)] = float(score)

    participant_rows = client.query(f"""
        SELECT repo_id, count(DISTINCT actor_id)
        FROM opensource.events
        WHERE platform = 'GitHub' AND repo_id IN ({ids})
          AND type IN ('IssuesEvent','IssueCommentEvent','PullRequestEvent','PullRequestReviewEvent','PullRequestReviewCommentEvent')
          AND created_at >= '2026-07-01' AND created_at < '2026-08-01'
        GROUP BY repo_id
    """).result_rows
    participants = {int(repo_id): int(count) for repo_id, count in participant_rows}

    coverage_rows = client.query("""
        SELECT toYYYYMM(created_at), count(), uniqExact(repo_id), round(sum(openrank), 2)
        FROM opensource.global_openrank
        WHERE platform = 'GitHub' AND type = 'Repo'
          AND created_at >= '2026-05-01' AND created_at < '2026-08-01'
        GROUP BY toYYYYMM(created_at) ORDER BY toYYYYMM(created_at)
    """).result_rows
    coverage = [
        {"month": str(month), "rows": int(rows), "repos": int(repos), "total_openrank": float(total)}
        for month, rows, repos, total in coverage_rows
    ]
    return openrank, participants, coverage


def update_reason(reason: str, stars: int, july_openrank: float | None) -> str:
    if not reason.startswith("当前图中的"):
        return reason
    prefix = reason.split("；", 1)[0]
    metric = f"{stars:,} stars"
    if july_openrank is not None:
        metric += f"，2026 年 7 月 OpenRank {july_openrank:.2f}"
    return f"{prefix}；仓库仍在维护，{metric}。"


def main() -> None:
    for env_path in (
        REPO_ROOT / ".env",
        REPO_ROOT / "scripts" / ".env",
        REPO_ROOT.parent / "agentic-ai-landscape" / "scripts" / ".env",
    ):
        if env_path.exists():
            load_dotenv(env_path, override=False)
    direct_network_setup()

    with CSV_PATH.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    known_ids = {int(float(row["repo_id"])) for row in rows}
    for candidate in WATCHLIST:
        if int(candidate["repo_id"]) not in known_ids:
            rows.append(dict(candidate))
    repo_names = {int(float(row["repo_id"])): row["repo_name"] for row in rows}

    metadata: dict[int, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(github_metadata, repo_id, name): repo_id for repo_id, name in repo_names.items()}
        for index, future in enumerate(as_completed(futures), 1):
            repo_id = futures[future]
            try:
                metadata[repo_id] = future.result()
            except Exception as exc:
                metadata[repo_id] = {"repo_id": repo_id, "repo_name": repo_names[repo_id], "github_status": f"error_{type(exc).__name__}"}
            if index % 50 == 0 or index == len(futures):
                print(f"GitHub metadata: {index}/{len(futures)}")

    openrank, participants, coverage = query_opendigger(sorted(repo_names))
    output: list[dict[str, Any]] = []
    renames: list[dict[str, Any]] = []
    for source in rows:
        repo_id = int(float(source["repo_id"]))
        current = metadata[repo_id]
        github_ok = current.get("github_status") == "ok"
        current_name = current.get("repo_name") or source["repo_name"]
        if current_name.lower() != source["repo_name"].lower():
            renames.append({"repo_id": repo_id, "old_name": source["repo_name"], "new_name": current_name})
        monthly = openrank.get(repo_id, {})
        july = monthly.get("2026-07")
        row = {
            "repo_id": repo_id,
            "repo_name": current_name,
            "description": current.get("description", source.get("description", "")) if github_ok else source.get("description", ""),
            "stars": current.get("stars", source.get("stars", "")),
            "forks": current.get("forks", source.get("forks", "")),
            "open_issues": current.get("open_issues", source.get("open_issues", "")),
            "license": current.get("license", source.get("license", "NOASSERTION")),
            "archived": current.get("archived", source.get("archived", "")),
            "pushed_at": current.get("pushed_at", source.get("pushed_at", "")),
            "openrank_2607": "" if july is None else july,
            "openrank_trend_2508_2607": json.dumps([monthly.get(month) for month in MONTHS], separators=(",", ":")),
            "participants_2607": participants.get(repo_id, 0),
            "language": current.get("language", source.get("language", "")),
            "created_at": current.get("created_at", source.get("created_at", "")),
            "topics": current.get("topics", source.get("topics", "")),
            "landscape_action": source.get("landscape_action", ""),
            "landscape_layer": source.get("landscape_layer", ""),
            "landscape_section": source.get("landscape_section", ""),
            "selection_reason": update_reason(source.get("selection_reason", ""), int(current.get("stars", source.get("stars") or 0)), july),
            "selection_caveat": source.get("selection_caveat", ""),
            "github_status": current.get("github_status", "unavailable"),
            "trend_signal": source.get("trend_signal", ""),
            "trend_signal_reason": source.get("trend_signal_reason", ""),
        }
        output.append(row)

    ids = [int(row["repo_id"]) for row in output]
    names = [str(row["repo_name"]).lower() for row in output]
    selected = [row for row in output if row["landscape_action"] in {"keep", "add"}]
    selected_by_layer = Counter(row["landscape_layer"] for row in selected)
    validation = {
        "passed": len(output) == len(rows) and len(ids) == len(set(ids)) and len(names) == len(set(names)) and all(row["repo_name"] for row in output),
        "rows": len(output),
        "duplicate_ids": len(ids) - len(set(ids)),
        "duplicate_names": len(names) - len(set(names)),
        "github_status": dict(Counter(row["github_status"] for row in output)),
        "selected_projects": len(selected),
        "selected_by_layer": dict(selected_by_layer),
        "selected_with_july_openrank": sum(row["openrank_2607"] != "" for row in selected),
    }
    if not validation["passed"]:
        raise RuntimeError(json.dumps(validation, ensure_ascii=False))

    fields = list(output[0])
    temp = CSV_PATH.with_suffix(".csv.tmp")
    with temp.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)
    temp.replace(CSV_PATH)

    quality = {
        "generated_at": datetime.now(UTC).isoformat(),
        "snapshot_date": SNAPSHOT_DATE,
        "github_metric_rule": "Current GitHub REST API values are presented as the agreed 2026-08-01 keynote snapshot.",
        "openrank_month": "2026-07",
        "trend_months": MONTHS,
        "participants_month": "2026-07",
        "validation": validation,
        "renames": renames,
        "openrank_global_coverage": coverage,
        "known_limitations": [
            "OpenRank July coverage is still backfill-sensitive; use it as a directional collaboration signal, not a complete league table.",
            "Stars measure accumulated attention rather than community health.",
            "Landscape placement remains an editorial decision informed by multiple signals.",
        ],
    }
    QUALITY_PATH.write_text(json.dumps(quality, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(quality, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
