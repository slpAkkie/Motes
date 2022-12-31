from base.Window import Window
from layouts.ui_NewMovieWindow import Ui_NewMovieWindow


class MovieWindow(Ui_NewMovieWindow, Window):

    def __init__(self, parent=None): super().__init__(parent)
