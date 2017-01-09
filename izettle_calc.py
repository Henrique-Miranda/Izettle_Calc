# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
import os

class MainW(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainW, self).__init__(parent)
        self.resize(350, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(self)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self)
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel(self)
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.radioButton = QtGui.QRadioButton(self)
        self.radioButton.setChecked(True)
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self)
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.label_2 = QtGui.QLabel(self)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.label_5 = QtGui.QLabel(self)
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.pushButton = QtGui.QPushButton(self)
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self)
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.credits = QtGui.QLabel(self)
        self.verticalLayout_2.addWidget(self.credits)
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.contact = QtGui.QLabel(self)
        self.verticalLayout_2.addWidget(self.contact)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.close)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.lineEdit, self.radioButton)
        self.setTabOrder(self.radioButton, self.radioButton_2)
        self.setTabOrder(self.radioButton_2, self.comboBox)
        self.setTabOrder(self.comboBox, self.lineEdit_2)
        self.setTabOrder(self.lineEdit_2, self.pushButton)
        self.setTabOrder(self.pushButton, self.pushButton_2)
        self.setWindowTitle("Calculadora Izettle")
        self.label_3.setText("Calculadora Izettle")
        self.pixmap = QtGui.QPixmap("logo.png")
        self.label_3.setPixmap(self.pixmap)
        self.label_4.setText("Informe o valor à parcelar: Ex. 50.00 para R$50,00")
        self.label.setText("Valor :")
        self.radioButton.setText("Crédito")
        self.radioButton.clicked.connect(self.comboBoxStatusOn)
        self.radioButton_2.setText("Débito")
        self.radioButton_2.clicked.connect(self.comboBoxStatusOff)
        self.label_2.setText("Número de parcelas:")
        self.comboBox.setItemText(0, "1")
        self.comboBox.setItemText(1, "2")
        self.comboBox.setItemText(2, "3")
        self.comboBox.setItemText(3, "4")
        self.comboBox.setItemText(4, "5")
        self.comboBox.setItemText(5, "6")
        self.comboBox.setItemText(6, "7")
        self.comboBox.setItemText(7, "8")
        self.comboBox.setItemText(8, "9")
        self.comboBox.setItemText(9, "10")
        self.comboBox.setItemText(10, "11")
        self.comboBox.setItemText(11, "12")
        self.label_5.setText("Valor com Taxa:")
        self.pushButton.setText("Sair")
        self.pushButton_2.setText("Calcular")
        self.pushButton_2.clicked.connect(self.calcular)
        self.credits.setText("Por: Henrique Miranda")
        self.contact.setText("Contato: lhmiranda29@gmail.com")

    #Enable combobox
    def comboBoxStatusOn(self):
        self.comboBox.setDisabled(False)
    #Unable combobox
    def comboBoxStatusOff(self):
        self.comboBox.setDisabled(True)

    def calcular(self):
        if self.lineEdit.text() != "":
            self.valor = float(self.lineEdit.text())
            #Tax Configuration
            self.tax = {'1' : 4.99, '2' : 6.98, '3' : 8.97, '4' : 10.96, '5' : 12.95, '6' : 14.94, '7' : 16.93, '8' : 18.92, '9' : 20.91, '10' : 22.9, '11' : 24.89, '12' : 26.88}
            self.taxParcel = 1.99
            self.taxDebt = 2.39
            self.cashOut = 3.00

            if self.radioButton.isChecked() == True:
                #Credit
                self.x = self.comboBox.currentText()
                self.calc()

            else:
                #Debt
                total = self.valor + self.cashOut
                total = total + ((self.valor*self.taxDebt)/100)
                self.lineEdit_2.setText('R$%.2f' %total)
        else:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setWindowTitle('Campo Valor Vazio!')
            msg.setText('Antes de Calcular informe um valor')
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.buttonClicked.connect(msg.close)
            rt = msg.exec_()
    #Function to calc, tax Credit.
    def calc(self):
        total = self.valor + self.cashOut
        total = total + (self.valor*self.tax[self.x])/100

        if self.x != '1':
            x2 = int(self.x)
            parcela = total / x2
            self.lineEdit_2.setText('R$%.2f' %total)
            self.lineEdit_2.setText('R$%.2f em %sX de R$%.2f' % (total, x2, parcela))
        else:
            self.lineEdit_2.setText('R$%.2f À Vista' %total)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainW()
    ui.show()
    app.exec_()
