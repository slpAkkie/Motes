from db.Database import Database
from db.Migration import Migration


class CreateMoviesTable(Migration):
    _db: Database
    _table: str = 'movies'

    def create_table(self, drop: bool = False) -> None:
        super().create_table(drop=drop)

        self._db.execute(
            query=f"""CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                poster TEXT,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )""",
            commit=True
        )