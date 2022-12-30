import sqlite3

from config.App import AppConfig


class Database():
    _instance = None

    _config: AppConfig.DB

    _connection: sqlite3.Connection
    _cursor: sqlite3.Cursor

    def __init__(self, config: AppConfig.DB | None = None):
        """Initializes database connection"""
        if not Database._instance is None:
            return Database._instance

        print('Creating new Database instance')

        self._config = AppConfig.DB() if config is None else config

        self._connection = sqlite3.connect(self._config.file)
        self._cursor = self._connection.cursor()

    def query(self, query: str, parameters: list[__builtins__] = [], fetch_count: int = 0) -> list:
        """Executes non-destructive query"""
        self.execute(query, parameters, False)

        if fetch_count == 0:
            return self._cursor.fetchall()
        elif fetch_count == 1:
            return self._cursor.fetchone()
        else:
            return self._cursor.fetchmany(fetch_count)

    def execute(self, query: str, parameters: list[__builtins__] = [], commit: bool = False) -> None:
        """Execute a query and commit it if a commit parameter is True"""
        self._cursor.execute(query, parameters)

        if commit:
            self.commit()

    def executemany(self, query: str, parameters: list[tuple[__builtins__]] = [], commit: bool = True) -> None:
        """Execute a query and commit it if a commit parameter is True"""
        self._cursor.executemany(query, parameters)

        if commit:
            self.commit()

    def commit(self) -> None:
        """Commit previous changes"""
        self._connection.commit()

    def rollback(self) -> None:
        """Rollback all uncommited changes"""
        self._connection.rollback()
