class Schedule:
    """
    Represents one schedule entry. (date + time + task)
    """

    def __init__(self, task, time, date):
        # Private attributes (encapsulation)
        self._task = task
        self._time = time
        self._date = date

    # Read-only accessors
    @property
    def task(self):
        return self._task

    @property
    def time(self):
        return self._time

    @property
    def date(self):
        return self._date
