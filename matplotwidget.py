from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from create_figure import *


class MatPlotWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.canvas = FigureCanvasQTAgg(Figure())
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(projection='3d')
        self.canvas.axes.set_box_aspect(aspect=(1, 1, 1))
        self.canvas.axes.set_axis_off()
        self.setLayout(layout)
        self.canvas.axes.set_xlabel('x')
        self.canvas.axes.set_ylabel('y')
        self.canvas.axes.set_zlabel('z')
        self.canvas.axes.set_xlim3d(0, 1000)
        self.canvas.axes.set_ylim3d(0, 1000)
        self.canvas.axes.set_zlim3d(0, 1000)

    def update_screen(self, figure, params):
        self.canvas.axes.clear()

        if CreateFigure.get_figure() == "круг":
            X = params[0]
            u = np.linspace(0, 2 * np.pi, 100)
            x = np.cos(u) * X
            y = np.sin(u) * X
            self.canvas.axes.plot(x, y, 0)
            self.canvas.axes.set_box_aspect(aspect=(X, X, 0))

        elif CreateFigure.get_figure() == "квадрат":
            x = params[0]
            self.canvas.axes.plot([0, x, x, 0, 0], [0, 0, x, x, 0], [0, 0, 0, 0, 0])
            self.canvas.axes.set_box_aspect(aspect=(x, x, 0))

        elif CreateFigure.get_figure() == "прямоугольник":
            x = params[0]
            y = params[1]
            self.canvas.axes.plot([0, x, x, 0, 0], [0, 0, y, y, 0], [0, 0, 0, 0, 0])
            self.canvas.axes.set_box_aspect(aspect=(x, y, 0))

        elif CreateFigure.get_figure() == "треугольник":
            x = params[0]
            y = params[1]
            a = params[2] * np.pi / 180
            endy = y * np.sin(a)
            endx = x * np.cos(a)
            self.canvas.axes.plot([0, x, (x - endx), 0], [0, 0, y, 0], [0, 0, 0, 0])
            self.canvas.axes.set_box_aspect(aspect=(x, y, 0))

        elif CreateFigure.get_figure() == "трапеция":
            x = params[0]
            y = params[1]
            h = params[2]
            self.canvas.axes.plot([0, 0, y, x, 0], [0, h, h, 0, 0], [0, 0, 0, 0, 0])
            self.canvas.axes.set_box_aspect(aspect=(x, h, 0))

        elif CreateFigure.get_figure() == "ромб":
            x = params[0]
            a = params[1] * np.pi / 180
            b = (180 - params[1]) * np.pi / 180
            endy = x * np.sin(a)
            endx = x * np.cos(a)
            print(endx)
            print(endy)
            print(x + endx)
            print(x - endx)
            print(x + endy)
            print(x - endy)

            self.canvas.axes.plot([0, x, (x - endx)], [0, 0, endy],
                                  [0, 0, 0], color='b')
            self.canvas.axes.plot([0, -endx, (x + -endx)], [0,  endy, endy],
                                  [0, 0, 0], color='b')
            #self.canvas.axes.set_box_aspect(aspect=((x - endx), (x - endx), 0))
            self.canvas.axes.set_xlim3d(0, x - endx)
            self.canvas.axes.set_ylim3d(0, x - endx)
            self.canvas.axes.set_zlim3d(0, 0)

        elif CreateFigure.get_figure() == "сфера":
            u = np.linspace(0, 2 * np.pi, 100)
            v = np.linspace(0, np.pi, 100)
            x = params[0] * np.outer(np.cos(u), np.sin(v))
            y = params[0] * np.outer(np.sin(u), np.sin(v))
            z = params[0] * np.outer(np.ones(np.size(u)), np.cos(v))
            self.canvas.axes.plot_surface(x, y, z)
            self.canvas.axes.set_box_aspect(aspect=(params[0], params[0], params[0]))

        elif CreateFigure.get_figure() == "куб":
            x = params[0]
            self.canvas.axes.plot([0, x, x, 0, 0], [0, 0, x, x, 0], [0, 0, 0, 0, 0], color='b')
            self.canvas.axes.plot([0, 0, x, x], [0, 0, 0, 0], [0, x, x, 0], color='b')
            self.canvas.axes.plot([x, x, x, x], [0, 0, x, x], [0, x, x, 0], color='b')
            self.canvas.axes.plot([x, x, 0, 0], [x, x, x, x], [0, x, x, 0], color='b')
            self.canvas.axes.plot([0, 0, 0], [x, x, 0], [0, x, x], color='b')
            self.canvas.axes.set_box_aspect(aspect=(x, x, x))

        elif CreateFigure.get_figure() == "паралепипед":
            x = params[0]
            y = params[1]
            z = params[2]
            self.canvas.axes.plot([0, x, x, 0, 0], [0, 0, y, y, 0], [0, 0, 0, 0, 0], color='b')
            self.canvas.axes.plot([0, 0, x, x], [0, 0, 0, 0], [0, z, z, 0], color='b')
            self.canvas.axes.plot([x, x, x, x], [0, 0, y, y], [0, z, z, 0], color='b')
            self.canvas.axes.plot([x, x, 0, 0], [y, y, y, y], [0, z, z, 0], color='b')
            self.canvas.axes.plot([0, 0, 0], [y, y, 0], [0, z, z], color='b')
            self.canvas.axes.set_box_aspect(aspect=(x, y, z))

        elif CreateFigure.get_figure() == "пирамида":
            def pc(t):
                x = np.cos(t) * (np.cos(an / 2) / (np.cos(an * (t / an - np.floor(t / an)) - an / 2)))
                return x

            def ps(t):
                y = np.sin(t) * (np.cos(an / 2) / (np.cos(an * (t / an - np.floor(t / an)) - an / 2)))
                return y

            n = params[1]
            an = 2 * np.pi / n

            v = np.linspace(0, 2 * np.pi, 100)
            u = np.linspace(0, np.pi, 100)
            v, u = np.meshgrid(v, u)

            x = ps(u) * pc(v) * params[0]
            y = ps(u) * ps(v) * params[0]
            z = pc(u) * params[2]
            z[z <= 0.02] = np.nan

            self.canvas.axes.plot_surface(x, y, z)
            self.canvas.axes.set_box_aspect(aspect=(params[0], params[0], params[2]))

        elif CreateFigure.get_figure() == "цилиндр":
            def data_for_cylinder_along_z(center_x, center_y, radius, height_z):
                z = np.linspace(0, height_z, 50)
                theta = np.linspace(0, 2 * np.pi, 50)
                theta_grid, z_grid = np.meshgrid(theta, z)
                x_grid = radius * np.cos(theta_grid) + center_x
                y_grid = radius * np.sin(theta_grid) + center_y
                return x_grid, y_grid, z_grid

            x, y, z = data_for_cylinder_along_z(0, 0, params[0], params[1])
            self.canvas.axes.plot_surface(x, y, z)
            self.canvas.axes.set_box_aspect(aspect=(x, y, z))

        elif CreateFigure.get_figure() == "конус":
            theta = np.linspace(0, 2 * np.pi, 100)
            r = np.linspace(0, 2, 100)
            t, R = np.meshgrid(theta, r)

            x = R * np.cos(t) * params[0]
            y = R * np.sin(t) * params[0]
            z = (-R * 2.5 + 5) * (params[1]) / 5

            self.canvas.axes.plot_surface(x, y, z)
            self.canvas.axes.set_box_aspect(aspect=(x, y, z))

        #self.canvas.axes.set_axis_off()
        self.canvas.draw()
