# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastrar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastrar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 341)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 351, 31))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_2.setStyleSheet("font: 75 10pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 61, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 160, 71, 16))
        self.label_4.setStyleSheet("font: 75 10pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.btnadd = QtWidgets.QPushButton(Dialog)
        self.btnadd.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.btnadd.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.btnadd.setObjectName("btnadd")
        self.btnc = QtWidgets.QPushButton(Dialog)
        self.btnc.setGeometry(QtCore.QRect(130, 240, 75, 23))
        self.btnc.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.btnc.setObjectName("btnc")
        self.btnl = QtWidgets.QPushButton(Dialog)
        self.btnl.setGeometry(QtCore.QRect(240, 240, 75, 23))
        self.btnl.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Verdana\";")
        self.btnl.setObjectName("btnl")
        self.inputnome = QtWidgets.QLineEdit(Dialog)
        self.inputnome.setGeometry(QtCore.QRect(70, 100, 113, 20))
        self.inputnome.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.inputnome.setObjectName("inputnome")
        self.inputend = QtWidgets.QLineEdit(Dialog)
        self.inputend.setGeometry(QtCore.QRect(70, 130, 113, 20))
        self.inputend.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.inputend.setObjectName("inputend")
        self.inputdoc = QtWidgets.QLineEdit(Dialog)
        self.inputdoc.setGeometry(QtCore.QRect(70, 160, 113, 20))
        self.inputdoc.setStyleSheet("border-color: rgb(0, 85, 255);")
        self.inputdoc.setObjectName("inputdoc")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 80, 81, 111))
        self.label_5.setStyleSheet("image: url(:/add/icons/adduser - Copia.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tela de cadastro"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Cadastrar usuaro no sistema</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Nome"))
        self.label_3.setText(_translate("Dialog", "Endereço"))
        self.label_4.setText(_translate("Dialog", "Documento"))
        self.btnadd.setText(_translate("Dialog", "Cadastrar"))
        self.btnc.setText(_translate("Dialog", "Cancelar"))
        self.btnl.setText(_translate("Dialog", "Limpar"))
        self.inputnome.setPlaceholderText(_translate("Dialog", "insira seu nome"))
        self.inputend.setPlaceholderText(_translate("Dialog", "insira seu endereço"))
        self.inputdoc.setPlaceholderText(_translate("Dialog", "insira seu documento"))
import template.cadastro


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_cadastrar()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
