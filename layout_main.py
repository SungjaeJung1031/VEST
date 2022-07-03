import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtOpenGL import *
import OpenGL.GL as gl          # python wrapping of OpenGL
from OpenGL import GLU          # OpenGL Utility Library, extends OpenGL functionality
from OpenGL.arrays import vbo    # used to store VBO data

from widget.plotter.plotter_3d import Plotter3D
from widget.plotter.plotter_3d_option import Plotter3dOption
from widget.plotter.plotter_3d_prog import Plotter3dProg

class LayoutMain(QHBoxLayout):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
    
        self.splt_main = QSplitter()
        self.splt_plotter_3d = QSplitter(Qt.Vertical)

        self.gbox_plotter_3d = QGroupBox('3D-Plotter')
        self.vlyt_plotter_3d = QVBoxLayout()

        self.plotter_3d = Plotter3D(self.main_window)
        self.plotter_3d_prog = Plotter3dProg(o_plot3d=self.plotter_3d)
        self.plotter_3d_opt = Plotter3dOption(o_plot3d=self.plotter_3d)
        

        self.setTimerPlotter3D()

        self.splt_plotter_3d.addWidget(self.plotter_3d_prog)
        self.splt_plotter_3d.addWidget(self.plotter_3d)
        self.splt_plotter_3d.addWidget(self.plotter_3d_opt)
        self.splt_plotter_3d.setSizes([100, 800, 100])
        
        self.vlyt_plotter_3d.addWidget(self.splt_plotter_3d)



        self.gbox_plotter_3d.setLayout(self.vlyt_plotter_3d)

        self.splt_main.addWidget(QGroupBox('group 1'))
        self.splt_main.addWidget(self.gbox_plotter_3d)
        self.splt_main.addWidget(QGroupBox('group 1'))
        
        self.splt_main.setSizes([100, 800, 100])


        self.addWidget(self.splt_main)

    def setTimerPlotter3D(self):
        timerPlotter3D = QTimer(self.main_window)
        timerPlotter3D.setInterval(20)      # period, in milliseconds
        timerPlotter3D.timeout.connect(self.plotter_3d.updateGL)
        timerPlotter3D.start()

    def initRender(self):
        self.plotter_3d_prog.initRender()
        self.plotter_3d.initRender()
        self.plotter_3d_opt.initRender()