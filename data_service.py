class IDataService:
    def add(self, item):
        raise NotImplementedError

    def delete(self, index):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError