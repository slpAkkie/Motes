from base.Window import Window
from PyQt6.QtCore import pyqtSlot
from base.Application import Application
from layouts.ui_MainWindow import Ui_MainWindow
from screens.NewMovieWindow import NewMovieWindow


class MainWindow(Ui_MainWindow, Window):

    def __init__(self, parent=None): super().__init__(parent)

    @pyqtSlot(name='on_ActionLangs_enUS_triggered')
    def setLang_enUS(self): Application.setLanguage('en_US')

    @pyqtSlot(name='on_ActionLangs_ruRU_triggered')
    def setLang_ruRU(self): Application.setLanguage('ru_RU')

    @pyqtSlot(name='on_ButtonNewMovie_clicked')
    def newMovie(self): Application.addWindow(NewMovieWindow(self)).show()
