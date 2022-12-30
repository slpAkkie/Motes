from abc import abstractmethod
from PyQt6.QtWidgets import QMainWindow


class Window(QMainWindow):

    @abstractmethod
    def setupUi(self, MainWindow):
        pass

    @abstractmethod
    def retranslateUi(self, MainWindow):
        pass
