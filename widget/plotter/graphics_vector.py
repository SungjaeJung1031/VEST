import OpenGL.GL as gl              # python wrapping of OpenGL
from OpenGL import GLU              # OpenGL Utility Library, extends OpenGL functionality
import numpy as np

class GraphicsVector(object):
    """
    Class for rendering a three-dimensional vector.
    """

    def __init__(self):
        self.quadric = GLU.gluNewQuadric()
        GLU.gluQuadricNormals(self.quadric, GLU.GLU_SMOOTH) #Create Smooth Normals
        GLU.gluQuadricTexture(self.quadric, gl.GL_TRUE) #Create Texture Coords


    # self.x_axis.render(t, R[:,0], 0.3, 0.01, np.array([1.0, 0.0, 0.0]))
    def render(self, start, dir, length, width, color):

        if length > 0.0:
            # Compute the angle-axis rotation require to orient the vector along dir:
            up_vec = np.array([0.0, 0.0, 1.0])
            axis = np.cross(up_vec, dir)
            trip_prod = np.linalg.det(np.dstack((up_vec, dir, axis)))
            if trip_prod > 0:
                angle = np.arccos(np.dot(up_vec, dir))
            else:
                angle = 2*np.pi - np.arccos(np.dot(up_vec, dir))

            # Draw the shaft using a cylinder:
            gl.glPushMatrix()
            gl.glColor3f(*color)
            gl.glTranslatef(*start)
            gl.glRotate((180.0/np.pi)*angle, *axis)
            GLU.gluCylinder(self.quadric, width, width, length, 100, 10)
            gl.glPopMatrix()

            # Draw the head using a cylinder having zero width on top:
            gl.glPushMatrix()
            gl.glColor3f(*color)
            gl.glTranslatef(*start)
            gl.glRotate((180.0/np.pi)*angle, *axis)
            gl.glTranslatef(0.0, 0.0, length)
            GLU.gluCylinder(self.quadric, 2.0*width, 0.0, 0.1*length, 100, 10)
            gl.glPopMatrix()