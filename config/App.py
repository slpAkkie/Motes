from abc import ABC

from config.Lang import LangConfig
from config.Database import DbConfig


class AppConfig(ABC):
    Lang = LangConfig
    DB = DbConfig
