from typing import List
from abc import ABC, abstractmethod


class SupaBaseClientInterface(ABC):
    @abstractmethod
    def init_app(self, app):
        ...

    @abstractmethod
    def get(self) -> List:
        ...

    @abstractmethod
    def get_item(self, id):
        ...

    @abstractmethod
    def post(self, name, price) -> list:
        ...

    @abstractmethod
    def update(self, id, name=None, price=None):
        ...

    @abstractmethod
    def delete(self, id):
        ...
