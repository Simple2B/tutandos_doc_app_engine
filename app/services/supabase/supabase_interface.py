from flask import Flask
from typing import List
from abc import ABC, abstractmethod


class SupaBaseClientInterface(ABC):
    @abstractmethod
    def init_app(self, app: Flask):
        ...

    @abstractmethod
    def get(self, table: str, eq={}, count=None) -> List:
        ...

    @abstractmethod
    def get_item(self, id):
        ...

    @abstractmethod
    def create(self, name, price) -> list:
        ...

    @abstractmethod
    def update(self, id, name=None, price=None):
        ...

    @abstractmethod
    def delete(self, id):
        ...
