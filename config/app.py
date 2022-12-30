from abc import ABC

from config.lang import LangConfig
from config.database import DbConfig


class AppConfig(ABC):
    Lang = LangConfig
    DB = DbConfig
