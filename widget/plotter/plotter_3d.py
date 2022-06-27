
from PyQt5.QtCore import Qt         # core Qt functionality
from PyQt5.QtGui import QColor, \
                        QKeyEvent   # extends QtCore with GUI functionality    
from PyQt5.QtOpenGL import *        # provides QGLWidget, a special OpenGL QWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtOpenGL import QGLWidget

import OpenGL.GL as gl              # python wrapping of OpenGL
from OpenGL import GLU              # OpenGL Utility Library, extends OpenGL functionality

import sys                          # we'll need this later to run our Qt application

from OpenGL.arrays import vbo       # used to store VBO data
import numpy as np
from value_types.enum_color import EnumColor                  # general matrix/array math

from widget.plotter.detection_graphics import DetectionGraphics
from widget.plotter.fov_graphics import FovGraphics
from widget.plotter.object_graphics import ObjectGraphics
from widget.plotter.vector_graphics import VectorGraphics
from widget.plotter.ground_graphics import GroundGraphics

from value_types.valtype_object import DataclsObject


            
class AxesGraphics(object):
    """
    Class for rendering an axes (frame vectors) object.
    """
    
    def __init__(self):
        self.x_axis = VectorGraphics()
        self.y_axis = VectorGraphics()
        self.z_axis = VectorGraphics()

        self.tmp_datacls_obj = DataclsObject()

        self.tmp_dtct = DetectionGraphics(0.0, 0.0, 0.0, 0)
        self.tmp_object = ObjectGraphics(self.tmp_datacls_obj, 1.0, EnumColor.RED)
        self.tmp_fov = FovGraphics()

    def render(self, R, t):
        self.x_axis.render(t, R[:,0],
                           0.3, 0.01, np.array([1.0, 0.0, 0.0]))
        self.y_axis.render(t, R[:,1
        ],
                           0.3, 0.01, np.array([0.0, 1.0, 0.0]))
        self.z_axis.render(t, R[:,2],
                           0.3, 0.01, np.array([0.0, 0.0, 1.0]))

        self.tmp_dtct.render()
        self.tmp_object.render()
        self.tmp_fov.render()

            
class Plotter3D(QGLWidget):
    """
    This class defines the Qt OpenGL widget, which is the main object for performing all openGL
    graphics programming.  The functions initializeGL, resizeGL, paintGL must be defined.
    """

    def __init__(self, main_window=None):
        """ Initialize the Qt OpenGL Widget.
        Initialize the Qt OpenGL widget.
        Args:
            (None)
        Returns:
            (None)
        """
        # Store reference to and initialize the parent class
        self.main_window = main_window
        QGLWidget.__init__(self, main_window)

        # Initialize geometry if necessary
        self.initGeometry()

        
    def initializeGL(self):
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
        self.qglClearColor(QColor(255, 255, 255)) # a grey background
                
        # Enable the depth buffer:
        gl.glEnable(gl.GL_DEPTH_TEST)

        # Initialize the user-specified geometry
        self.initGeometry()

        # Initialize the ground plane graphics geometry
        self.ground_graphics = GroundGraphics(length=400.0, width=400.0)

        # Initialize the origin axes graphics geometry
        self.origin_axes_graphics = AxesGraphics()
        
        # Initialize the camera state and set the initial view
        self.eye_r = 7.0     # camera radius, in meters
        self.eye_th = -1.5707     # camera azimuth angle, in radians
        self.eye_phi = 0.8   # camera elevation angle, in radians
        self.center_pos = np.array([0.0, 0.0, 0.0])
        self.update_view()

        # Set focus to the window
        self.setFocusPolicy(Qt.StrongFocus)

        
    def keyPressEvent(self, event):
        """ Defines callbacks for keypress events.
        Implement override for virtual function provided by Qt base class for defining
        keypress event callbacks, for example manipulating the primary view camera.
        Args:
            event (QKeyEvent): Screen width in pixels.
            height (int): Screen height in pixels.
        Returns:
            (None)
        """
        if type(event) == QKeyEvent:
            if event.key() == Qt.Key_W:
                # Hold W to decrease radius (zoom in)
                self.eye_r -= 0.5
                self.update_view()
                
            elif event.key() == Qt.Key_S:
                # Hold S to increase radius (zoom out)
                self.eye_r += 0.5
                self.update_view()

            elif event.key() == Qt.Key_Down:
                # Hold DOWNARROW to increase elevation angle 
                self.eye_phi += 0.05
                self.update_view()

            elif event.key() == Qt.Key_Up:
                # Hold UPARROW to decrease elevation angle
                self.eye_phi -= 0.05
                self.update_view()

            elif event.key() == Qt.Key_Right:
                # Hold RIGHTARROW to increase azimuth angle
                self.eye_th += 0.05
                self.update_view()

            elif event.key() == Qt.Key_Left:
                # Hold LEFTARROW to decrease azimuth angle
                self.eye_th -= 0.05
                self.update_view()

                
    def update_view(self):
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
        gl.glLoadIdentity()
        GLU.gluLookAt(*np.concatenate((self.eye_pos, self.center_pos, up_vec)))

        
    def resizeGL(self, width, height):
        """ Defines behavior of OpenGL window when resized.
        Virtual function provided by QGLWidget, called once at the beginning of application
        to set up the OpenGL viewing volume and then called each time the window is resized
        by the user.
        Args:
            width (int): Screen width in pixels.
            height (int): Screen height in pixels.
        Returns:
            (None)
        """
        # Create the viewport, using the full window size
        gl.glViewport(0, 0, width, height)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        aspect = width / float(height)

        # Define the viewing volume (frustrum)
        GLU.gluPerspective(45.0, aspect, 1.0, 100.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

        
    def paintGL(self):
        """ Defines behavior of OpenGL window when resized.
        Virtual function provided by QGLWidget, called from QGLWidget method updateGL.
        All user rendering code should be defined here.
        Args:
            (None)
        Returns:
            (None)
        """
        # Start from a blank slate each render by clearing buffers
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        
        self.ground_graphics.render()
        
        self.origin_axes_graphics.render(np.identity(3), np.zeros(3))

        
    def initGeometry(self):
        """ Initializes any geometry not encapsulated in a class. """

        pass