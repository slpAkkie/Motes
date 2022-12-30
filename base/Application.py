
import os
import locale
import typing
import darkdetect
import resources.resources

import PyQt6.QtCore as QtCore
from config.App import AppConfig
from PyQt6.QtWidgets import QApplication
from base.Window import Window


class Application(QApplication):

    translator: QtCore.QTranslator = QtCore.QTranslator()

    windows: list[Window] = []

    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)

        self.setLanguage(locale.getdefaultlocale()[0])
        self.installTranslator(Application.translator)
        self.loadTheme()

    @staticmethod
    def addWindow(window: Window) -> Window:
        Application.windows.append(window)

        return window

    @staticmethod
    def setLanguage(lang: str | None) -> None:
        """Load provided language into translator"""
        if not lang is None:
            AppConfig.Lang.current = lang

        lang_file_path = f'{AppConfig.Lang.path}{AppConfig.Lang.current}.qm'

        if not os.path.exists(lang_file_path):
            lang_file_path = f'{AppConfig.Lang.path}{AppConfig.Lang.default}.qm'

        Application.translator.load(lang_file_path)

        for w in Application.windows:
            w.retranslateUi(w)

    def loadTheme(self) -> None:
        """Returns stylesheet as a string depends on OS theme"""

        file = QtCore.QFile(':/theme/{}/stylesheet.qss'.format(
            'dark' if darkdetect.isDark() else 'light'))
        file.open(QtCore.QFile.OpenModeFlag.ReadOnly |
                  QtCore.QFile.OpenModeFlag.Text)

        self.setStyleSheet(QtCore.QTextStream(file).readAll())
