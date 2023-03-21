from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import  Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys
from db.query import server_db

from template.cadastrar import Ui_cadastrar

class cadastrar(QDialog):
    def __init__(self,*args,**argvs):
        super(cadastrar,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar()
        self.ui.setupUi(self)
        self.ui.btnadd.clicked.connect(self.add)
        self.ui.btnc.clicked.connect(self.can)
        self.ui.btnl.clicked.connect(self.limpar)    

    
    
    
    def add(self):
        db = server_db ("manager.db")
        
        name = self.ui.inputnome.text()
        docu = self.ui.inputdoc.text()
        end = self.ui.inputend.text()
        adm = 1
        if name =="" or docu =="" or end =="":
             QMessageBox.information(QMessageBox(),"Preencha os Dados")            
        
        else:
            db.inserir_apagar_atualiza("INSERT INTO funcionarios (nome, documento,endereco,admin) VALUES ('{}' , '{}' , '{}' , '{}')",format(name,docu,end,adm))
            QMessageBox.information(QMessageBox(),"Dados Gravdos com sucesso!")  




    def can(self):
        pass





    def  limpar(self):
        self.ui.inputnome.setText("")
        self.ui.inputdoc.setText("")
        self.ui.inputend.setText("")