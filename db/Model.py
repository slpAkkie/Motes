from abc import ABC

from db.Database import Database
from functions import camel_case_split


class ModelAbstract(ABC):

    _db: Database
    _table: str | None = None
    _columns: tuple = ()
    _primary_key = 'id'

    _fillable: tuple = ()
    _original: dict = {}

    def __init__(self, data: dict = {}):
        self._db = Database()
        self.columns()

        if len(data.keys()) > 0:
            self._original = data

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

    @staticmethod
    def __slit_cols_values(data: dict):
        return [i for i in data.keys()], [i for i in data.values()]

    @classmethod
    def create(cls, data: dict):
        if len(data.keys()) == 0:
            Database().execute(
                query=f"""INSERT INTO {cls.getTable()} DEFAULT VALUES""",
                commit=True
            )

            return cls.find(Database().lastInsertedId())

        for i in data.keys():
            if (i not in cls._fillable):
                raise Exception(
                    f'Column [{i}] not in _fillable for model [{cls.__name__}]')

        columns, values = cls.__slit_cols_values(data)

        Database().execute(
            query=f"""INSERT INTO {cls.getTable()} (
                {', '.join([i for i in columns])}
            ) VALUES (
                {', '.join(['?' for _ in values])}
            )""",
            parameters=values,
            commit=True
        )

        return cls.find(Database().lastInsertedId())

    @classmethod
    def columns(cls) -> tuple:
        if len(cls._columns) > 0:
            return cls._columns

        q_res = Database().query(f"""PRAGMA table_info({cls.getTable()})""")
        cls._columns = tuple([i[1] for i in q_res])

        return cls._columns

    @classmethod
    def __new_from_list(cls, values: list | None):
        if values is None:
            return None

        data = {}

        for j in range(0, len(values)):
            data[cls.columns()[j]] = values[j]

        return cls(data)

    @classmethod
    def all(cls, count: int | None = None, offset: int | None = None) -> list:
        q_res = Database().query(
            f"""SELECT * FROM {cls.getTable()} ORDER BY {cls._primary_key} DESC""")

        return [cls.__new_from_list(d) for d in q_res]

    @classmethod
    def find(cls, primary_key_value):
        res = Database().query(
            query=f"""SELECT * FROM {cls.getTable()} WHERE {cls._primary_key} = ?""",
            parameters=[primary_key_value],
            fetch_count=1
        )

        return cls.__new_from_list(res)

    @classmethod
    def where(cls, *wheres: list[str]):
        conditions = []
        values = []

        for condition in wheres:
            conditions.append(f'{condition[0]} {condition[1]} ?')
            values.append(condition[2])

        res = Database().query(
            query=f"""SELECT * FROM {cls.getTable()} WHERE {' AND '.join(conditions)}""",
            parameters=values
        )

        return [cls.__new_from_list(d) for d in res]

    def __getitem__(self, indices):
        if isinstance(indices, tuple):
            raise Exception(
                'Indexing of Model available only with single value')

        if indices not in self._original:
            raise Exception(
                f"The property [{indices}] doesn't exists in the [{self.__class__.__name__}] model")

        return self._original[indices]
