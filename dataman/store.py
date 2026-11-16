"""Replaceable in-memory store for one prototype run."""

from dataman.logic import Task


class InMemoryTaskStore:
    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        task = Task(id=self._next_id, title=title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)