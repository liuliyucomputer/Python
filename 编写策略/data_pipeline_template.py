"""策略3：数据管道模板 | Strategy 3: Data pipeline template
编写顺序 | Writing order:
1. 配置与日志 Configuration & logging
2. 数据读取 Data ingestion
3. 转换/验证 Transform & validate
4. 导出结果 Export outputs
适合 ETL / 数据清洗流程，便于扩展多步管道。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger("pipeline")

CONFIG = {
    "input": Path("data/input.json"),
    "output": Path("data/clean.json"),
}


def load_raw_data(path: Path) -> list[dict[str, Any]]:
    """读取原始 JSON 数据 | Read raw JSON data."""

    LOGGER.info("Loading data from %s", path)
    return json.loads(path.read_text(encoding="utf-8"))


def transform(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """简单转换：筛选字段 + 填充默认值 | Simple transform."""

    LOGGER.info("Transforming %d records", len(records))
    cleaned: list[dict[str, Any]] = []
    for item in records:
        cleaned.append(
            {
                "name": item.get("name", "unknown"),
                "score": float(item.get("score", 0)),
            }
        )
    return cleaned


def export_data(records: list[dict[str, Any]], path: Path) -> None:
    """导出成 JSON | Export data as JSON."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    LOGGER.info("Exported %d records to %s", len(records), path)


def run_pipeline(config: dict[str, Path]) -> None:
    """统筹执行整条管道 | Run the entire pipeline."""

    raw = load_raw_data(config["input"])
    cleaned = transform(raw)
    export_data(cleaned, config["output"])


if __name__ == "__main__":
    run_pipeline(CONFIG)
