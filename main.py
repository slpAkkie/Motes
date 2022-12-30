#!./venv/bin/python

import sys

from base.Application import Application
from screens.MainWindow import MainWindow


def start_application() -> None:
    app = Application(sys.argv)

    app.addWindow(MainWindow()).show()

    sys.exit(app.exec())


if __name__ == '__main__':

    start_application()
