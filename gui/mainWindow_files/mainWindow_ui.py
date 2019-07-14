# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(326, 897)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/Jicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userDetails_grid = QtWidgets.QGridLayout()
        self.userDetails_grid.setObjectName("userDetails_grid")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.userDetails_grid.addWidget(self.listView, 10, 1, 1, 2)
        self.motherBoard_label = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_label.setObjectName("motherBoard_label")
        self.userDetails_grid.addWidget(self.motherBoard_label, 3, 1, 1, 1)
        self.lastName_text = QtWidgets.QLabel(self.centralwidget)
        self.lastName_text.setObjectName("lastName_text")
        self.userDetails_grid.addWidget(self.lastName_text, 2, 2, 1, 1)
        self.motherBoard_text = QtWidgets.QLabel(self.centralwidget)
        self.motherBoard_text.setObjectName("motherBoard_text")
        self.userDetails_grid.addWidget(self.motherBoard_text, 3, 2, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.userDetails_grid.addWidget(self.name_label, 1, 1, 1, 1)
        self.Jtag_label = QtWidgets.QLabel(self.centralwidget)
        self.Jtag_label.setObjectName("Jtag_label")
        self.userDetails_grid.addWidget(self.Jtag_label, 0, 1, 1, 1)
        self.addFriend_text = QtWidgets.QLineEdit(self.centralwidget)
        self.addFriend_text.setText("")
        self.addFriend_text.setObjectName("addFriend_text")
        self.userDetails_grid.addWidget(self.addFriend_text, 5, 2, 1, 1)
        self.searchFriend_label = QtWidgets.QLabel(self.centralwidget)
        self.searchFriend_label.setObjectName("searchFriend_label")
        self.userDetails_grid.addWidget(self.searchFriend_label, 9, 1, 1, 1)
        self.Jtag_text = QtWidgets.QLabel(self.centralwidget)
        self.Jtag_text.setObjectName("Jtag_text")
        self.userDetails_grid.addWidget(self.Jtag_text, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.userDetails_grid.addWidget(self.lineEdit, 9, 2, 1, 1)
        self.addFriend_label = QtWidgets.QLabel(self.centralwidget)
        self.addFriend_label.setObjectName("addFriend_label")
        self.userDetails_grid.addWidget(self.addFriend_label, 5, 1, 1, 1)
        self.name_text = QtWidgets.QLabel(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.userDetails_grid.addWidget(self.name_text, 1, 2, 1, 1)
        self.lastName_label = QtWidgets.QLabel(self.centralwidget)
        self.lastName_label.setObjectName("lastName_label")
        self.userDetails_grid.addWidget(self.lastName_label, 2, 1, 1, 1)
        self.addFriend_button = QtWidgets.QPushButton(self.centralwidget)
        self.addFriend_button.setObjectName("addFriend_button")
        self.userDetails_grid.addWidget(self.addFriend_button, 6, 2, 1, 1)
        self.horizontalLayout.addLayout(self.userDetails_grid)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "JBM"))
        self.motherBoard_label.setText(_translate("mainWindow", "Mother Board:"))
        self.lastName_text.setText(_translate("mainWindow", "-----"))
        self.motherBoard_text.setText(_translate("mainWindow", "-----"))
        self.name_label.setText(_translate("mainWindow", "Name:"))
        self.Jtag_label.setText(_translate("mainWindow", "Jtag:"))
        self.searchFriend_label.setText(_translate("mainWindow", "Search Friend:"))
        self.Jtag_text.setText(_translate("mainWindow", "-----"))
        self.addFriend_label.setText(_translate("mainWindow", "Add Friend:"))
        self.name_text.setText(_translate("mainWindow", "-----"))
        self.lastName_label.setText(_translate("mainWindow", "Last Name:"))
        self.addFriend_button.setText(_translate("mainWindow", "ADD"))


def ac():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

ac()