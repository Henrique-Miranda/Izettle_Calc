# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(320, 298)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_6.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.credits = QtGui.QLabel(Form)
        self.credits.setObjectName(_fromUtf8("credits"))
        self.verticalLayout_2.addWidget(self.credits)
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.contact = QtGui.QLabel(Form)
        self.contact.setObjectName(_fromUtf8("contact"))
        self.verticalLayout_2.addWidget(self.contact)
        self.contact.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.radioButton)
        Form.setTabOrder(self.radioButton, self.radioButton_2)
        Form.setTabOrder(self.radioButton_2, self.comboBox)
        Form.setTabOrder(self.comboBox, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.pushButton)
        Form.setTabOrder(self.pushButton, self.pushButton_2)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_translate("Form", "Calculadora Izettle", None))
        self.label_3.setText(_translate("Form", "Calculadora Izettle", None))
        self.pixmap = QtGui.QPixmap("logo.png")
        self.label_3.setPixmap(self.pixmap)
        self.label_4.setText(_translate("Form", "Informe o valor à parcelar:", None))
        self.label.setText(_translate("Form", "Valor :", None))
        self.radioButton.setText(_translate("Form", "Crédito", None))
        self.radioButton.clicked.connect(self.comboBoxStatusOn)
        self.radioButton_2.setText(_translate("Form", "Débito", None))
        self.radioButton_2.clicked.connect(self.comboBoxStatusOff)
        self.label_2.setText(_translate("Form", "Parcelas:", None))
        self.comboBox.setItemText(0, _translate("Form", "1X", None))
        self.comboBox.setItemText(1, _translate("Form", "2X", None))
        self.comboBox.setItemText(2, _translate("Form", "3X", None))
        self.comboBox.setItemText(3, _translate("Form", "4X", None))
        self.comboBox.setItemText(4, _translate("Form", "5X", None))
        self.comboBox.setItemText(5, _translate("Form", "6X", None))
        self.comboBox.setItemText(6, _translate("Form", "7X", None))
        self.comboBox.setItemText(7, _translate("Form", "8X", None))
        self.comboBox.setItemText(8, _translate("Form", "9X", None))
        self.comboBox.setItemText(9, _translate("Form", "10X", None))
        self.comboBox.setItemText(10, _translate("Form", "11X", None))
        self.comboBox.setItemText(11, _translate("Form", "12X", None))
        self.label_5.setText(_translate("Form", "Valor a cobrar:", None))
        self.pushButton.setText(_translate("Form", "Sair", None))
        self.pushButton_2.setText(_translate("Form", "Calcular", None))
        self.pushButton_2.clicked.connect(self.calcular)
        self.credits.setText(_translate("Form", "By Henrique Miranda", None))
        self.contact.setText(_translate("Form", "Contact: lhmiranda29@gmail.com", None))


    #Enable combobox
    def comboBoxStatusOn(self):
        self.comboBox.setDisabled(False)
    #Unable combobox
    def comboBoxStatusOff(self):
        self.comboBox.setDisabled(True)

    def calcular(self):
        self.valor = float(self.lineEdit.text())
        type(self.valor)
        self.lista = []
        if self.radioButton.isChecked() == True:
            #Credit
            if self.comboBox.currentText() == "1X":
                self.calc1x()
            elif self.comboBox.currentText() == "2X":
                self.calc2x()
            elif self.comboBox.currentText() == "3X":
                self.calc3x()
            elif self.comboBox.currentText() == "4X":
                self.calc4x()
            elif self.comboBox.currentText() == "5X":
                self.calc5x()
            elif self.comboBox.currentText() == "6X":
                self.calc6x()
            elif self.comboBox.currentText() == "7X":
                self.calc7x()
            elif self.comboBox.currentText() == "8X":
                self.calc8x()
            elif self.comboBox.currentText() == "9X":
                self.calc9x()
            elif self.comboBox.currentText() == "10X":
                self.calc10x()
            elif self.comboBox.currentText() == "11X":
                self.calc11x()
            elif self.comboBox.currentText() == "12X":
                self.calc12x()
        else:
            #Debt
            self.lista.clear()
            self.lista.append((self.valor*2.99)/100)
            total = self.lista[0] + self.valor + 3
            self.lineEdit_2.setText('R$%.2f' %total)

    #Functions to calc, tax in percent.

    def calc1x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f À Vista' %total)

    def calc2x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc3x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc4x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc5x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc6x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc7x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc8x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93, 18.92]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc9x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93, 18.92, 20.91]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc10x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93, 18.92, 20.91, 22.9]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc11x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93, 18.92, 20.91, 22.9, 24.89]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))

    def calc12x(self):
        self.lista.clear()
        total = self.valor+3
        juros = [4.99, 6.98, 8.97, 10.96, 12.95, 14.94, 16.93, 18.92, 20.91, 22.9, 24.89, 26.88]
        for j in juros:
            self.lista.append((self.valor/len(juros)*j)/100)
        for l in self.lista:
            total = total + l
            parcela = total / len(juros)
        self.lineEdit_2.setText('R$%.2f em %s de R$%.2f' % (total, self.comboBox.currentText(), parcela))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
