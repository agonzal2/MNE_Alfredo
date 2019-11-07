# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainGUIwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.ButtonSelectRawDataFolder = QtWidgets.QPushButton(Dialog)
        self.ButtonSelectRawDataFolder.setGeometry(QtCore.QRect(30, 60, 131, 23))
        self.ButtonSelectRawDataFolder.setObjectName("ButtonSelectRawDataFolder")
        self.ButtonLoadData = QtWidgets.QPushButton(Dialog)
        self.ButtonLoadData.setGeometry(QtCore.QRect(30, 90, 131, 31))
        self.ButtonLoadData.setObjectName("ButtonLoadData")
        self.ButtonPlotRawData = QtWidgets.QPushButton(Dialog)
        self.ButtonPlotRawData.setGeometry(QtCore.QRect(30, 130, 131, 31))
        self.ButtonPlotRawData.setObjectName("ButtonPlotRawData")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ButtonSelectRawDataFolder.setText(_translate("Dialog", "Select Raw Data Folder"))
        self.ButtonLoadData.setText(_translate("Dialog", "LoadData"))
        self.ButtonPlotRawData.setText(_translate("Dialog", "Plot Data"))
