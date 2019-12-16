# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/ChrisCho/Documents/GitHub/auxData/GUI/QTDesignerUIConverter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMessageBox, QShortcut

# sys.path.append()
# Deleted path to Qt_DragDrop_UI
from Qt_DragDrop_UI import FileEdit




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(545, 155)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.button_Browse.setGeometry(QtCore.QRect(425, 20, 100, 25))
        self.button_Browse.setObjectName("button_Browse")
        self.button_Convert = QtWidgets.QPushButton(self.centralwidget)
        self.button_Convert.setGeometry(QtCore.QRect(20, 60, 505, 75))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.button_Convert.setFont(font)
        self.button_Convert.setIconSize(QtCore.QSize(16, 16))
        self.button_Convert.setObjectName("button_Convert")
        self.line_File = FileEdit(self.centralwidget)
        self.line_File.setGeometry(QtCore.QRect(20, 20, 400, 25))
        self.line_File.setCursorPosition(0)
        self.line_File.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.line_File.setObjectName("line_File")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # User-Assigned Functionality
        self.button_Browse.clicked.connect(self.setFile)
        self.button_Convert.clicked.connect(self.convertFile)

        # Window Icon
        # sys.path.append()
        # Deleted path to Icon
        # MainWindow.setWindowIcon(QtGui.QIcon())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Browse.setText(_translate("MainWindow", "Browse"))
        self.button_Convert.setText(_translate("MainWindow", "Convert"))
        self.line_File.setPlaceholderText(_translate("MainWindow", "Qt Designer UI File (no spaces allowed)"))

    def setFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select UI File", "", "QT Designer UI Files (*.ui)")
        if fileName:
            self.line_File.setText(fileName)
    
    def convertFile(self):
        File = (self.line_File.text())
        if File:
            Directory = str(os.path.dirname(File)) + "/"
            UI_File = Directory + str(os.path.basename(File))
            PY_File = str(os.path.splitext(File)[0]) + ".py"
            os.chdir(r"C:\\Users\\ChrisCho\\AppData\\Local\\Programs\\Python\\Python37\\Scripts")
            subprocess.call("pyuic5 -x %s -o %s" % (UI_File, PY_File))
            dialog = QMessageBox()
            dialog.setWindowTitle("Success")
            dialog.setText("File Converted!")
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()
        else:
            dialog = QMessageBox()
            dialog.setWindowTitle("Failure")
            dialog.setText("An error occurred.  Connversion failed.")
            dialog.setIcon(QMessageBox.Warning)
            dialog.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
