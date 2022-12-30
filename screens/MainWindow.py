from PyQt6.QtCore import pyqtSlot
import PyQt6.QtWidgets as QtWidgets
from application import Application
from layouts.ui_MainWindow import Ui_MainWindow
from screens.NewMovieWindow import NewMovieWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    childWindows: list[QtWidgets.QMainWindow] = []

    def __init__(self, parent=None) -> None:
        """Initializes a window and its widgets"""

        super().__init__(parent)

        self.setupUi(self)

    @pyqtSlot(name='on_ActionLangs_enUS_triggered')
    def setLang_enUS(self): self.setLang('en_US')

    @pyqtSlot(name='on_ActionLangs_ruRU_triggered')
    def setLang_ruRU(self): self.setLang('ru_RU')

    @pyqtSlot(name='on_NewMovieButton_clicked')
    def newMovie(self):
        newMovieWindow: NewMovieWindow = NewMovieWindow(self)
        self.childWindows.append(newMovieWindow)

        newMovieWindow.show()

    def setLang(self, lang: str):
        Application.setLanguage(lang)
        self.retranslateUi(self)

        for w in self.childWindows:
            w.retranslateUi(w)
