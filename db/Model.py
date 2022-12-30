from abc import ABC

from db.Database import Database
from functions import camel_case_split


class ModelAbstract(ABC):

    _db: Database
    _table: str | None = None

    _fillable: tuple = ()

    def __init__(self):
        self._db = Database()

    @classmethod
    def getTable(cls) -> str:
        if cls._table is not None:
            return cls._table

        class_name = '_'.join(
            camel_case_split(cls.__name__)
        ).lower()

        if class_name.endswith('y'):
            return f'{class_name[:-1]}ies'

        if class_name.endswith(('ss', 'x', 'sh', 'ch', 'o')):
            return f'{class_name[:-1]}es'

        return f'{class_name}s'

    def create(self, values: dict):
        pass
