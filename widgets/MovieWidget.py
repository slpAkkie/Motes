from base.Widget import Widget
from layouts.ui_WidgetMovie import Ui_WidgetMovie

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
