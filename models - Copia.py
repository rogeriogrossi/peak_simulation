import pyqtgraph as pg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import skewnorm, skewcauchy
from PySide6.QtCore import Slot
plt.style.use('ggplot')

class Peak:
    def __init__(self, peak_type: dict, peak_parameters: dict):
        self.peak_type = peak_type
        self.peak_parameters = peak_parameters
        self.x = self.get_x()
        self.y = []
        self.fity = []
        self.fitting = False
        self.generate()

    def get_x(self):
        #Larger the standard deviation large the xlim
        lim_increment = 15
        xlim = [self.peak_parameters['center']-lim_increment,
                self.peak_parameters['center']+lim_increment]
        return np.arange(xlim[0],xlim[1],0.1)

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
        # diff = (self.x - self.peak_parameters['center'])
        #
        # #Assymetric std
        # sigma_assymetric = self.peak_parameters['sigma'] / (1 + np.exp(self.peak_parameters['assymetry']*diff))
        #
        #
        # # Gaussian curve
        # gaussian = gaussian = 1/(np.sqrt(2*np.pi*sigma_assymetric))*\
        #                       np.exp(-diff**2/np.sqrt(2*sigma_assymetric))
        #
        # gamma_2 = np.sqrt(2 * np.log(2) * sigma_assymetric)
        # lorentizian = 1 / np.pi * (gamma_2 / (diff + gamma_2) ** 2)
        #
        # #PseudoVoigt if 0<alpha<1
        # self.y = self.peak_parameters['intensity']*(alpha*(gaussian) + (1-alpha)*(lorentizian) +self.noise())
        # return self

    # def gaussian(self, x = None, center = None,
    #              sigma = None, assymetry = None):
    #     """
    #     Values required in order to fit with scipy's curvefit
    #     """
    #     if type(x) == type(None):
    #         x = self.x
    #     if type(center) == type(None):
    #         center = self.peak_parameters['center']
    #     if type(sigma) == type(None):
    #         sigma = self.peak_parameters['sigma']
    #     if type(assymetry) == type(None):
    #         assymetry = self.peak_parameters['assymetry']
    #
    #     var = sigma / (1 + np.exp(assymetry * (x - center)))
    #     gaussian = 1/(np.sqrt(2*np.pi*var))*np.exp(-(x-center)**2/np.sqrt(2*var))
    #     if self.fitting == False:
    #         self.y = self.peak_parameters['intensity'] * (gaussian + self.noise())
    #         return self.y
    #     else:
    #         self.fity = self.peak_parameters['intensity']*gaussian
    #         return self.fity
    #
    # def lorentizian(self, x = None, center = None,
    #              sigma = None, assymetry = None):
    #     """
    #     Values required in order to fit with scipy's curvefit
    #     """
    #
    #     if type(x) == type(None):
    #         x = self.x
    #     if type(center) == type(None):
    #         center = self.peak_parameters['center']
    #     if type(sigma) == type(None):
    #         sigma = self.peak_parameters['sigma']
    #     if type(assymetry) == type(None):
    #         assymetry = self.peak_parameters['assymetry']
    #
    #     var = sigma / (1 + np.exp(assymetry * (x - center)))
    #     gamma_2 = np.sqrt(2 * np.log(2) * var)
    #     lorentizian = 1 / np.pi * (gamma_2 / ((x - center) ** 2 + gamma_2) ** 2)
    #
    #     if self.fitting == False:
    #         self.y = self.peak_parameters['intensity'] * (lorentizian + self.noise())
    #         return self.y
    #     else:
    #         self.fity = self.peak_parameters['intensity']*lorentizian
    #         return self.fity


    def pseudovoigt(self, x = None, center = None,
                 sigma = None, assymetry = None):
        """
        Values required in order to fit with scipy's curvefit
        """
        if type(x) == type(None):
            x = self.x
        if type(center) == type(None):
            center = self.peak_parameters['center']
        if type(sigma) == type(None):
            sigma = self.peak_parameters['sigma']
        if type(assymetry) == type(None):
            assymetry = self.peak_parameters['assymetry']

        var = sigma / (1 + np.exp(assymetry * (x - center)))
        gamma_2 = np.sqrt(2 * np.log(2) * var)
        alpha = self.peak_type['gl_ratio']


        if self.fitting == False:
            pseudo_voigt = alpha * self.gaussian() + (1 - alpha) * self.lorentizian()
            self.y = self.peak_parameters['intensity'] * (pseudo_voigt + self.noise())
            return self.y
        else:
            pseudo_voigt = alpha * self.gaussian(self.x,center,sigma,assymetry) + (1 - alpha) * self.lorentizian(self.x,center,sigma,assymetry)
            self.fity = self.peak_parameters['intensity']*pseudo_voigt+self.y[:10].mean()
            return self.fity


    def noise(self):
        return np.random.randn(self.x.shape[0])*self.peak_parameters['noise']*10


    def fit(self):

        popt, pcov = curve_fit(self.pseudovoigt,
                               self.x,
                               self.y,
                               [3,
                                self.peak_parameters['sigma'],
                                self.peak_parameters['assymetry']])
        center_opt, sigma_opt, a_opt = popt
        print(center_opt)
        self.fitting = True
        self.fity = self.pseudovoigt(self.x,center_opt,sigma_opt,a_opt)
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
        self.draw()

    def plot_fit(self):
        plotfit = self.ax.plot(self.peak_data.x,self.peak_data.fity, color='r', lw=2)
        self.ax.set_title(f'obs-Center: {self.peak_data.peak_parameters["center"]} | calc-Center: ')
        self.draw()
