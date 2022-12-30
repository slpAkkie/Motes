from abc import abstractmethod
from PyQt6 import QtGui, QtWidgets, QtCore


class Window(QtWidgets.QMainWindow):

    closed: QtCore.pyqtSignal = QtCore.pyqtSignal(name='closed')

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setupUi(self)

    @abstractmethod
    def setupUi(self, MainWindow):
        pass

    @abstractmethod
    def retranslateUi(self, MainWindow):
        pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        super().closeEvent(a0)

        self.closed.emit()
