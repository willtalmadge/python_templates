import os
import sys

import PyQt4
import PyQt4.uic
import matplotlib.figure
import matplotlib.pyplot
import numpy as np
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from qt_template import pkg_dir

# We defined the widgets and layout with QTCreator instead of programmatically
window_form, QMainWindow = PyQt4.uic.loadUiType(os.path.join(pkg_dir, 'ui', 'main_window.ui'))


class PlotWindow(QMainWindow, window_form):
    def __init__(self):
        super(PlotWindow, self).__init__()
        self.canvas = None
        self.setupUi(self)

        self.sine_button.clicked.connect(self.plot_sine)
        self.sqrt_button.clicked.connect(self.plot_sqrt)

        self.fig = matplotlib.pyplot.figure('main_fig')
        self.ax = self.fig.add_subplot(111)

        self.set_figure(self.fig)

    def set_figure(self, fig):
        """
        We created a vertical layout inside of the 'plot_widget' widget in QTCreator. The vertical layout
        allows us to insert a toolbar and figure under that widget and have them fill the widget space
        and be stacked.
        :param fig: a matplotlib figure object
        :return: None
        """

        # Clear out the wold figure to make way for the new one
        if self.canvas is not None:
            self.plot_layout.removeWidget(self.canvas)
            self.plot_layout.removeWidget(self.toolbar)
            self.canvas.close()
            self.toolbar.close()

        self.canvas = FigureCanvas(fig)
        self.plot_layout.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas,
                                         self.plot_widget, coordinates=True)
        self.plot_layout.addWidget(self.toolbar)

    def plot_sine(self):
        """
        Clear the figure and plot a simple sine function. We clear the plot and replot rather than replacing it
        since that is a lot more efficient
        :return:
        """
        matplotlib.pyplot.figure('main_fig')
        self.ax.clear()
        xs = np.linspace(0, 2 * np.pi, 500)
        ys = np.sin(xs)
        self.ax.plot(xs, ys)
        self.fig.canvas.draw()

    def plot_sqrt(self):
        """
        Clear the plot and plot a sqrt function
        :return:
        """
        matplotlib.pyplot.figure('main_fig')
        self.ax.clear()
        xs = np.linspace(0, 4, 500)
        ys = np.sqrt(xs)
        self.ax.plot(xs, ys)
        self.fig.canvas.draw()


def main():
    app = QtGui.QApplication(sys.argv)
    main = PlotWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
