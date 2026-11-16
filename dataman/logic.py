"""Interface-independent task-entry rules."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Task:
    id: int
    title: str


class TaskStore(Protocol):
    def add_task(self, title: str) -> Task: ...


def add_task(store: TaskStore, title: str) -> Task:
    normalized_title = title.strip()
    if not normalized_title:
        raise ValueError("Task title cannot be blank.")
    return store.add_task(normalized_title)