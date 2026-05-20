from interfaces.data_service import IDataService
from models.note import Note

class NotesService(IDataService):
    """
    Handles note operations
    Implements IDataService (polymorphism)
    """

    def __init__(self):
        # Internal storage for notes
        self._notes = []

    def add(self, item):
        if not item or not item.strip():
            raise ValueError("Note cannot be empty")

        self._notes.append(Note(item.strip()))

    def delete(self, index):
        # Removes note if index is valid
        if 0 <= index < len(self._notes):
            self._notes.pop(index)

    def get_all(self):
        return self._notes
