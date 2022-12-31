from abc import abstractmethod
from PyQt6.QtWidgets import QWidget


class Widget(QWidget):

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.setupUi(self)

    @abstractmethod
    def setupUi(self, Widget):
        pass

    @abstractmethod
    def retranslateUi(self, Widget):
        pass
