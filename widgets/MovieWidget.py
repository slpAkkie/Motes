
from PyQt6.QtCore import pyqtSlot

from base.Widget import Widget
from base.Application import Application
from layouts.ui_WidgetMovie import Ui_WidgetMovie
from screens.MovieWindow import MovieWindow

from db.models.Movie import Movie


class MovieWidget(Ui_WidgetMovie, Widget):

    _model: Movie

    def __init__(self, movie: Movie, parent) -> None:
        self._model = movie

        super().__init__(parent)

    def retranslateUi(self, Widget):
        super().retranslateUi(Widget)

        self.LabelTitle.setText(self._model['title'])
        self.LabelRateValue.setText(str(self._model['rate']))

    @pyqtSlot(name='on_ButtonOpen_clicked')
    def open(self):
        window = MovieWindow(
            movie=self._model,
            parent=self.parent()
        )
        window.saved.connect(lambda: self.retranslateUi(self))

        Application.addWindow(window).show()
