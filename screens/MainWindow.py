
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSlot

from base.Window import Window
from base.Application import Application
from layouts.ui_MainWindow import Ui_MainWindow
from screens.MovieWindow import MovieWindow
from db.models.Movie import Movie
from widgets.MovieWidget import MovieWidget


class MainWindow(Ui_MainWindow, Window):

    _movie_widgets: list[MovieWidget] = []

    def __init__(self, parent=None): super().__init__(parent)

    @pyqtSlot(name='on_ActionLangs_enUS_triggered')
    def setLang_enUS(self): Application.setLanguage('en_US')

    @pyqtSlot(name='on_ActionLangs_ruRU_triggered')
    def setLang_ruRU(self): Application.setLanguage('ru_RU')

    @pyqtSlot(name='on_ButtonNewMovie_clicked')
    def newMovie(self):
        model = Movie.create({})

        if model is None:
            return

        self._createWidgetForModel(model)

        Application.addWindow(MovieWindow(model, self)).show()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        super().showEvent(a0)

        movies = Movie.all()

        for i in range(0, len(movies)):
            self._createWidgetForModel(movies[i], i)

    def _createWidgetForModel(self, model: Movie, pos: int = 0):
        movie_widget = MovieWidget(
            movie=model,
            parent=self
        )

        self.LayoutScrollAreaMovies.insertWidget(pos, movie_widget)
        self._movie_widgets.append(movie_widget)

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)

        for _ in self._movie_widgets:
            _.retranslateUi(_)
