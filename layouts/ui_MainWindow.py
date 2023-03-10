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
        self.Body = QtWidgets.QWidget(MainWindow)
        self.Body.setObjectName("Body")
        self.LayoutBody = QtWidgets.QVBoxLayout(self.Body)
        self.LayoutBody.setObjectName("LayoutBody")
        self.LayoutControls = QtWidgets.QHBoxLayout()
        self.LayoutControls.setObjectName("LayoutControls")
        self.InputSearchbox = QtWidgets.QLineEdit(self.Body)
        self.InputSearchbox.setObjectName("InputSearchbox")
        self.LayoutControls.addWidget(self.InputSearchbox)
        self.ButtonSearch = QtWidgets.QPushButton(self.Body)
        self.ButtonSearch.setObjectName("ButtonSearch")
        self.LayoutControls.addWidget(self.ButtonSearch)
        self.ButtonNewMovie = QtWidgets.QPushButton(self.Body)
        self.ButtonNewMovie.setObjectName("ButtonNewMovie")
        self.LayoutControls.addWidget(self.ButtonNewMovie)
        self.LayoutBody.addLayout(self.LayoutControls)
        self.ScrollAreaMovies = QtWidgets.QScrollArea(self.Body)
        self.ScrollAreaMovies.setWidgetResizable(True)
        self.ScrollAreaMovies.setObjectName("ScrollAreaMovies")
        self.ScrollAreaMoviesContainer = QtWidgets.QWidget()
        self.ScrollAreaMoviesContainer.setGeometry(QtCore.QRect(0, 0, 780, 497))
        self.ScrollAreaMoviesContainer.setObjectName("ScrollAreaMoviesContainer")
        self.LayoutScrollAreaMovies = QtWidgets.QVBoxLayout(self.ScrollAreaMoviesContainer)
        self.LayoutScrollAreaMovies.setObjectName("LayoutScrollAreaMovies")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.LayoutScrollAreaMovies.addItem(spacerItem)
        self.ScrollAreaMovies.setWidget(self.ScrollAreaMoviesContainer)
        self.LayoutBody.addWidget(self.ScrollAreaMovies)
        MainWindow.setCentralWidget(self.Body)
        self.MenuBar = QtWidgets.QMenuBar(MainWindow)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.MenuBar.setObjectName("MenuBar")
        self.MenuBarLangs = QtWidgets.QMenu(self.MenuBar)
        self.MenuBarLangs.setObjectName("MenuBarLangs")
        MainWindow.setMenuBar(self.MenuBar)
        self.StatusBar = QtWidgets.QStatusBar(MainWindow)
        self.StatusBar.setObjectName("StatusBar")
        MainWindow.setStatusBar(self.StatusBar)
        self.ActionLangs_enUS = QtGui.QAction(MainWindow)
        self.ActionLangs_enUS.setObjectName("ActionLangs_enUS")
        self.ActionLangs_ruRU = QtGui.QAction(MainWindow)
        self.ActionLangs_ruRU.setObjectName("ActionLangs_ruRU")
        self.MenuBarLangs.addAction(self.ActionLangs_enUS)
        self.MenuBarLangs.addAction(self.ActionLangs_ruRU)
        self.MenuBar.addAction(self.MenuBarLangs.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "window.title"))
        self.ButtonSearch.setText(_translate("MainWindow", "btn.search"))
        self.ButtonNewMovie.setText(_translate("MainWindow", "btn.new"))
        self.MenuBarLangs.setTitle(_translate("MainWindow", "menubar.langs"))
        self.ActionLangs_enUS.setText(_translate("MainWindow", "langs.en_US"))
        self.ActionLangs_ruRU.setText(_translate("MainWindow", "langs.ru_RU"))
