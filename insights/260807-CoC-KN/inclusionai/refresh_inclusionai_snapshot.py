#!/usr/bin/env python3
"""Refresh the three-platform InclusionAI keynote snapshot."""

from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path

import requests
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[3]
OUT_DIR = ROOT / "public" / "keynote" / "inclusionai"
SNAPSHOT = "2026-08-01"
GITHUB_ORGS = ["inclusionAI", "AQ-MedAI", "Robbyant"]
HF_AUTHORS = ["inclusionAI", "AQ-MedAI", "robbyant"]
MS_OWNERS = ["inclusionAI", "AQ-MedAI", "robbyant"]


def setup() -> dict[str, str]:
    for path in (ROOT / ".env", ROOT.parent / "agentic-ai-landscape" / "scripts" / ".env"):
        if path.exists():
            load_dotenv(path, override=False)
    token = (os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN") or "").strip()
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "coc-keynote-inclusionai"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def github(headers: dict[str, str]) -> list[dict[str, int | str]]:
    output = []
    for org in GITHUB_ORGS:
        repos = []
        page = 1
        while True:
            response = requests.get(
                f"https://api.github.com/orgs/{org}/repos",
                params={"per_page": 100, "page": page, "type": "public"},
                headers=headers,
                timeout=30,
            )
            response.raise_for_status()
            chunk = response.json()
            repos.extend(chunk)
            if len(chunk) < 100:
                break
            page += 1
        output.append({
            "publisher": org,
            "repositories": len(repos),
            "stars": sum(int(repo.get("stargazers_count") or 0) for repo in repos),
            "forks": sum(int(repo.get("forks_count") or 0) for repo in repos),
            "fork_repositories": sum(bool(repo.get("fork")) for repo in repos),
        })
    return output


def huggingface() -> list[dict[str, int | str]]:
    output = []
    for author in HF_AUTHORS:
        response = requests.get(
            "https://huggingface.co/api/models",
            params={"author": author, "limit": 1000, "full": "true"},
            headers={"User-Agent": "coc-keynote-inclusionai"},
            timeout=45,
        )
        response.raise_for_status()
        models = response.json()
        output.append({
            "publisher": author,
            "models": len(models),
            "downloads": sum(int(model.get("downloads") or 0) for model in models),
            "likes": sum(int(model.get("likes") or 0) for model in models),
        })
    return output


def modelscope() -> list[dict[str, int | str]]:
    output = []
    for owner in MS_OWNERS:
        models: dict[str, dict] = {}
        page = 1
        while True:
            response = requests.get(
                "https://modelscope.cn/openapi/v1/models",
                params={"owner": owner, "page_size": 50, "page_number": page},
                headers={"User-Agent": "coc-keynote-inclusionai"},
                timeout=45,
            )
            response.raise_for_status()
            payload = response.json()
            data = payload.get("Data") or payload.get("data") or {}
            rows = data.get("Models") or data.get("models") or []
            for model in rows:
                key = str(model.get("Id") or model.get("id") or model.get("Path") or model.get("path"))
                models[key] = model
            if len(rows) < 50:
                break
            page += 1
        values = list(models.values())
        def number(item: dict, *keys: str) -> int:
            for key in keys:
                if item.get(key) is not None:
                    return int(item[key] or 0)
            return 0
        output.append({
            "publisher": owner,
            "models": len(values),
            "downloads": sum(number(model, "Downloads", "downloads", "DownloadCount", "download_count") for model in values),
            "likes": sum(number(model, "Likes", "likes", "LikeCount", "like_count") for model in values),
        })
    return output


def totals(rows: list[dict], fields: list[str]) -> dict[str, int]:
    return {field: sum(int(row[field]) for row in rows) for field in fields}


def main() -> None:
    headers = setup()
    gh = github(headers)
    hf = huggingface()
    ms = modelscope()
    snapshot = {
        "generated_at": datetime.now(UTC).isoformat(),
        "snapshot_date": SNAPSHOT,
        "github": {"publishers": gh, "total": totals(gh, ["repositories", "stars", "forks", "fork_repositories"])},
        "huggingface": {"publishers": hf, "total": totals(hf, ["models", "downloads", "likes"]), "downloads_window": "rolling 30 days"},
        "modelscope": {"publishers": ms, "total": totals(ms, ["models", "downloads", "likes"]), "downloads_window": "not declared by the API"},
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / f"snapshot-{SNAPSHOT}.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def table(rows: list[dict], fields: list[tuple[str, str]]) -> str:
        header = "| 发布者 | " + " | ".join(label for _, label in fields) + " |\n"
        rule = "|---|" + "---:|" * len(fields) + "\n"
        body = "".join("| " + str(row["publisher"]) + " | " + " | ".join(f"{int(row[key]):,}" for key, _ in fields) + " |\n" for row in rows)
        total = totals(rows, [key for key, _ in fields])
        body += "| **合计** | " + " | ".join(f"**{total[key]:,}**" for key, _ in fields) + " |\n"
        return header + rule + body

    markdown = f"""# InclusionAI 开放生态快照

数据截至：{SNAPSHOT}。GitHub 使用当前 REST API 返回值，并按演讲约定归入 8 月 1 日快照。

三个平台存在重复发布，模型数与互动数据只在各平台内解释，不跨平台相加。

## GitHub

{table(gh, [('repositories','公开仓库'),('stars','Stars'),('forks','Forks'),('fork_repositories','fork 仓库')])}

范围：`inclusionAI`、`AQ-MedAI`、`Robbyant` 三个组织的公开仓库。

## Hugging Face

{table(hf, [('models','公开模型'),('downloads','近 30 天 Downloads'),('likes','Likes')])}

范围：`inclusionAI`、`AQ-MedAI`、`robbyant` 三个发布者。Downloads 是滚动近 30 天窗口。

## ModelScope

{table(ms, [('models','公开模型'),('downloads','Downloads'),('likes','Likes')])}

范围：`inclusionAI`、`AQ-MedAI`、`robbyant` 三个发布者。API 未声明 Downloads 的统计窗口。
"""
    (OUT_DIR / f"snapshot-{SNAPSHOT}.md").write_text(markdown, encoding="utf-8")
    print(json.dumps(snapshot, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
