"""Detection Graphics

Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import sys

import math

import OpenGL.GL as gl                # python wrapping of OpenGL
import OpenGL.GLU as glu

from value_types.enum_color import EnumColor

import g_data
import enum_g_data
import g_config

class GraphicsDetections(object):
    def __init__(self):
        """ Initialize the detection graphics object.
        Initialize the ground graphics object.
        Args:
            pos_lat      (float): lateral position of the detection 
            pos_long     (float): longitudinal position of the detection
            scale_factor (float): rendering scale factor
            color_code   (float): color code for detecion color
        """
    def render(self):
        if 0 < g_data.frm_len:
            df_dtct = g_data.df_dict_log_data[enum_g_data.ListLogDataType.DTCT]
            for j in range(df_dtct["num_det"][g_data.cur_frm]):
                pos_lat = float()
                pos_long = float()
                poz_horz = float()

                rng_key = "range_" + str(j)
                rng_rate_key = "range_rate_" + str(j)
                azimuth_key = "azimuth_" + str(j)
                elevation_key = "elevation_" + str(j)

                rng = df_dtct[rng_key][g_data.cur_frm]
                rng_rate = df_dtct[rng_rate_key][g_data.cur_frm]
                azimuth = df_dtct[azimuth_key][g_data.cur_frm]
                elevation = df_dtct[elevation_key][g_data.cur_frm]

                scaled_pos_lat = g_config.unit_vector_scale_factor * rng * math.cos(azimuth)
                scaled_pos_long = g_config.unit_vector_scale_factor * rng * math.sin(azimuth)
                scaled_pos_horz = g_config.unit_vector_scale_factor * rng * math.sin(elevation)

                gl.glPushMatrix()
                gl.glTranslatef(scaled_pos_lat, scaled_pos_long, 0.2)
                gl.glScalef( 0.1, 0.1, 0.1 )
                gl.glColor4f(1.0, 0.0, 0.0, 0.0)
                gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_LINE )
                gl.glDisable( gl.GL_TEXTURE_2D)
                sphere = glu.gluNewQuadric()
                glu.gluSphere( sphere, 1.0, 24, 24 )
                gl.glEnable( gl.GL_TEXTURE_2D)
                gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_FILL )
                gl.glPopMatrix()
                gl.glFlush()

        # gl.glPushMatrix()
        # gl.glTranslatef(0.05, 0.05, 0.5)
        # gl.glScalef( 0.5, 0.5, 0.5 )
        # gl.glColor4f(1.0, 0.0, 0.0, 0.0)
        # gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_LINE )
        # gl.glDisable( gl.GL_TEXTURE_2D)
        # sphere = glu.gluNewQuadric()
        # glu.gluSphere( sphere, 1.0, 24, 24 )
        # gl.glEnable( gl.GL_TEXTURE_2D)
        # gl.glPolygonMode( gl.GL_FRONT_AND_BACK,  gl.GL_FILL )
        # gl.glPopMatrix()
        # gl.glFlush()