# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqtui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton_2D = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2D.setGeometry(QtCore.QRect(50, 30, 40, 20))
        self.radioButton_2D.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2D.setObjectName("radioButton_2D")
        self.radioButton_3D = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3D.setGeometry(QtCore.QRect(100, 30, 40, 20))
        self.radioButton_3D.setObjectName("radioButton_3D")
        self.combo_figures = QtWidgets.QComboBox(self.centralwidget)
        self.combo_figures.setGeometry(QtCore.QRect(10, 80, 160, 20))
        self.combo_figures.setObjectName("combo_figures")
        self.label_tape = QtWidgets.QLabel(self.centralwidget)
        self.label_tape.setGeometry(QtCore.QRect(10, 10, 160, 20))
        self.label_tape.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tape.setObjectName("label_tape")
        self.label_figere = QtWidgets.QLabel(self.centralwidget)
        self.label_figere.setGeometry(QtCore.QRect(10, 60, 160, 20))
        self.label_figere.setAlignment(QtCore.Qt.AlignCenter)
        self.label_figere.setObjectName("label_figere")
        self.label_in = QtWidgets.QLabel(self.centralwidget)
        self.label_in.setGeometry(QtCore.QRect(10, 170, 160, 20))
        self.label_in.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_in.setObjectName("label_in")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 160, 20))
        self.pushButton.setObjectName("pushButton")
        self.combo_operations = QtWidgets.QComboBox(self.centralwidget)
        self.combo_operations.setGeometry(QtCore.QRect(10, 130, 160, 20))
        self.combo_operations.setObjectName("combo_operations")
        self.label_calculation = QtWidgets.QLabel(self.centralwidget)
        self.label_calculation.setGeometry(QtCore.QRect(10, 110, 160, 20))
        self.label_calculation.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calculation.setObjectName("label_calculation")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 190, 160, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_a = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_a.setObjectName("label_a")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_a)
        self.field_a = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.field_a.setObjectName("field_a")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.field_a)
        self.label_b = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_b.setEnabled(True)
        self.label_b.setObjectName("label_b")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_b)
        self.field_b = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.field_b.setEnabled(True)
        self.field_b.setObjectName("field_b")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.field_b)
        self.label_c = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_c.setEnabled(True)
        self.label_c.setObjectName("label_c")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_c)
        self.field_c = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.field_c.setEnabled(True)
        self.field_c.setObjectName("field_c")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.field_c)
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 340, 160, 20))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 0, 3, 400))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MatPlotWidgetWindow = MatPlotWidget(self.centralwidget)
        self.MatPlotWidgetWindow.setGeometry(QtCore.QRect(180, 0, 400, 400))
        self.MatPlotWidgetWindow.setObjectName("MatPlotWidgetWindow")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_2D.setText(_translate("MainWindow", "2D"))
        self.radioButton_3D.setText(_translate("MainWindow", "3D"))
        self.label_tape.setText(_translate("MainWindow", "Тип"))
        self.label_figere.setText(_translate("MainWindow", "Форма"))
        self.label_in.setText(_translate("MainWindow", "Дано"))
        self.pushButton.setText(_translate("MainWindow", "GO!"))
        self.label_calculation.setText(_translate("MainWindow", "Вычесление"))
        self.label_a.setText(_translate("MainWindow", "label_a, мм:"))
        self.label_b.setText(_translate("MainWindow", "label_b, мм:"))
        self.label_c.setText(_translate("MainWindow", "label_c, °:"))
from matplotwidget import MatPlotWidget