# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(487, 568)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 180, 321, 16))
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 200, 401, 91))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ButtonSelectSpreadSheet = QtWidgets.QPushButton(self.frame)
        self.ButtonSelectSpreadSheet.setGeometry(QtCore.QRect(30, 30, 181, 23))
        self.ButtonSelectSpreadSheet.setObjectName("ButtonSelectSpreadSheet")
        self.ButtonSpreadsheetTimes = QtWidgets.QPushButton(self.frame)
        self.ButtonSpreadsheetTimes.setGeometry(QtCore.QRect(290, 30, 91, 23))
        self.ButtonSpreadsheetTimes.setObjectName("ButtonSpreadsheetTimes")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(40, 50, 401, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ButtonPlotRawData = QtWidgets.QPushButton(self.frame_2)
        self.ButtonPlotRawData.setGeometry(QtCore.QRect(30, 70, 101, 23))
        self.ButtonPlotRawData.setObjectName("ButtonPlotRawData")
        self.ButtonLoadData = QtWidgets.QPushButton(self.frame_2)
        self.ButtonLoadData.setGeometry(QtCore.QRect(229, 20, 101, 23))
        self.ButtonLoadData.setObjectName("ButtonLoadData")
        self.ButtonSelectRawDataFolder = QtWidgets.QPushButton(self.frame_2)
        self.ButtonSelectRawDataFolder.setGeometry(QtCore.QRect(30, 20, 111, 23))
        self.ButtonSelectRawDataFolder.setObjectName("ButtonSelectRawDataFolder")
        self.ButtonFilterRawData = QtWidgets.QPushButton(self.frame_2)
        self.ButtonFilterRawData.setGeometry(QtCore.QRect(230, 70, 131, 23))
        self.ButtonFilterRawData.setObjectName("ButtonFilterRawData")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 101, 16))
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(40, 330, 401, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.ButtonPlotEpochs = QtWidgets.QPushButton(self.frame_3)
        self.ButtonPlotEpochs.setGeometry(QtCore.QRect(20, 70, 121, 23))
        self.ButtonPlotEpochs.setObjectName("ButtonPlotEpochs")
        self.ButtonCalculateEpochs = QtWidgets.QPushButton(self.frame_3)
        self.ButtonCalculateEpochs.setGeometry(QtCore.QRect(20, 20, 131, 23))
        self.ButtonCalculateEpochs.setObjectName("ButtonCalculateEpochs")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 310, 57, 15))
        self.label_3.setObjectName("label_3")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ephys"))
        self.label.setText(_translate("Dialog", "Analyse with times from spreadsheet"))
        self.ButtonSelectSpreadSheet.setText(_translate("Dialog", "Select spreadsheet"))
        self.ButtonSpreadsheetTimes.setText(_translate("Dialog", "Analyse"))
        self.ButtonPlotRawData.setText(_translate("Dialog", "Plot Raw Data"))
        self.ButtonLoadData.setText(_translate("Dialog", "Load Raw Data"))
        self.ButtonSelectRawDataFolder.setText(_translate("Dialog", "Select Folder"))
        self.ButtonFilterRawData.setText(_translate("Dialog", "Filter Raw Data"))
        self.label_2.setText(_translate("Dialog", "Raw Data"))
        self.ButtonPlotEpochs.setText(_translate("Dialog", "Plot Epochs"))
        self.ButtonCalculateEpochs.setText(_translate("Dialog", "Calculate epochs"))
        self.label_3.setText(_translate("Dialog", "Epochs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

