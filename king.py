# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'king.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.student_id = QtWidgets.QLineEdit(self.centralwidget)
        self.student_id.setGeometry(QtCore.QRect(30, 180, 211, 31))
        self.student_id.setObjectName("student_id")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 250, 211, 31))
        self.password.setObjectName("password")
        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(60, 310, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName("title")
        self.abstract_2 = QtWidgets.QLabel(self.centralwidget)
        self.abstract_2.setGeometry(QtCore.QRect(180, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.abstract_2.setFont(font)
        self.abstract_2.setObjectName("abstract_2")
        self.directory = QtWidgets.QPushButton(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(20, 130, 151, 32))
        self.directory.setObjectName("directory")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 60, 16))
        self.label_4.setObjectName("label_4")
        self.alipay = QtWidgets.QLabel(self.centralwidget)
        self.alipay.setGeometry(QtCore.QRect(480, 120, 51, 51))
        self.alipay.setText("")
        self.alipay.setPixmap(QtGui.QPixmap("imgs/alipay.png"))
        self.alipay.setScaledContents(True)
        self.alipay.setIndent(-1)
        self.alipay.setObjectName("alipay")
        self.qrcode = QtWidgets.QLabel(self.centralwidget)
        self.qrcode.setGeometry(QtCore.QRect(330, 170, 201, 271))
        self.qrcode.setText("")
        self.qrcode.setPixmap(QtGui.QPixmap("imgs/qrcode.png"))
        self.qrcode.setScaledContents(True)
        self.qrcode.setObjectName("qrcode")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(360, 100, 121, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(20, 410, 291, 21))
        self.email.setObjectName("email")
        self.notice2 = QtWidgets.QLabel(self.centralwidget)
        self.notice2.setGeometry(QtCore.QRect(110, 280, 191, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.notice2.setFont(font)
        self.notice2.setObjectName("notice2")
        self.notice1 = QtWidgets.QLabel(self.centralwidget)
        self.notice1.setGeometry(QtCore.QRect(30, 280, 191, 21))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.notice1.setFont(font)
        self.notice1.setObjectName("notice1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 211, 41))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.download.setText(_translate("MainWindow", "下载"))
        self.title.setText(_translate("MainWindow", "龙大课件王"))
        self.abstract_2.setText(_translate("MainWindow", "龙大学子的课件下载器"))
        self.directory.setText(_translate("MainWindow", "选择你的目标文件夹"))
        self.label_3.setText(_translate("MainWindow", "学号"))
        self.label_4.setText(_translate("MainWindow", "密码"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">如果您觉得有用，</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">打赏两块钱，</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">请我喝杯咖啡哦^_^</p></body></html>"))
        self.email.setText(_translate("MainWindow", "如有问题，请联系我: lehaolin@link.cuhk.edu.cn"))
        self.notice2.setText(_translate("MainWindow", "不会以任何方式储存你的密码"))
        self.notice1.setText(_translate("MainWindow", "仅输入可见"))
        self.label.setText(_translate("MainWindow", "v2020.3"))
        self.label_2.setText(_translate("MainWindow", "批量从blackboard下载课件到本地"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
