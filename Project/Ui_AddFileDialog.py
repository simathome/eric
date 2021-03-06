# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Project/AddFileDialog.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddFileDialog(object):
    def setupUi(self, AddFileDialog):
        AddFileDialog.setObjectName("AddFileDialog")
        AddFileDialog.resize(391, 141)
        AddFileDialog.setSizeGripEnabled(True)
        self.vboxlayout = QtWidgets.QVBoxLayout(AddFileDialog)
        self.vboxlayout.setObjectName("vboxlayout")
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")
        self.targetDirLabel = QtWidgets.QLabel(AddFileDialog)
        self.targetDirLabel.setObjectName("targetDirLabel")
        self.gridlayout.addWidget(self.targetDirLabel, 1, 0, 1, 1)
        self.targetDirEdit = QtWidgets.QLineEdit(AddFileDialog)
        self.targetDirEdit.setObjectName("targetDirEdit")
        self.gridlayout.addWidget(self.targetDirEdit, 1, 1, 1, 1)
        self.sourceFileLabel = QtWidgets.QLabel(AddFileDialog)
        self.sourceFileLabel.setObjectName("sourceFileLabel")
        self.gridlayout.addWidget(self.sourceFileLabel, 0, 0, 1, 1)
        self.sourceFileEdit = QtWidgets.QLineEdit(AddFileDialog)
        self.sourceFileEdit.setObjectName("sourceFileEdit")
        self.gridlayout.addWidget(self.sourceFileEdit, 0, 1, 1, 1)
        self.sourceFileButton = QtWidgets.QToolButton(AddFileDialog)
        self.sourceFileButton.setObjectName("sourceFileButton")
        self.gridlayout.addWidget(self.sourceFileButton, 0, 2, 1, 1)
        self.targetDirButton = QtWidgets.QToolButton(AddFileDialog)
        self.targetDirButton.setObjectName("targetDirButton")
        self.gridlayout.addWidget(self.targetDirButton, 1, 2, 1, 1)
        self.vboxlayout.addLayout(self.gridlayout)
        self.sourcecodeCheckBox = QtWidgets.QCheckBox(AddFileDialog)
        self.sourcecodeCheckBox.setObjectName("sourcecodeCheckBox")
        self.vboxlayout.addWidget(self.sourcecodeCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddFileDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.targetDirLabel.setBuddy(self.targetDirEdit)
        self.sourceFileLabel.setBuddy(self.sourceFileEdit)

        self.retranslateUi(AddFileDialog)
        self.buttonBox.accepted.connect(AddFileDialog.accept)
        self.buttonBox.rejected.connect(AddFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddFileDialog)
        AddFileDialog.setTabOrder(self.sourceFileEdit, self.sourceFileButton)
        AddFileDialog.setTabOrder(self.sourceFileButton, self.targetDirEdit)
        AddFileDialog.setTabOrder(self.targetDirEdit, self.targetDirButton)
        AddFileDialog.setTabOrder(self.targetDirButton, self.sourcecodeCheckBox)

    def retranslateUi(self, AddFileDialog):
        _translate = QtCore.QCoreApplication.translate
        AddFileDialog.setWindowTitle(_translate("AddFileDialog", "Add Files"))
        AddFileDialog.setWhatsThis(_translate("AddFileDialog", "<b>Add Files Dialog</b>\n"
"<p>This dialog is used to add files to the current project.</p>"))
        self.targetDirLabel.setText(_translate("AddFileDialog", "&Target Directory:"))
        self.targetDirEdit.setToolTip(_translate("AddFileDialog", "Enter the target directory for the file"))
        self.targetDirEdit.setWhatsThis(_translate("AddFileDialog", "<b>Target Directory</b>\n"
"<p>Enter the target directory. You may select it\n"
" with a dialog by pressing the button to the right.</p>"))
        self.sourceFileLabel.setText(_translate("AddFileDialog", "&Source Files:"))
        self.sourceFileEdit.setToolTip(_translate("AddFileDialog", "Enter the name of files to add separated by the path separator"))
        self.sourceFileEdit.setWhatsThis(_translate("AddFileDialog", "<b>Source Files</b>\n"
"<p>Enter the name of files to add to the current project separated\n"
"by the path separator. You may select them with a dialog by pressing \n"
"the button to the right.</p>"))
        self.sourceFileButton.setWhatsThis(_translate("AddFileDialog", "<b>Source Files</b>\n"
"<p>Select the source files via a files selection dialog.</p>"))
        self.targetDirButton.setWhatsThis(_translate("AddFileDialog", "<b>Target Directory</b>\n"
"<p>Select the target directory via a directory selection dialog.</p>"))
        self.sourcecodeCheckBox.setToolTip(_translate("AddFileDialog", "Select, if the files should be added as sourcecode (overriding automatic detection)"))
        self.sourcecodeCheckBox.setText(_translate("AddFileDialog", "Is source&code files"))
        self.sourcecodeCheckBox.setShortcut(_translate("AddFileDialog", "Alt+C"))

