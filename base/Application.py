
import os
import locale
import typing

import darkdetect
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication

import resources.resources
from base.Window import Window
from config.App import AppConfig


class Application(QApplication):

    _translator: QtCore.QTranslator = QtCore.QTranslator()

    _windows: list[Window] = []

    def __init__(self, argv: typing.List[str]) -> None:
        super().__init__(argv)

        self.setLanguage(locale.getdefaultlocale()[0])
        self.installTranslator(Application._translator)
        self.loadTheme()

    @staticmethod
    def addWindow(window: Window) -> Window:
        Application._windows.append(window)
        window.closed.connect(lambda: Application._windows.remove(window))

        return window

    @staticmethod
    def setLanguage(lang: str | None) -> None:
        """Load provided language into translator"""
        if lang is not None:
            AppConfig.Lang.current = lang

        lang_file_path = f'{AppConfig.Lang.path}{AppConfig.Lang.current}.qm'

        if not os.path.exists(lang_file_path):
            lang_file_path = f'{AppConfig.Lang.path}{AppConfig.Lang.default}.qm'

        Application._translator.load(lang_file_path)

        for w in Application._windows:
            w.retranslateUi(w)

    def loadTheme(self) -> None:
        """Returns stylesheet as a string depends on OS theme"""

        file = QtCore.QFile(':/theme/{}/stylesheet.qss'.format(
            'dark' if darkdetect.isDark() else 'light'))
        file.open(QtCore.QFile.OpenModeFlag.ReadOnly |
                  QtCore.QFile.OpenModeFlag.Text)

        self.setStyleSheet(QtCore.QTextStream(file).readAll())
