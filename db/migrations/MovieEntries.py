from db.Database import Database
from db.Migration import Migration


class CreateMovieEntriesTable(Migration):
    _table: str = 'movie_entries'

    def create_table(self, drop: bool = False) -> None:
        super().create_table(drop=drop)

        self._db.execute(
            query=f"""CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                title TEXT,
                poster TEXT,
                episodes INTEGER DEFAULT NULL,
                stars REAL,
                created_at TIMESTAMP,
                updated_at TIMESTAMP
            )""",
            commit=True
        )
