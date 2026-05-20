from interfaces.data_service import IDataService
from models.task import Task

class TaskService(IDataService):
    """
    Handles task operations. (create, update, delete)
    Implements IDataService
    """

    def __init__(self):
        self._tasks = []

    def add(self, item):
        # Add new task if input is not empty
        if not item or not item.strip():
            raise ValueError("Task cannot be empty")

        self._tasks.append(Task(item.strip()))

    def toggle(self, index, value):
        # Mark task as completed/uncompleted
        if 0 <= index < len(self._tasks):
            self._tasks[index].mark_completed(value)

    def delete(self, index):
        # Delete task by index
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)

    def get_all(self):
        return self._tasks
