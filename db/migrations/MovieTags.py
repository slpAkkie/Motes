from db.Migration import MigrationAbstract


class CreateMovieTagsTable(MigrationAbstract):
    _table: str = 'movie_tags'

    def create_table(self, drop: bool = False) -> None:
        super().create_table(drop=drop)

        self._db.execute(
            query=f"""CREATE TABLE IF NOT EXISTS {self._table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                movie_id INTEGER NOT NULL,
                title TEXT NOT NULL
            )""",
            commit=True
        )
