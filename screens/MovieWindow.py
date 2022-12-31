from base.Window import Window
from layouts.ui_MovieWindow import Ui_MovieWindow


class MovieWindow(Ui_MovieWindow, Window):

    def __init__(self, parent=None): super().__init__(parent)
