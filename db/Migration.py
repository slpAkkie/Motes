from abc import abstractmethod

from db.Database import Database


class MigrationAbstract:
    _db: Database
    _table: str

    def __init__(self, db: Database) -> None:
        self._db = db

    @abstractmethod
    def create_table(self, drop: bool = False) -> None:
        print(
            f"Migrate table: {self._table}{' (Was dropped)' if drop else ''}")
        if drop:
            self._db.execute(
                query=f"""DROP TABLE IF EXISTS {self._table}""",
                commit=True
            )
