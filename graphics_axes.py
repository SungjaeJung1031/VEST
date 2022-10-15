
import numpy as np

from graphics_vector import GraphicsVector

class GraphicsAxes(object):
    """
    Class for rendering an axes (frame vectors) object.
    """
    
    def __init__(self):
        self.x_axis = GraphicsVector()
        self.y_axis = GraphicsVector()
        self.z_axis = GraphicsVector()

    def render(self, R, t):
        self.x_axis.render(t, R[:,0],
                           0.3, 0.01, np.array([1.0, 0.0, 0.0]))
        self.y_axis.render(t, R[:,1
        ],
                           0.3, 0.01, np.array([0.0, 1.0, 0.0]))
        self.z_axis.render(t, R[:,2],
                           0.3, 0.01, np.array([0.0, 0.0, 1.0]))