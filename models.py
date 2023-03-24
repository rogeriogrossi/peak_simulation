import pyqtgraph as pg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import skewnorm, skewcauchy
from PySide6.QtCore import Slot
plt.style.use('bmh')

class Peak:
    def __init__(self, peak_type: dict, peak_parameters: dict):
        self.peak_type = peak_type
        self.peak_parameters = peak_parameters
        self.x = self.get_x()
        self.y = []
        self.fity = []
        self.generate()

    def get_x(self):
        #Larger the standard deviation large the xlim
        lim_increment = 15
        xlim = [self.peak_parameters['center']-lim_increment,
                self.peak_parameters['center']+lim_increment]
        return np.arange(xlim[0],xlim[1],self.peak_parameters['resolution'])

    def generate(self):
        if self.peak_type['type'] == 'gaussian':
            alpha = 1
        elif self.peak_type['type'] == 'lorentizian':
            alpha = 0
        elif self.peak_type['type'] == 'pseudovoigt':
            alpha = self.peak_type['gl_ratio']

        gaussian = skewnorm.pdf(self.x,
                                self.peak_parameters['assymetry'],
                                loc=self.peak_parameters['center'],
                                scale=self.peak_parameters['sigma'])

        lorentizian = skewcauchy.pdf(self.x,
                                self.peak_parameters['assymetry'],
                                loc=self.peak_parameters['center'],
                                scale=self.peak_parameters['sigma'])

        self.y = self.peak_parameters['intensity'] * (alpha * (gaussian) + (1 - alpha) * (lorentizian)) + self.noise()
        return self



    def fit_function(self, x, center, sigma, assymetry,intensity, bias):

        if self.peak_type['type'] == 'gaussian':
            alpha = 1
        elif self.peak_type['type'] == 'lorentizian':
            alpha = 0
        elif self.peak_type['type'] == 'pseudovoigt':
            alpha = self.peak_type['gl_ratio']

        gaussian = skewnorm.pdf(x,
                                assymetry,
                                loc=center,
                                scale=sigma)

        lorentizian = skewcauchy.pdf(x,
                                assymetry,
                                loc=center,
                                scale=sigma)

        y = intensity * (alpha * (gaussian) + (1 - alpha) * (lorentizian))+bias
        return y


    def noise(self):
        return np.random.normal(size=self.x.shape[0],loc=10)*self.peak_parameters['noise']*6


    def fit(self):

        p0 = [self.peak_parameters['center'],
              self.peak_parameters['sigma'],
              self.peak_parameters['assymetry'],
              self.peak_parameters['intensity'],
              0]
        self.popt, self.pcov = curve_fit(self.fit_function,
                               self.x,
                               self.y,
                               p0 = p0)
        center_opt, sigma_opt, a_opt,intensity,bias = self.popt
        self.fity = self.fit_function(self.x,center_opt,sigma_opt,a_opt, intensity,bias)
        return self

    def get_data(self):
        pass





class MatplotGraphic(FigureCanvasQTAgg):
    def __init__(self, peak_data: Peak,width=10, height=7,dpi=150):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.peak_data = peak_data
        self.plot()

    def plot(self):
        self.fig.clear()
        self.ax.cla()
        self.ax = self.fig.add_subplot(111)
        self.plot1 = self.ax.scatter(self.peak_data.x, self.peak_data.y, marker='o',facecolor='b',
                                     edgecolor='b', s=10,label='Obs_data')
        self.ax.legend()
        self.draw()

    def plot_fit(self):
        plotfit = self.ax.plot(self.peak_data.x,self.peak_data.fity, color='r', lw=2, label='Calc_data')
        self.ax.axvline(self.peak_data.peak_parameters['center'], linestyle='--', color='green', label='real center')
        self.ax.set_title(f'obs-Center: {self.peak_data.peak_parameters["center"]} | calc-Center: {self.peak_data.popt[0]:.2f}')
        self.ax.legend()
        self.draw()
