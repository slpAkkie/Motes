from db.database import Database
from db.migrations.migration import Migration


class CreateMovieTagsTable(Migration):
    _db: Database
    _table: str = 'movie_tags'

    def create_table(self, drop: bool = False) -> None:
        super().create_table(drop=drop)

        self._db.execute(
            query=f"""CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER,
                title TEXT
            )""",
            commit=True
        )
