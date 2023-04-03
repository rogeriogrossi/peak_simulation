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
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(901, 778)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"C:/Users/roger/Downloads/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(100,100,100);\n"
"}")
        MainWindow.setIconSize(QSize(35, 35))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gbType = QGroupBox(self.centralwidget)
        self.gbType.setObjectName(u"gbType")
        font = QFont()
        font.setBold(True)
        self.gbType.setFont(font)
        self.gbType.setStyleSheet(u"QGroupBox{\n"
"color: White;\n"
"}")
        self.gbType.setFlat(False)
        self.gridLayout_2 = QGridLayout(self.gbType)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rbGaussian = QRadioButton(self.gbType)
        self.rbGaussian.setObjectName(u"rbGaussian")
        self.rbGaussian.setStyleSheet(u"QRadioButton {\n"
"    color:  white;\n"
"   font-weight: bold\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
" background-color:  rgba(110, 0, 240, 200);\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
" background-color: White;\n"
"    border:                 2px solid white;\n"
"}")
        self.rbGaussian.setChecked(True)

        self.gridLayout_2.addWidget(self.rbGaussian, 0, 0, 1, 2)

        self.sbRatio = QDoubleSpinBox(self.gbType)
        self.sbRatio.setObjectName(u"sbRatio")
        self.sbRatio.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbRatio.setAccelerated(True)
        self.sbRatio.setMaximum(1.000000000000000)
        self.sbRatio.setSingleStep(0.010000000000000)
        self.sbRatio.setValue(0.200000000000000)

        self.gridLayout_2.addWidget(self.sbRatio, 2, 1, 1, 1)

        self.rbPseudoVoigt = QRadioButton(self.gbType)
        self.rbPseudoVoigt.setObjectName(u"rbPseudoVoigt")
        self.rbPseudoVoigt.setStyleSheet(u"QRadioButton {\n"
"    color:  white;\n"
"   font-weight: bold\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
" background-color:  rgba(110, 0, 240, 200);\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
" background-color: White;\n"
"    border:                 2px solid white;\n"
"}")

        self.gridLayout_2.addWidget(self.rbPseudoVoigt, 0, 3, 1, 1)

        self.rbLorentizian = QRadioButton(self.gbType)
        self.rbLorentizian.setObjectName(u"rbLorentizian")
        self.rbLorentizian.setStyleSheet(u"QRadioButton {\n"
"    color:  white;\n"
"   font-weight: bold\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
" background-color:  rgba(110, 0, 240, 200);\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
" background-color: White;\n"
"    border:                 2px solid white;\n"
"}")

        self.gridLayout_2.addWidget(self.rbLorentizian, 0, 2, 1, 1)

        self.lbRatio = QLabel(self.gbType)
        self.lbRatio.setObjectName(u"lbRatio")
        self.lbRatio.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout_2.addWidget(self.lbRatio, 2, 0, 1, 1)

        self.label_7 = QLabel(self.gbType)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout_2.addWidget(self.label_7, 2, 2, 1, 1)

        self.sbResolution = QDoubleSpinBox(self.gbType)
        self.sbResolution.setObjectName(u"sbResolution")
        self.sbResolution.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbResolution.setDecimals(3)
        self.sbResolution.setMinimum(0.001000000000000)
        self.sbResolution.setMaximum(2.000000000000000)
        self.sbResolution.setSingleStep(0.001000000000000)
        self.sbResolution.setValue(0.010000000000000)

        self.gridLayout_2.addWidget(self.sbResolution, 2, 3, 1, 1)


        self.gridLayout_3.addWidget(self.gbType, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"color: White\n"
"}")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.sbCenter = QDoubleSpinBox(self.groupBox_2)
        self.sbCenter.setObjectName(u"sbCenter")
        self.sbCenter.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbCenter.setDecimals(3)
        self.sbCenter.setMaximum(99.989999999999995)
        self.sbCenter.setSingleStep(0.010000000000000)
        self.sbCenter.setValue(9.330000000000000)

        self.gridLayout.addWidget(self.sbCenter, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.sbAssymetry = QDoubleSpinBox(self.groupBox_2)
        self.sbAssymetry.setObjectName(u"sbAssymetry")
        self.sbAssymetry.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbAssymetry.setMinimum(-1.000000000000000)
        self.sbAssymetry.setMaximum(1.000000000000000)
        self.sbAssymetry.setSingleStep(0.010000000000000)
        self.sbAssymetry.setValue(0.700000000000000)

        self.gridLayout.addWidget(self.sbAssymetry, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.sbIntensity = QDoubleSpinBox(self.groupBox_2)
        self.sbIntensity.setObjectName(u"sbIntensity")
        self.sbIntensity.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbIntensity.setDecimals(0)
        self.sbIntensity.setMinimum(1.000000000000000)
        self.sbIntensity.setMaximum(1000.000000000000000)
        self.sbIntensity.setSingleStep(20.000000000000000)
        self.sbIntensity.setValue(100.000000000000000)

        self.gridLayout.addWidget(self.sbIntensity, 0, 5, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.sbSigma = QDoubleSpinBox(self.groupBox_2)
        self.sbSigma.setObjectName(u"sbSigma")
        self.sbSigma.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbSigma.setDecimals(3)
        self.sbSigma.setMaximum(15.000000000000000)
        self.sbSigma.setSingleStep(0.050000000000000)
        self.sbSigma.setValue(3.000000000000000)

        self.gridLayout.addWidget(self.sbSigma, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.sbNoise = QDoubleSpinBox(self.groupBox_2)
        self.sbNoise.setObjectName(u"sbNoise")
        self.sbNoise.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbNoise.setMaximum(30.000000000000000)
        self.sbNoise.setSingleStep(0.100000000000000)
        self.sbNoise.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.sbNoise, 1, 3, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"color: White\n"
"}")

        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.sbScale = QDoubleSpinBox(self.groupBox_2)
        self.sbScale.setObjectName(u"sbScale")
        self.sbScale.setStyleSheet(u"QDoubleSpinBox {\n"
"    color: white;\n"
"    selection-background-color: black;\n"
"    background:  rgba(110, 0, 240, 200);\n"
"    border: 1px solid white;\n"
"    border-radius: 5px;\n"
"    padding-left: 2px;\n"
"    padding-top: 2px;\n"
"}")
        self.sbScale.setDecimals(4)
        self.sbScale.setMinimum(0.000100000000000)
        self.sbScale.setMaximum(1.000000000000000)
        self.sbScale.setSingleStep(0.001000000000000)
        self.sbScale.setValue(0.010000000000000)

        self.gridLayout.addWidget(self.sbScale, 1, 5, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btExport = QPushButton(self.centralwidget)
        self.btExport.setObjectName(u"btExport")
        self.btExport.setEnabled(True)
        self.btExport.setStyleSheet(u"QPushButton {\n"
"  border-radius: 10px;\n"
"  padding: 5px;\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(117, 0, 248, 180), stop:0.988636 rgba(153, 79, 252, 180));\n"
"color: White;\n"
"font-size: 15px;\n"
"font-weight: bold\n"
"    }\n"
"QPushButton:hover {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 220), stop:0.988636 rgba(153, 79, 252, 220));\n"
"color: #DDDDDD\n"
"    }\n"
"QPushButton:pressed {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 255), stop:0.988636 rgba(153, 79, 252, 255));\n"
"color: #AAAAAA\n"
"}")

        self.gridLayout_6.addWidget(self.btExport, 2, 0, 1, 1)

        self.btFit = QPushButton(self.centralwidget)
        self.btFit.setObjectName(u"btFit")
        self.btFit.setEnabled(True)
        self.btFit.setStyleSheet(u"QPushButton {\n"
"  border-radius: 10px;\n"
"  padding: 5px;\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(117, 0, 248, 180), stop:0.988636 rgba(153, 79, 252, 180));\n"
"color: White;\n"
"font-size: 15px;\n"
"font-weight: bold\n"
"    }\n"
"QPushButton:hover {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 220), stop:0.988636 rgba(153, 79, 252, 220));\n"
"color: #DDDDDD\n"
"    }\n"
"QPushButton:pressed {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 255), stop:0.988636 rgba(153, 79, 252, 255));\n"
"color: #AAAAAA\n"
"}")

        self.gridLayout_6.addWidget(self.btFit, 1, 0, 1, 1)

        self.btPlot = QPushButton(self.centralwidget)
        self.btPlot.setObjectName(u"btPlot")
        self.btPlot.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btPlot.sizePolicy().hasHeightForWidth())
        self.btPlot.setSizePolicy(sizePolicy1)
        self.btPlot.setMinimumSize(QSize(150, 0))
        self.btPlot.setMouseTracking(False)
        self.btPlot.setStyleSheet(u"QPushButton {\n"
"  border-radius: 10px;\n"
"  padding: 5px;\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(117, 0, 248, 180), stop:0.988636 rgba(153, 79, 252, 180));\n"
"color: White;\n"
"font-size: 15px;\n"
"font-weight: bold\n"
"    }\n"
"QPushButton:hover {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 220), stop:0.988636 rgba(153, 79, 252, 220));\n"
"color: #DDDDDD\n"
"    }\n"
"QPushButton:pressed {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.693182, y2:0.693, stop:0.0454545 rgba(110, 0, 240, 255), stop:0.988636 rgba(153, 79, 252, 255));\n"
"color: #AAAAAA\n"
"}")

        self.gridLayout_6.addWidget(self.btPlot, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.graphic = QWidget(self.centralwidget)
        self.graphic.setObjectName(u"graphic")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.graphic.sizePolicy().hasHeightForWidth())
        self.graphic.setSizePolicy(sizePolicy2)
        self.graphic.setStyleSheet(u"QWidget{\n"
"border: 3px solid white;\n"
"background: rgb(85, 0, 255)}")

        self.gridLayout_4.addWidget(self.graphic, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 21))
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
        self.rbPseudoVoigt.setText(QCoreApplication.translate("MainWindow", u"Pseudo-Voigt", None))
        self.rbLorentizian.setText(QCoreApplication.translate("MainWindow", u"Lorentizian", None))
        self.lbRatio.setText(QCoreApplication.translate("MainWindow", u"G/L Ratio:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Peak Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Center:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Assymetry:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Intensity:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u03c3:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Noise:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scale Factor:", None))
#if QT_CONFIG(tooltip)
        self.sbScale.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.sbScale.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.sbScale.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btExport.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.btFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.btPlot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
    # retranslateUi

