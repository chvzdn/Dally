from interfaces.data_service import IDataService
from models.schedule import Schedule

class ScheduleService(IDataService):
    """
    Handles scheduling operations (date + time + task)
    """

    def __init__(self):
        self._schedule = []

    def add(self, item):
        raise NotImplementedError

    def assign(self, task, time, date):
        # Adds a schedule entry
        if not task.strip() or not time.strip() or not date.strip():
            raise ValueError("All schedule fields are required")

        self._schedule.append(Schedule(task, time, date))
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
