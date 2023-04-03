import pyqtgraph as pg
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT,FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import skewnorm, skewcauchy
from PySide6.QtCore import Slot
plt.style.use('dark_background')

class Peak:
    """



    """
    def __init__(self, peak_type: dict, peak_parameters: dict):
        self.peak_type = peak_type
        self.peak_parameters = peak_parameters
        self.scale()
        self.x = self.get_x()
        self.y = []
        self.noise_y = []
        self.fity = np.zeros(self.x.shape[0])
        self.generate()

    def scale(self):
        self.peak_parameters['sigma'] = self.peak_parameters['sigma']*self.peak_type['scalefactor']

    def get_x(self):
       
        lim_increment = 0.4+self.peak_parameters['sigma']*5
        xlim = [self.peak_parameters['center']-lim_increment,
                self.peak_parameters['center']+lim_increment]
        return np.arange(xlim[0],xlim[1],self.peak_type['resolution'])

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

        self.y = self.peak_parameters['intensity'] * (alpha * (gaussian) + \
                (1 - alpha) * (lorentizian))
        self.noise_y = self.y + (1/self.peak_type['scalefactor'])*self.noise()
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
        return np.random.normal(size=self.x.shape[0],loc=10)*self.peak_parameters['noise']


    def fit(self):

        p0 = [self.peak_parameters['center'],
              self.peak_parameters['sigma'],
              self.peak_parameters['assymetry'],
              self.peak_parameters['intensity'],
              0]
        self.popt, self.pcov = curve_fit(self.fit_function,
                               self.x,
                               self.noise_y,
                               p0 = p0)
        center_opt, sigma_opt, a_opt,intensity,bias = self.popt
        self.fity = self.fit_function(self.x,center_opt,sigma_opt,a_opt, intensity,bias)
        return self


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

        self.plot_noise = self.ax.scatter(self.peak_data.x,self.peak_data.noise_y ,
                                     marker='o',facecolor='#719FF7',
                                     edgecolor='#719FF7', s=10,label='Obs_data')
        self.plot_real = self.ax.plot(self.peak_data.x, self.peak_data.y+self.peak_data.noise_y[:5].mean(), color='#8EF17E', label='real_data')
        self.ax.legend()
        self.ax.set_ylim(-0.03*np.max(self.peak_data.y),np.max(1.3*self.peak_data.noise_y))
        self.draw()

    def plot_fit(self):
        plotfit = self.ax.plot(self.peak_data.x,self.peak_data.fity, color='#FC724D', lw=2, label='Calc_data')
        self.ax.axvline(self.peak_data.peak_parameters['center'], linestyle='--', color='#8EF17E', label='real center')
        self.ax.set_title(f'obs-Center: {self.peak_data.peak_parameters["center"]:.3f}\
        calc-Center: {self.peak_data.popt[0]:.3f}')
        self.ax.legend()
        self.draw()
