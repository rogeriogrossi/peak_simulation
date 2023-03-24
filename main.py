from main_window import *
from models import *
from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication
import sys
from qt_material import list_themes, apply_stylesheet
matplotlib.use('Qt5Agg')

class PeakWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, parent = None):
        super(PeakWindow, self).__init__(parent)
        super().setupUi(self)
        #Type dict
        self.type_dict = {}
        self.get_peak_type()
        self.rbGaussian.toggled.connect(lambda :self.get_peak_type())
        self.rbLorentizian.toggled.connect(lambda :self.get_peak_type())
        self.rbPseudoVoigt.toggled.connect(lambda :self.get_peak_type())
        self.sbRatio.valueChanged.connect(lambda :self.get_peak_type())

        #Peak parameters
        self.peak_dict = {}
        self.get_peak_parameters()
        self.sbCenter.valueChanged.connect(lambda: self.get_peak_parameters())
        self.sbSigma.valueChanged.connect(lambda: self.get_peak_parameters())
        self.sbAssymetry.valueChanged.connect(lambda: self.get_peak_parameters())
        self.sbNoise.valueChanged.connect(lambda: self.get_peak_parameters())
        self.sbIntensity.valueChanged.connect(lambda: self.get_peak_parameters())
        self.sbResolution.valueChanged.connect(lambda: self.get_peak_parameters())

        #Peak
        self.peak = Peak(self.type_dict, self.peak_dict)

        #Figure
        self.matplotfig = MatplotGraphic(self.peak)
        self.wtoobar = NavigationToolbar2QT(self.matplotfig, self)
        self.addToolBar(self.wtoobar)
        # self.horizontalLayout.removeWidget(self.graphic)
        self.gridLayout_4.addWidget(self.matplotfig, 1, 0, 1, 1)

        #Buttons
        self.btPlot.clicked.connect(self.plot)
        self.btFit.clicked.connect(self.plot_fit)
        #Plot
        self.plot()

    def get_peak_type(self):
        type_dict = {}
        #Radio Buttom selected
        if self.rbGaussian.isChecked():
            type_dict['type'] = 'gaussian'
        elif self.rbLorentizian.isChecked():
            type_dict['type'] = 'lorentizian'
        else:
            type_dict['type'] = 'pseudovoigt'
        #Gaussian/Lorentizian ratio
        type_dict['gl_ratio'] = np.round(self.sbRatio.value(),2)
        self.type_dict = type_dict
        return self


    def get_peak_parameters(self):
        self.peak_dict['center'] = self.sbCenter.value()
        self.peak_dict['sigma'] = self.sbSigma.value()
        self.peak_dict['assymetry'] = self.sbAssymetry.value()
        self.peak_dict['noise'] = self.sbNoise.value()
        self.peak_dict['intensity'] = self.sbIntensity.value()
        self.peak_dict['resolution'] = self.sbResolution.value()
        return self


    def plot(self):
        self.peak = Peak(self.type_dict, self.peak_dict)
        self.matplotfig = MatplotGraphic(self.peak)
        self.removeToolBar(self.wtoobar)
        self.wtoobar = NavigationToolbar2QT(self.matplotfig, self)
        self.addToolBar(self.wtoobar)
        # self.horizontalLayout.removeWidget(self.graphic)
        self.gridLayout_4.addWidget(self.matplotfig, 1, 0, 1, 1)

    def plot_fit(self):
        self.peak.fit()
        self.matplotfig.plot_fit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    peak_window = PeakWindow()
    peak_window.show()
    app.exec()