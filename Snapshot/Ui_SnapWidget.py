# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Snapshot/SnapWidget.ui'
#
# Created: Tue Nov 18 17:53:58 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SnapWidget(object):
    def setupUi(self, SnapWidget):
        SnapWidget.setObjectName("SnapWidget")
        SnapWidget.resize(500, 400)
        SnapWidget.setMinimumSize(QtCore.QSize(250, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(SnapWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preview = SnapshotPreview(SnapWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview.sizePolicy().hasHeightForWidth())
        self.preview.setSizePolicy(sizePolicy)
        self.preview.setMinimumSize(QtCore.QSize(230, 130))
        self.preview.setAlignment(QtCore.Qt.AlignCenter)
        self.preview.setObjectName("preview")
        self.verticalLayout.addWidget(self.preview)
        self.line = QtWidgets.QFrame(SnapWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(SnapWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.modeCombo = QtWidgets.QComboBox(SnapWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeCombo.sizePolicy().hasHeightForWidth())
        self.modeCombo.setSizePolicy(sizePolicy)
        self.modeCombo.setObjectName("modeCombo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.modeCombo)
        self.label_2 = QtWidgets.QLabel(SnapWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delaySpin = QtWidgets.QSpinBox(SnapWidget)
        self.delaySpin.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delaySpin.setObjectName("delaySpin")
        self.horizontalLayout_2.addWidget(self.delaySpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.line_3 = QtWidgets.QFrame(SnapWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(SnapWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pathNameEdit = QtWidgets.QLineEdit(SnapWidget)
        self.pathNameEdit.setReadOnly(True)
        self.pathNameEdit.setObjectName("pathNameEdit")
        self.horizontalLayout_3.addWidget(self.pathNameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(SnapWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(SnapWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.copyButton = QtWidgets.QPushButton(SnapWidget)
        self.copyButton.setEnabled(False)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.copyPreviewButton = QtWidgets.QPushButton(SnapWidget)
        self.copyPreviewButton.setEnabled(False)
        self.copyPreviewButton.setObjectName("copyPreviewButton")
        self.horizontalLayout.addWidget(self.copyPreviewButton)
        spacerItem2 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.takeButton = QtWidgets.QPushButton(SnapWidget)
        self.takeButton.setObjectName("takeButton")
        self.horizontalLayout.addWidget(self.takeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SnapWidget)
        QtCore.QMetaObject.connectSlotsByName(SnapWidget)
        SnapWidget.setTabOrder(self.modeCombo, self.delaySpin)
        SnapWidget.setTabOrder(self.delaySpin, self.takeButton)
        SnapWidget.setTabOrder(self.takeButton, self.pathNameEdit)
        SnapWidget.setTabOrder(self.pathNameEdit, self.saveButton)
        SnapWidget.setTabOrder(self.saveButton, self.copyButton)
        SnapWidget.setTabOrder(self.copyButton, self.copyPreviewButton)

    def retranslateUi(self, SnapWidget):
        _translate = QtCore.QCoreApplication.translate
        SnapWidget.setWindowTitle(_translate("SnapWidget", "eric6 Snapshot"))
        self.label.setText(_translate("SnapWidget", "Snapshot Mode:"))
        self.modeCombo.setToolTip(_translate("SnapWidget", "Select the snapshot mode"))
        self.label_2.setText(_translate("SnapWidget", "Delay:"))
        self.delaySpin.setToolTip(_translate("SnapWidget", "Enter the delay before taking the snapshot"))
        self.delaySpin.setSpecialValueText(_translate("SnapWidget", " No delay"))
        self.delaySpin.setSuffix(_translate("SnapWidget", " s"))
        self.label_3.setText(_translate("SnapWidget", "Path Name:"))
        self.pathNameEdit.setToolTip(_translate("SnapWidget", "Shows the name of the directory used for saving"))
        self.saveButton.setToolTip(_translate("SnapWidget", "Press to save the snapshot"))
        self.saveButton.setText(_translate("SnapWidget", "&Save Snapshot ..."))
        self.copyButton.setToolTip(_translate("SnapWidget", "Press to copy the snapshot to the clipboard"))
        self.copyButton.setText(_translate("SnapWidget", "&Copy"))
        self.copyPreviewButton.setToolTip(_translate("SnapWidget", "Press to copy the snapshot preview to the clipboard"))
        self.copyPreviewButton.setText(_translate("SnapWidget", "Copy &Preview"))
        self.takeButton.setToolTip(_translate("SnapWidget", "Press to take a snapshot"))
        self.takeButton.setText(_translate("SnapWidget", "&Take Snapshot ..."))

from Snapshot.SnapshotPreview import SnapshotPreview
