from statistics import variance
from typing import overload
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6 import QtGui, QtCore
import PySide6.QtGui as qgui
from graphics_ground import GraphicsGround
from graphics_axes import GraphicsAxes
from graphics_triangle import GraphicsTriangle
from OpenGL.GL.shaders import compileProgram,compileShader

import OpenGL.GL as gl              # python wrapping of OpenGL
import OpenGL.GLU as glu            # OpenGL Utility Library, extends OpenGL functionality
import OpenGL.GLUT as glut
import numpy as np


class TopViewAnnotationPage(QOpenGLWidget):
    """
    This class defines the Qt OpenGL widget, which is the main object for performing all openGL
    graphics programming.  The functions initializeGL, resizeGL, paintGL must be defined.
    """
    
    def __init__(self, annotation_page = None):
        """ Initialize the Qt OpenGL Widget.
        Initialize the Qt OpenGL widget.
        Args:
            (None)
        Returns:
            (None)
        """
        self.annotation_page = annotation_page
        
        QOpenGLWidget.__init__(self, annotation_page)

        self.glf = QtGui.QOpenGLFunctions()

        # Initialize the camera state and set the initial view
        self.eye_r = 7.0            # camera radius, in meters
        self.eye_th = -1.5707       # camera azimuth angle, in radians
        self.eye_phi = 0.8          # camera elevation angle, in radians
        self.center_pos = np.array([0.0, 0.0, 0.0])

    def initializeGL(self) -> None:
        """ Initializes OpenGL functionality and geometry.

        Virtual function provided by QGLWidget, called once at the beginning of application.
        OpenGL and geometry initialization is performed here.

        Args:
            (None)

        Returns:
            (None)

        """

        # Convenience function, calls glClearColor under the hood.
        # QColor is specified as RGB ints (0-255).  Specify this clear
        # color once and call glClear(GL_COLOR_BUFFER_BIT) before each
        # round of rendering (in paintGL):
        self.glf.initializeOpenGLFunctions()
        # self.glf.glClearColor(0.96078, 0.96078, 0.96078, 1.0) # F5F5F5
        self.glf.glClearColor(0, 0, 0, 1.0) # F5F5F5
        # # Enable the depth buffer:
        self.glf.glEnable(gl.GL_DEPTH_TEST)

        # Initialize the ground plane graphics geometry
        graphic_ground_num_grid = 200
        grahpic_ground_grid_scale_factor = 0.5
        unit_vector_scale_factor = graphic_ground_num_grid * 0.5 / float(graphic_ground_num_grid+1)

        # self.graphics_ground = GraphicsGround(num_grid=graphic_ground_num_grid, 
        #                                     grid_scale_factor=grahpic_ground_grid_scale_factor)

        self.graphics_origin_axes = GraphicsAxes()

        self.updateView()

        # Set focus to the window
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def paintGL(self) -> None:

        # Start from a blank slate each render by clearing buffers
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # self.graphics_ground.render()
        self.graphics_origin_axes.render(np.identity(3), np.zeros(3))

    def updateView(self) -> None:
        """ Updates the camera view using current camera state.
        Function to be called after updating any camera state variable in order to update
        the camera view. Converts spherical camera coordinates to a Cartesian position for
        the eye of the camera, with the center position (focal point) fixed at the origin.
        Args:
            (None)
        Returns:
            (None)
        """
        self.eye_pos = np.array([self.eye_r*np.sin(self.eye_phi)*np.cos(self.eye_th),
                                 self.eye_r*np.sin(self.eye_phi)*np.sin(self.eye_th),
                                 self.eye_r*np.cos(self.eye_phi)])
        up_vec = np.array([0.0, 0.0, 1.0])
        
        # glu.gluLookAt(*np.concatenate((self.eye_pos, self.center_pos, up_vec)))

    def orientCamera(self) -> None:
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()

    def resizeGL(self, w: int, h: int) -> None:
        pass

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """ Defines callbacks for keypress events.
        Implement override for virtual function provided by Qt base class for defining
        keypress event callbacks, for example manipulating the primary view camera.
        Args:
            event (QKeyEvent): Screen width in pixels.
            height (int): Screen height in pixels.
        Returns:
            (None)
        """
        if type(event) == QtGui.QKeyEvent:
            if event.key() == QtCore.Qt.Key_W:
                # Hold W to decrease radius (zoom in)
                self.eye_r -= 0.5
                print(self.eye_phi)
                self.updateView()
                
            elif event.key() == QtCore.Qt.Key_S:
                # Hold S to increase radius (zoom out)
                self.eye_r += 0.5
                print(self.eye_phi)
                self.updateView()

            elif event.key() == QtCore.Qt.Key_Down:
                # Hold DOWNARROW to increase elevation angle 
                self.eye_phi += 0.05
                print(self.eye_phi)
                self.updateView()

            elif event.key() == QtCore.Qt.Key_Up:
                # Hold UPARROW to decrease elevation angle
                self.eye_phi -= 0.05
                print(self.eye_phi)
                self.updateView()

            elif event.key() == QtCore.Qt.Key_Right:
                # Hold RIGHTARROW to increase azimuth angle
                self.eye_th += 0.05
                print(self.eye_phi)
                self.updateView()

            elif event.key() == QtCore.Qt.Key_Left:
                # Hold LEFTARROW to decrease azimuth angle
                self.eye_th -= 0.05
                print(self.eye_phi)
                self.updateView()

    def initRender(self):
        self.paintGL()
        # gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        # gl.glFlush()
    
