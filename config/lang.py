from abc import ABC


class LangConfig(ABC):
    path: str = './resources/lang/'
    default: str = 'en_US'
    current: str = 'en_US'
