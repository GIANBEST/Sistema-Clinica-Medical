from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from template.tela import Ui_MainWindow
from modulos.cadastrar import cadastrar

class telaprincipal(QMainWindow):
    def __init__(self,*args,**argvs):
        super(telaprincipal,self).__init__(*args,**argvs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionCadastrar.triggered.connect(self.add)
        

    
    def add(self):
        add = cadastrar()
        add.exec_()
