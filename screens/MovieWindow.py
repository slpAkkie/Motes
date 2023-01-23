from PyQt6.QtCore import pyqtSlot, pyqtSignal

from base.Window import Window
from layouts.ui_MovieWindow import Ui_MovieWindow

from db.models.Movie import Movie


class MovieWindow(Ui_MovieWindow, Window):

    saved: pyqtSignal = pyqtSignal(name='saved')
    deleted: pyqtSignal = pyqtSignal(name='deleted')

    _model: Movie

    def __init__(self, movie: Movie, parent=None):
        self._model = movie

        super().__init__(parent)

    @pyqtSlot(name='on_ButtonCancel_clicked')
    def cancel(self):
        self._model.cancel()

        self.close()

    @pyqtSlot(name='on_ButtonSave_clicked')
    def save(self):
        self._model['title'] = self.InputTitle.text()
        self._model['rate'] = self.InputRate.value()

        self._model.save()
        self.saved.emit()

        self.close()

    @pyqtSlot(name='on_ButtonDelete_clicked')
    def delete(self):
        self._model.delete()
        self.deleted.emit()

        self.close()

    def retranslateUi(self, MovieWindow):
        super().retranslateUi(MovieWindow)

        self.InputTitle.setText(self._model['title'])
        self.InputRate.setValue(self._model['rate'])
