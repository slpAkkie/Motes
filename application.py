
import os
import locale
import typing
import darkdetect
import resources.resources

import PyQt6.QtCore as QtCore
from config.app import AppConfig
from PyQt6.QtWidgets import QApplication


class Application(QApplication):
    translator: QtCore.QTranslator = QtCore.QTranslator()

    def __init__(self, argv: typing.List[str]) -> None:
        self.setLanguage(locale.getdefaultlocale()[0])

        super().__init__(argv)

        self.loadTheme()

        self.installTranslator(Application.translator)

    @staticmethod
    def setLanguage(lang: str | None) -> None:
        """Load provided language into translator"""
        lang_file_path = f'{AppConfig.lang_path}{lang}.qm'

        if not os.path.exists(lang_file_path):
            lang_file_path = f'{AppConfig.lang_path}{AppConfig.lang_default}.qm'

        Application.translator.load(lang_file_path)

    def loadTheme(self) -> None:
        """Returns stylesheet as a string depends on OS theme"""

        file = QtCore.QFile(':/theme/{}/stylesheet.qss'.format(
            'dark' if darkdetect.isDark() else 'light'))
        file.open(QtCore.QFile.OpenModeFlag.ReadOnly |
                  QtCore.QFile.OpenModeFlag.Text)

        self.setStyleSheet(QtCore.QTextStream(file).readAll())
