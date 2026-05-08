class IDataService:
    """
    Interface for all data services.
    Demonstrates polymorphism.
    """

    def add(self, item):
        raise NotImplementedError

    def delete(self, index):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError
