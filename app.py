"""Text interface for the ST-04 task-entry prototype."""

from dataman.logic import add_task
from dataman.store import InMemoryTaskStore


def run() -> None:
    store = InMemoryTaskStore()
    print("Study task entry")

    while True:
        print("\n1. Add task\n2. List tasks\n3. Exit")
        choice = input("> ").strip()

        if choice == "1":
            title = input("Task title: ")
            try:
                task = add_task(store, title)
            except ValueError as error:
                print(error)
            else:
                print(f"Added task {task.id}: {task.title}")
        elif choice == "2":
            tasks = store.list_tasks()
            if not tasks:
                print("No tasks yet.")
            else:
                for task in tasks:
                    print(f"{task.id}. {task.title}")
        elif choice == "3":
            print("Goodbye.")
            return
        else:
            print("Choose 1, 2, or 3.")


if __name__ == "__main__":
    run()