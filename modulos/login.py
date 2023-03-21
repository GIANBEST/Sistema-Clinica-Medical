from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from  modulos.principal import telaprincipal
from template.login import Ui_login





class login(QDialog):
    def __init__(self,*args,**argvs):
        super(login,self).__init__(*args,**argvs)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        #self.ui.pushButton_2.clicked.connect(self.login)


    
    def login(self):
        admin ="123"
        senha ="123"
    
        user = self.ui.lineEdit.text()
        passwd =self.ui.lineEdit_2.text()

        if admin == user and passwd ==senha:
            QMessageBox.information(QMessageBox(),"login realizado!", "Seja Bem vindo Rafael")
            self.window = telaprincipal()
            self.window.show()
        else:
            QMessageBox.warning(QMessageBox(),"login errado!", "Login errado insira de novo")
       


