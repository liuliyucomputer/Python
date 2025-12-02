"""策略2：包级模块结构 | Strategy 2: Package-style module layout
编写顺序 | Writing order:
1. __all__ 与版本常量 Module metadata
2. 型别与异常 Type hints & custom errors
3. 业务类与方法 Business classes & methods
4. 工具函数 Utilities
5. if __name__ == '__main__' 用于快速调试 Quick debug hook
适合需要被复用 / 导入的功能模块。
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

__all__ = ["Task", "TaskRepository", "sync_tasks"]
__version__ = "0.1.0"


class TaskSyncError(RuntimeError):
    """同步任务失败 | Raised when syncing tasks fails."""


@dataclass(slots=True)
class Task:
    """任务数据结构 | Task data structure."""

    title: str
    completed: bool = False


class TaskRepository:
    """任务仓库 | Repository managing tasks."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def add(self, task: Task) -> None:
        self._tasks.append(task)

    def list_all(self) -> list[Task]:
        return list(self._tasks)


def sync_tasks(repo: TaskRepository, incoming: Iterable[Task]) -> int:
    """把外部任务同步到仓库 | Sync tasks from external source."""

    try:
        count = 0
        for task in incoming:
            repo.add(task)
            count += 1
        return count
    except Exception as exc:  # noqa: BLE001 demo 简化
        raise TaskSyncError("同步任务失败 | Failed to sync tasks") from exc


if __name__ == "__main__":
    demo_repo = TaskRepository()
    added = sync_tasks(
        demo_repo,
        [Task("Write docs"), Task("Review code", completed=True)],
    )
    print(f"Synced {added} tasks | 已同步 {added} 条任务")
