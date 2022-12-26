# Form implementation generated from reading ui file 'layouts/MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.BodyContent = QtWidgets.QWidget(MainWindow)
        self.BodyContent.setObjectName("BodyContent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.BodyContent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ControlsContainer = QtWidgets.QHBoxLayout()
        self.ControlsContainer.setObjectName("ControlsContainer")
        self.Searchbox = QtWidgets.QLineEdit(self.BodyContent)
        self.Searchbox.setObjectName("Searchbox")
        self.ControlsContainer.addWidget(self.Searchbox)
        self.SearchButton = QtWidgets.QPushButton(self.BodyContent)
        self.SearchButton.setObjectName("SearchButton")
        self.ControlsContainer.addWidget(self.SearchButton)
        self.NewMovieButton = QtWidgets.QPushButton(self.BodyContent)
        self.NewMovieButton.setObjectName("NewMovieButton")
        self.ControlsContainer.addWidget(self.NewMovieButton)
        self.verticalLayout.addLayout(self.ControlsContainer)
        self.MoviesContainer = QtWidgets.QVBoxLayout()
        self.MoviesContainer.setObjectName("MoviesContainer")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.MoviesContainer.addItem(spacerItem)
        self.verticalLayout.addLayout(self.MoviesContainer)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.BodyContent)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.MenuBar.setObjectName("MenuBar")
        self.menumenubar_langs = QtWidgets.QMenu(self.MenuBar)
        self.menumenubar_langs.setObjectName("menumenubar_langs")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.ActionLangs_enUS = QtGui.QAction(MainWindow)
        self.ActionLangs_enUS.setObjectName("ActionLangs_enUS")
        self.ActionLangs_ruRU = QtGui.QAction(MainWindow)
        self.ActionLangs_ruRU.setObjectName("ActionLangs_ruRU")
        self.menumenubar_langs.addAction(self.ActionLangs_enUS)
        self.menumenubar_langs.addAction(self.ActionLangs_ruRU)
        self.MenuBar.addAction(self.menumenubar_langs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "window.title"))
        self.SearchButton.setText(_translate("MainWindow", "btn.search"))
        self.NewMovieButton.setText(_translate("MainWindow", "btn.new-movie"))
        self.menumenubar_langs.setTitle(_translate("MainWindow", "menubar.langs"))
        self.ActionLangs_enUS.setText(_translate("MainWindow", "langs.en_US"))
        self.ActionLangs_ruRU.setText(_translate("MainWindow", "langs.ru_RU"))
