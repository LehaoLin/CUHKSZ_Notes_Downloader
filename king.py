from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from blackboard_export import start_download


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.student_id = QtWidgets.QLineEdit(self.centralwidget)
        self.student_id.setGeometry(QtCore.QRect(30, 180, 211, 31))
        self.student_id.setObjectName("student_id")
        self.student_id.setPlaceholderText("请输入你的学号")

        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(30, 250, 211, 31))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("请输入密码")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(60, 310, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.download.setFont(font)
        self.download.setObjectName("download")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(130, 20, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName("title")

        self.directory = QtWidgets.QPushButton(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(20, 110, 151, 32))
        self.directory.setObjectName("directory")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 230, 60, 16))
        self.label_4.setObjectName("label_4")

        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(20, 410, 291, 21))
        self.email.setObjectName("email")

        self.notice1 = QtWidgets.QLabel(self.centralwidget)
        self.notice1.setGeometry(QtCore.QRect(110, 280, 191, 21))
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
        self.label_2.setGeometry(QtCore.QRect(160, 70, 211, 41))
        self.label_2.setObjectName("label_2")
        self.location = QtWidgets.QLabel(self.centralwidget)
        self.location.setGeometry(QtCore.QRect(30, 140, 100, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.location.setFont(font)
        self.location.setObjectName("location")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.directory.clicked.connect(self.get_directory_name)     # 选择目录路径
        self.download.clicked.connect(self.start)                   # 开始下载

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CUHKSZ课件下载器 v2020.3.0"))
        self.download.setText(_translate("MainWindow", "下载"))
        self.title.setText(_translate("MainWindow", "CUHKSZ课件下载器"))
        # self.abstract_2.setText(_translate("MainWindow", "龙大学子的课件下载器"))
        self.directory.setText(_translate("MainWindow", "选择你的目标文件夹"))
        self.label_3.setText(_translate("MainWindow", "学号"))
        self.label_4.setText(_translate("MainWindow", "密码"))

        self.email.setText(_translate("MainWindow", "如有问题，请联系我: lehaolin@link.cuhk.edu.cn"))
        self.notice1.setText(_translate("MainWindow", "不会以任何方式储存你的密码"))
        self.label.setText(_translate("MainWindow", "v2020.3.0"))
        self.label_2.setText(_translate("MainWindow", "批量从blackboard下载课件到本地"))
        self.location.setText(_translate("MainWindow", "尚未选择文件夹"))

    def get_directory_name(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        directory_name = str(QtWidgets.QFileDialog.getExistingDirectoryUrl(self,'选择一个文件夹',QtCore.QUrl('./.')))

        directory_name = directory_name.replace("PyQt5.QtCore.QUrl('file://",'')
        directory_name = directory_name.replace("')",'')
        directory_name += '/'
        self.location.setText(_translate("MainWindow",directory_name))
        self.location.adjustSize()

        print("name", directory_name)

    def start(self, MainWindow):
        student_id = self.student_id.text()
        password = self.password.text()
        path = self.location.text()
        start_download(student_id, password, path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
