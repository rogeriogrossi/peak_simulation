# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(896, 769)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 11, 831, 691))
        self.gridLayout_4 = QGridLayout(self.layoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gbType = QGroupBox(self.layoutWidget)
        self.gbType.setObjectName(u"gbType")
        font = QFont()
        font.setBold(True)
        self.gbType.setFont(font)
        self.gbType.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.gbType)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rbGaussian = QRadioButton(self.gbType)
        self.rbGaussian.setObjectName(u"rbGaussian")
        self.rbGaussian.setChecked(True)

        self.gridLayout_2.addWidget(self.rbGaussian, 0, 0, 1, 2)

        self.rbLorentizian = QRadioButton(self.gbType)
        self.rbLorentizian.setObjectName(u"rbLorentizian")

        self.gridLayout_2.addWidget(self.rbLorentizian, 0, 2, 1, 1)

        self.rbPseudoVoigt = QRadioButton(self.gbType)
        self.rbPseudoVoigt.setObjectName(u"rbPseudoVoigt")

        self.gridLayout_2.addWidget(self.rbPseudoVoigt, 0, 3, 1, 1)

        self.lbRatio = QLabel(self.gbType)
        self.lbRatio.setObjectName(u"lbRatio")

        self.gridLayout_2.addWidget(self.lbRatio, 1, 0, 1, 1)

        self.sbRatio = QDoubleSpinBox(self.gbType)
        self.sbRatio.setObjectName(u"sbRatio")
        self.sbRatio.setAccelerated(True)
        self.sbRatio.setMaximum(1.000000000000000)
        self.sbRatio.setSingleStep(0.010000000000000)
        self.sbRatio.setValue(0.200000000000000)

        self.gridLayout_2.addWidget(self.sbRatio, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 3, 1, 1)


        self.gridLayout_3.addWidget(self.gbType, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.sbCenter = QDoubleSpinBox(self.groupBox_2)
        self.sbCenter.setObjectName(u"sbCenter")
        self.sbCenter.setDecimals(3)
        self.sbCenter.setMaximum(99.989999999999995)
        self.sbCenter.setSingleStep(0.010000000000000)
        self.sbCenter.setValue(9.330000000000000)

        self.gridLayout.addWidget(self.sbCenter, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.sbAssymetry = QDoubleSpinBox(self.groupBox_2)
        self.sbAssymetry.setObjectName(u"sbAssymetry")
        self.sbAssymetry.setMinimum(-1.000000000000000)
        self.sbAssymetry.setMaximum(1.000000000000000)
        self.sbAssymetry.setSingleStep(0.010000000000000)
        self.sbAssymetry.setValue(0.700000000000000)

        self.gridLayout.addWidget(self.sbAssymetry, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.sbIntensity = QDoubleSpinBox(self.groupBox_2)
        self.sbIntensity.setObjectName(u"sbIntensity")
        self.sbIntensity.setDecimals(0)
        self.sbIntensity.setMinimum(1.000000000000000)
        self.sbIntensity.setMaximum(300.000000000000000)
        self.sbIntensity.setSingleStep(20.000000000000000)
        self.sbIntensity.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.sbIntensity, 0, 5, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.sbSigma = QDoubleSpinBox(self.groupBox_2)
        self.sbSigma.setObjectName(u"sbSigma")
        self.sbSigma.setDecimals(3)
        self.sbSigma.setMaximum(15.000000000000000)
        self.sbSigma.setSingleStep(0.050000000000000)
        self.sbSigma.setValue(3.000000000000000)

        self.gridLayout.addWidget(self.sbSigma, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.sbNoise = QDoubleSpinBox(self.groupBox_2)
        self.sbNoise.setObjectName(u"sbNoise")
        self.sbNoise.setMaximum(30.000000000000000)
        self.sbNoise.setSingleStep(0.100000000000000)
        self.sbNoise.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.sbNoise, 1, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.sbResolution = QDoubleSpinBox(self.groupBox_2)
        self.sbResolution.setObjectName(u"sbResolution")
        self.sbResolution.setDecimals(3)
        self.sbResolution.setMinimum(0.001000000000000)
        self.sbResolution.setMaximum(2.000000000000000)
        self.sbResolution.setSingleStep(0.001000000000000)
        self.sbResolution.setValue(0.010000000000000)

        self.gridLayout.addWidget(self.sbResolution, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btPlot = QPushButton(self.layoutWidget)
        self.btPlot.setObjectName(u"btPlot")
        self.btPlot.setEnabled(True)

        self.verticalLayout.addWidget(self.btPlot)

        self.btFit = QPushButton(self.layoutWidget)
        self.btFit.setObjectName(u"btFit")
        self.btFit.setEnabled(True)

        self.verticalLayout.addWidget(self.btFit)

        self.btExport = QPushButton(self.layoutWidget)
        self.btExport.setObjectName(u"btExport")
        self.btExport.setEnabled(True)

        self.verticalLayout.addWidget(self.btExport)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.graphic = QWidget(self.layoutWidget)
        self.graphic.setObjectName(u"graphic")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.graphic.sizePolicy().hasHeightForWidth())
        self.graphic.setSizePolicy(sizePolicy1)
        self.graphic.setStyleSheet(u"background: rgb(85, 0, 255)")

        self.gridLayout_4.addWidget(self.graphic, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 896, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Peak Simulation", None))
        self.gbType.setTitle(QCoreApplication.translate("MainWindow", u"Peak Type", None))
        self.rbGaussian.setText(QCoreApplication.translate("MainWindow", u"Gaussian", None))
        self.rbLorentizian.setText(QCoreApplication.translate("MainWindow", u"Lorentizian", None))
        self.rbPseudoVoigt.setText(QCoreApplication.translate("MainWindow", u"Pseudo-Voigt", None))
        self.lbRatio.setText(QCoreApplication.translate("MainWindow", u"G/L Ratio:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Peak Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Assymetry:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intensity:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u03c3:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Noise:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.btPlot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.btFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.btExport.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
    # retranslateUi

