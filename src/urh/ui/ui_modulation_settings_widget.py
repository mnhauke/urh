# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/joe/GIT/urh/data/ui/modulation_settings_widget.ui',
# licensing of '/home/joe/GIT/urh/data/ui/modulation_settings_widget.ui' applies.
#
# Created: Thu Jun 20 11:48:48 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ModulationSettings(object):
    def setupUi(self, ModulationSettings):
        ModulationSettings.setObjectName("ModulationSettings")
        ModulationSettings.resize(821, 635)
        self.verticalLayout = QtWidgets.QVBoxLayout(ModulationSettings)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxSniffSettings = QtWidgets.QGroupBox(ModulationSettings)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.groupBoxSniffSettings.setFont(font)
        self.groupBoxSniffSettings.setStyleSheet("QGroupBox\n"
"{\n"
"border: none;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QGroupBox::indicator:unchecked {\n"
" image: url(:/icons/icons/collapse.svg)\n"
"}\n"
"QGroupBox::indicator:checked {\n"
" image: url(:/icons/icons/uncollapse.svg)\n"
"}")
        self.groupBoxSniffSettings.setFlat(True)
        self.groupBoxSniffSettings.setCheckable(True)
        self.groupBoxSniffSettings.setObjectName("groupBoxSniffSettings")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxSniffSettings)
        self.gridLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.groupBoxSniffSettings)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelModulationProfile = QtWidgets.QLabel(self.frame)
        self.labelModulationProfile.setObjectName("labelModulationProfile")
        self.verticalLayout_2.addWidget(self.labelModulationProfile)
        self.comboBoxModulationProfiles = QtWidgets.QComboBox(self.frame)
        self.comboBoxModulationProfiles.setObjectName("comboBoxModulationProfiles")
        self.verticalLayout_2.addWidget(self.comboBoxModulationProfiles)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelBitLength = QtWidgets.QLabel(self.frame)
        self.labelBitLength.setObjectName("labelBitLength")
        self.gridLayout.addWidget(self.labelBitLength, 0, 3, 1, 1)
        self.labelParamOneValue = QtWidgets.QLabel(self.frame)
        self.labelParamOneValue.setObjectName("labelParamOneValue")
        self.gridLayout.addWidget(self.labelParamOneValue, 1, 7, 1, 1)
        self.labelCarrierFrequencyValue = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCarrierFrequencyValue.sizePolicy().hasHeightForWidth())
        self.labelCarrierFrequencyValue.setSizePolicy(sizePolicy)
        self.labelCarrierFrequencyValue.setObjectName("labelCarrierFrequencyValue")
        self.gridLayout.addWidget(self.labelCarrierFrequencyValue, 0, 1, 1, 1)
        self.labelModulationType = QtWidgets.QLabel(self.frame)
        self.labelModulationType.setObjectName("labelModulationType")
        self.gridLayout.addWidget(self.labelModulationType, 1, 0, 1, 1)
        self.labelBitLengthValue = QtWidgets.QLabel(self.frame)
        self.labelBitLengthValue.setObjectName("labelBitLengthValue")
        self.gridLayout.addWidget(self.labelBitLengthValue, 0, 4, 1, 1)
        self.labelParamOne = QtWidgets.QLabel(self.frame)
        self.labelParamOne.setObjectName("labelParamOne")
        self.gridLayout.addWidget(self.labelParamOne, 1, 6, 1, 1)
        self.labelModulationTypeValue = QtWidgets.QLabel(self.frame)
        self.labelModulationTypeValue.setObjectName("labelModulationTypeValue")
        self.gridLayout.addWidget(self.labelModulationTypeValue, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 2, 1)
        self.labelCarrierFrequency = QtWidgets.QLabel(self.frame)
        self.labelCarrierFrequency.setObjectName("labelCarrierFrequency")
        self.gridLayout.addWidget(self.labelCarrierFrequency, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 5, 2, 1)
        self.labelParamZero = QtWidgets.QLabel(self.frame)
        self.labelParamZero.setObjectName("labelParamZero")
        self.gridLayout.addWidget(self.labelParamZero, 0, 6, 1, 1)
        self.labelParamZeroValue = QtWidgets.QLabel(self.frame)
        self.labelParamZeroValue.setObjectName("labelParamZeroValue")
        self.gridLayout.addWidget(self.labelParamZeroValue, 0, 7, 1, 1)
        self.labelSampleRate = QtWidgets.QLabel(self.frame)
        self.labelSampleRate.setObjectName("labelSampleRate")
        self.gridLayout.addWidget(self.labelSampleRate, 1, 3, 1, 1)
        self.labelSampleRateValue = QtWidgets.QLabel(self.frame)
        self.labelSampleRateValue.setObjectName("labelSampleRateValue")
        self.gridLayout.addWidget(self.labelSampleRateValue, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.btnConfigurationDialog = QtWidgets.QPushButton(self.frame)
