# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 721, 31))
        self.label.setStyleSheet("background-color: rgb(120, 120, 120);\n"
"border-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 321, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 50, 91, 16))
        self.label_3.setStyleSheet("font: 75 10pt \"Arial\";\n"
"color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.logado = QtWidgets.QLabel(self.centralwidget)
        self.logado.setGeometry(QtCore.QRect(600, 50, 47, 13))
        self.logado.setObjectName("logado")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 721, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivivos = QtWidgets.QMenu(self.menubar)
        self.menuArquivivos.setObjectName("menuArquivivos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionProcurar = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/principal/icons/pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProcurar.setIcon(icon)
        self.actionProcurar.setObjectName("actionProcurar")
        self.actionCadastrar = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/principal/icons/cadastrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCadastrar.setIcon(icon1)
        self.actionCadastrar.setObjectName("actionCadastrar")
        self.actionApagar = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/principal/icons/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionApagar.setIcon(icon2)
        self.actionApagar.setObjectName("actionApagar")
        self.actionAtualizar = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/principal/icons/manager.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAtualizar.setIcon(icon3)
        self.actionAtualizar.setObjectName("actionAtualizar")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/principal/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon4)
        self.actionRefresh.setObjectName("actionRefresh")
        self.menuArquivivos.addAction(self.actionProcurar)
        self.menuArquivivos.addAction(self.actionCadastrar)
        self.menuArquivivos.addAction(self.actionApagar)
        self.menuArquivivos.addAction(self.actionAtualizar)
        self.menuArquivivos.addAction(self.actionRefresh)
        self.menubar.addAction(self.menuArquivivos.menuAction())
        self.toolBar.addAction(self.actionCadastrar)
        self.toolBar.addAction(self.actionAtualizar)
        self.toolBar.addAction(self.actionProcurar)
        self.toolBar.addAction(self.actionApagar)
        self.toolBar.addAction(self.actionRefresh)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de usuários"))
        self.label_2.setText(_translate("MainWindow", "USUARIOS CADASTRADOS RECENTEMENTE"))
        self.label_3.setText(_translate("MainWindow", "Usuario logado:"))
        self.logado.setText(_translate("MainWindow", "...."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Endereço"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Profissao"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Documento"))
        self.menuArquivivos.setTitle(_translate("MainWindow", "Arquivos"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionProcurar.setText(_translate("MainWindow", "Procurar"))
        self.actionProcurar.setToolTip(_translate("MainWindow", "Procurar cadastros"))
        self.actionCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.actionCadastrar.setToolTip(_translate("MainWindow", "Cadastrar pessoas no sistema"))
        self.actionApagar.setText(_translate("MainWindow", "Apagar"))
        self.actionApagar.setToolTip(_translate("MainWindow", "Apagar pessoas cadastradas"))
        self.actionAtualizar.setText(_translate("MainWindow", "Atualizar"))
        self.actionAtualizar.setToolTip(_translate("MainWindow", "Atualizar cadastros do sistema"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        self.actionRefresh.setToolTip(_translate("MainWindow", "Atualizar tela"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "F5"))
import template.principal


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
