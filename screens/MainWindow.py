from window import Window
from PyQt6.QtCore import pyqtSlot
from application import Application
from layouts.ui_MainWindow import Ui_MainWindow
from screens.NewMovieWindow import NewMovieWindow


class MainWindow(Ui_MainWindow, Window):

    def __init__(self, parent=None) -> None:
        """Initializes a window and its widgets"""

        super().__init__(parent)

        self.setupUi(self)

    @pyqtSlot(name='on_ActionLangs_enUS_triggered')
    def setLang_enUS(self): self.setLang('en_US')

    @pyqtSlot(name='on_ActionLangs_ruRU_triggered')
    def setLang_ruRU(self): self.setLang('ru_RU')

    @pyqtSlot(name='on_ButtonNewMovie_clicked')
    def newMovie(self): Application.addWindow(NewMovieWindow(self)).show()

    def setLang(self, lang: str): Application.setLanguage(lang)
