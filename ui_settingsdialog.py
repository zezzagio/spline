# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settingsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(494, 101)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splineToleranceLabel = QtWidgets.QLabel(SettingsDialog)
        self.splineToleranceLabel.setObjectName("splineToleranceLabel")
        self.horizontalLayout.addWidget(self.splineToleranceLabel)
        self.splineToleranceSpinBox = QtWidgets.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineToleranceSpinBox.sizePolicy().hasHeightForWidth())
        self.splineToleranceSpinBox.setSizePolicy(sizePolicy)
        self.splineToleranceSpinBox.setDecimals(6)
        self.splineToleranceSpinBox.setMinimum(1e-06)
        self.splineToleranceSpinBox.setMaximum(10000.0)
        self.splineToleranceSpinBox.setProperty("value", 1.0)
        self.splineToleranceSpinBox.setObjectName("splineToleranceSpinBox")
        self.horizontalLayout.addWidget(self.splineToleranceSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splineTightnessLabel = QtWidgets.QLabel(SettingsDialog)
        self.splineTightnessLabel.setObjectName("splineTightnessLabel")
        self.horizontalLayout_5.addWidget(self.splineTightnessLabel)
        self.splineTightnessSpinBox = QtWidgets.QDoubleSpinBox(SettingsDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splineTightnessSpinBox.sizePolicy().hasHeightForWidth())
        self.splineTightnessSpinBox.setSizePolicy(sizePolicy)
        self.splineTightnessSpinBox.setMinimum(0.01)
        self.splineTightnessSpinBox.setMaximum(10.0)
        self.splineTightnessSpinBox.setSingleStep(0.1)
        self.splineTightnessSpinBox.setProperty("value", 0.1)
        self.splineTightnessSpinBox.setObjectName("splineTightnessSpinBox")
        self.horizontalLayout_5.addWidget(self.splineTightnessSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Digitize Spline Settings"))
        self.splineToleranceLabel.setText(_translate("SettingsDialog", "Tolerance"))
        self.splineToleranceSpinBox.setToolTip(_translate("SettingsDialog", "Polyline interpolation tolerance in map units."))
        self.splineTightnessLabel.setText(_translate("SettingsDialog", "Tightness"))

