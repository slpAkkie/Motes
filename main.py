#!./venv/bin/python

import sys

from application import Application
from screens.MainWindow import MainWindow


def start_application() -> None:
    app = Application(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':

    start_application()
