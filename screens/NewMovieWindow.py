import PyQt6.QtWidgets as QtWidgets
from layouts.ui_NewMovieWindow import Ui_NewMovieWindow


class NewMovieWindow(QtWidgets.QMainWindow, Ui_NewMovieWindow):
    def __init__(self, parent=None) -> None:
        """Initializes a window and its widgets"""

        super().__init__(parent)

        self.setupUi(self)
