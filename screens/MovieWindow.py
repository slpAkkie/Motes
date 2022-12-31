from base.Window import Window
from layouts.ui_MovieWindow import Ui_MovieWindow

from db.models.Movie import Movie


class MovieWindow(Ui_MovieWindow, Window):

    _model: Movie

    def __init__(self, movie: Movie, parent=None):
        self._model = movie

        super().__init__(parent)

    def retranslateUi(self, MovieWindow):
        super().retranslateUi(MovieWindow)

        self.InputTitle.setText(self._model['title'])
        self.InputRate.setValue(self._model['rate'])
