from abc import ABC, abstractmethod

class BaseDb(ABC):

    def __init__(self):

        self._cursor = None

    @abstractmethod
    def select(self, sql, data, fetch):
        pass

    @abstractmethod
    def insert(self, sql, data):
        pass

    @abstractmethod
    def update(self, sql, data):
        pass

    @abstractmethod
    def delete(self, sql, data):
        pass

