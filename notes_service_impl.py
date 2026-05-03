from interfaces.data_service import IDataService

class NotesService(IDataService):

    def __init__(self):
        self._notes = []

    def add(self, item):
        self._notes.append(item)

    def delete(self, index):
        if 0 <= index < len(self._notes):
            self._notes.pop(index)

    def get_all(self):
        return self._notes