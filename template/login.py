# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 314)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 311))
        self.label.setStyleSheet("background-color: rgb(213, 213, 213);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 71, 31))
        self.label_2.setStyleSheet("image: url(:/img/icons/usericon.png);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 47, 31))
        self.label_3.setStyleSheet("image: url(:/img/icons/password-icon-1.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 200, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Arial\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 270, 171, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(160, 110, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 371, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tela de Login"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Entrar"))
        self.pushButton_2.setText(_translate("Dialog", "Sair"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#00004c;\">Esqueceu sua senha?</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Digite seu login:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Digite sua senha:"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">SISTEMA DE CADASTRO DE FUNCIONÁRIOS</span></p></body></html>"))
import template.img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
