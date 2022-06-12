"""Detection Graphics

Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import sys

import OpenGL.GL as gl                # python wrapping of OpenGL
import OpenGL.GLU as glu

from value_types.enum_color import EnumColor



class DetectionGraphics(object):
    def __init__(self, pos_lat:float, pos_long:float, scale_factor:float, color_code:EnumColor):
        """ Initialize the detection graphics object.
        Initialize the ground graphics object.
        Args:
            pos_lat      (float): lateral position of the detection 
            pos_long     (float): longitudinal position of the detection
            scale_factor (float): rendering scale factor
            color_code   (float): color code for detecion color
        """

        self.pos_lat = pos_lat
        self.pos_long = pos_long
        self.scale_factor = scale_factor
        self.color_code = color_code

    def render(self):
        gl.glPushMatrix()
        gl.glTranslatef(0.5, 0.5, 0.5)
        gl.glScalef( 0.5, 0.5, 0.5 )
        gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_LINE )
        gl.glDisable( gl.GL_TEXTURE_2D)
        sphere = glu.gluNewQuadric()
        glu.gluSphere( sphere, 1.0, 24, 24 )
        gl.glEnable( gl.GL_TEXTURE_2D)
        gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_FILL )
        gl.glPopMatrix()