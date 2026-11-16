import unittest

from dataman.logic import add_task
from dataman.store import InMemoryTaskStore


class AddTaskTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = InMemoryTaskStore()

    def test_add_task_trims_title_and_retains_it(self) -> None:
        task = add_task(self.store, "  Practice fractions  ")

        self.assertEqual(task.title, "Practice fractions")
        self.assertEqual(self.store.list_tasks(), [task])

    def test_blank_title_is_rejected_without_changing_state(self) -> None:
        with self.assertRaisesRegex(ValueError, "cannot be blank"):
            add_task(self.store, "   ")

        self.assertEqual(self.store.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()