# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/NewPythonPackageDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewPythonPackageDialog(object):
    def setupUi(self, NewPythonPackageDialog):
        NewPythonPackageDialog.setObjectName("NewPythonPackageDialog")
        NewPythonPackageDialog.resize(400, 95)
        self.vboxlayout = QtWidgets.QVBoxLayout(NewPythonPackageDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.label_2 = QtWidgets.QLabel(NewPythonPackageDialog)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)
        self.packageEdit = QtWidgets.QLineEdit(NewPythonPackageDialog)
        self.packageEdit.setObjectName("packageEdit")
        self.vboxlayout.addWidget(self.packageEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewPythonPackageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPythonPackageDialog)
        self.buttonBox.accepted.connect(NewPythonPackageDialog.accept)
        self.buttonBox.rejected.connect(NewPythonPackageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPythonPackageDialog)

    def retranslateUi(self, NewPythonPackageDialog):
        _translate = QtCore.QCoreApplication.translate
        NewPythonPackageDialog.setWindowTitle(_translate("NewPythonPackageDialog", "Add new Python package"))
        self.label_2.setText(_translate("NewPythonPackageDialog", "Enter the dotted name of the new package"))
        self.packageEdit.setToolTip(_translate("NewPythonPackageDialog", "Enter the dotted package name"))

