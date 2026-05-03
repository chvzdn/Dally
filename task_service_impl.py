from interfaces.data_service import IDataService

class TaskService(IDataService):

    def __init__(self):
        self._tasks = []

    def add(self, item):
        self._tasks.append({
            "task": item,
            "completed": False
        })

    def toggle(self, index, value):
        self._tasks[index]["completed"] = value

    def delete(self, index):
        if 0 <= index < len(self._tasks):
            self._tasks.pop(index)

    def get_all(self):
        return self._tasks