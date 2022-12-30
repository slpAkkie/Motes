from abc import ABC


class DbConfig(ABC):
    file: str = 'storage/main.db'
