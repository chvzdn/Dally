from interfaces.data_service import IDataService

class ScheduleService(IDataService):

    def __init__(self):
        self._schedule = []

    def add(self, item):
        self._schedule.append(item)

    def assign(self, task, time, date):
        self._schedule.append({
            "task": task,
            "time": time,
            "date": date
        })

    def delete(self, index):
        if 0 <= index < len(self._schedule):
            self._schedule.pop(index)

    def clear(self):
        self._schedule.clear()

    def get_all(self):
        return self._schedule