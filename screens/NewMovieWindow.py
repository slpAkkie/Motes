from window import Window
from layouts.ui_NewMovieWindow import Ui_NewMovieWindow


class NewMovieWindow(Ui_NewMovieWindow, Window):
    def __init__(self, parent=None) -> None:
        """Initializes a window and its widgets"""

        super().__init__(parent)

        self.setupUi(self)
