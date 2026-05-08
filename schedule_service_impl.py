from interfaces.data_service import IDataService
from models.schedule import Schedule


class ScheduleService(IDataService):
    """
    Handles scheduling operations (date + time + task)
    """

    def __init__(self):
        self._schedule = []

    def add(self, item):
        self._schedule.append(item)

    def assign(self, task, time, date):
        # Adds a schedule entry
        if task.strip() and time.strip() and date.strip():
            self._schedule.append(
                Schedule(task, time, date)
            )

    def delete(self, index):
        # Deletes schedule entry
        if 0 <= index < len(self._schedule):
            self._schedule.pop(index)

    def clear(self):
        # Removes all schedules
        self._schedule.clear()

    def get_all(self):
        return self._schedule
