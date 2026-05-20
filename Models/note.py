class Note:
    """
    Represents a single note
    """

    def __init__(self, content):
        # Private attribute (encapsulation)
        self._content = content

    @property
    def content(self):
        # Read-only access to note content
        return self._content
