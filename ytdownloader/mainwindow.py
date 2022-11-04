# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ytdui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_YTDownloader(object):
    def setupUi(self, YTDownloader):
        YTDownloader.setObjectName("YTDownloader")
        YTDownloader.resize(997, 566)
        YTDownloader.setStyleSheet("Qframe#frame{\n"
"background-color: black;}")
        self.centralwidget = QtWidgets.QWidget(YTDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1000, 800))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.widget.setObjectName("widget")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(250, 40, 711, 121))
        self.title.setStyleSheet("font: 24pt \"Reem Kufi\";\n"
"color: white;")
        self.title.setObjectName("title")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(260, 250, 481, 231))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"background-color: rgb(207, 0, 0);}")
        self.widget_2.setObjectName("widget_2")
        self.inputlink = QtWidgets.QLineEdit(self.widget_2)
        self.inputlink.setGeometry(QtCore.QRect(40, 70, 391, 20))
        self.inputlink.setObjectName("inputlink")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QtCore.QRect(40, 120, 401, 80))
        self.widget_3.setObjectName("widget_3")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 0, 361, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 381, 71))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_9.setObjectName("label_9")
        self.enterbutton = QtWidgets.QPushButton(self.widget_2)
        self.enterbutton.setGeometry(QtCore.QRect(190, 100, 75, 23))
        self.enterbutton.setStyleSheet("font: 8pt \"Reem Kufi\";\n"
"background-color: rgb(148, 0, 0);\n"
"color: white;")
        self.enterbutton.setObjectName("enterbutton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 250, 171, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 310, 201, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 211, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 201, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 201, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 201, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Reem Kufi\";")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 539, 1001, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        YTDownloader.setCentralWidget(self.centralwidget)

        self.retranslateUi(YTDownloader)
        QtCore.QMetaObject.connectSlotsByName(YTDownloader)

    def retranslateUi(self, YTDownloader):
        _translate = QtCore.QCoreApplication.translate
        YTDownloader.setWindowTitle(_translate("YTDownloader", "MainWindow"))
        self.title.setText(_translate("YTDownloader", "Youtube Downloader by MonCcciii"))
        self.label_8.setText(_translate("YTDownloader", ""))
        self.label_9.setText(_translate("YTDownloader", ""))
        self.enterbutton.setText(_translate("YTDownloader", "Enter :)"))
        self.label_2.setText(_translate("YTDownloader", "How To Use?"))
        self.label_4.setText(_translate("YTDownloader", "2. Press Enter"))
        self.label_6.setText(_translate("YTDownloader", "into the Downloads folder of the folder"))
        self.label_7.setText(_translate("YTDownloader", "this file is in."))
        self.label_5.setText(_translate("YTDownloader", "3. Enjoy! Video should be downloaded"))
        self.label_3.setText(_translate("YTDownloader", "1. Input link into textbox."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YTDownloader = QtWidgets.QMainWindow()
    ui = Ui_YTDownloader()
    ui.setupUi(YTDownloader)
    YTDownloader.show()
    sys.exit(app.exec_())
