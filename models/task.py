class Task:
    """
    Represents a single task
    Demonstrates encapsulation using private attributes
    """

    def __init__(self, title):
        self._title = title
        self._completed = False

    @property
    def title(self):
        return self._title

    @property
    def completed(self):
        return self._completed

    def mark_completed(self, value):
        # Changes task completion status
        self._completed = value
