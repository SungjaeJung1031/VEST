"""Detection Graphics

Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import sys

import OpenGL.GL as gl                # python wrapping of OpenGL
import OpenGL.GLU as glu

from OpenGL.arrays import vbo       # used to store VBO data
import numpy as np                  # general matrix/array math

import g_config
import enum_g_config
import g_data
import enum_g_data

class GraphicsRoad(object):
    def __init__(self, radius_inner, radius_outer, angle_start_deg, angle_end_deg, angle_step_deg, lat_coord_0, long_coord_0):
        """ Initialize the detection graphics object.
        Initialize the ground graphics object.
        Args:
            radius_inner    (float):  
            radius_outer    (float): 
            angle_start     (float): 
            angle_end       (float): 
            angle_step      (float):
            lat_coord_0     (float):
            long_coord_0    (float):
        """
        self.radius_inner   = radius_inner
        self.radius_outer   = radius_outer
        self.angle_start_rad= angle_start_deg*np.pi/180.0
        self.angle_end_rad  = (angle_end_deg+angle_step_deg)*np.pi/180.0
        self.angle_step_rad = angle_step_deg*np.pi/180.0
        self.lat_coord_0    = lat_coord_0
        self.long_coord_0   = long_coord_0

    def render(self): 

        if (enum_g_config.EnumDispOpt.DISPLAY == g_config.disp_opt_road) and \
            (0 < g_data.frm_len):
            df_ego = g_data.df_dict_log_data[enum_g_data.ListLogDataType.EGO]
            radius = df_ego["vel"][g_data.cur_frm]/df_ego["yawrate"][g_data.cur_frm] * g_config.unit_vector_scale_factor
            if 0.0 < g_config.unit_vector_scale_factor:
                if (0 < df_ego["yawrate"][g_data.cur_frm]):
                    self.radius_outer = (radius + 4.0 * g_config.unit_vector_scale_factor) 
                    self.radius_inner = (radius - 4.0 * g_config.unit_vector_scale_factor) 
                    self.lat_coord_0  = -radius
                    self.long_coord_0 = 0.0
                    self.angle_step_rad = -0.5*np.pi/180.0
                    self.angle_start_rad = 180.0*np.pi/180.0
                    self.angle_end_rad = self.angle_start_rad \
                                        - np.arcsin((400.0* g_config.unit_vector_scale_factor)/self.radius_outer)
                else:
                    self.radius_outer = (radius + 4.0 * g_config.unit_vector_scale_factor)
                    self.radius_inner = (radius - 4.0 * g_config.unit_vector_scale_factor)
                    self.lat_coord_0  = radius
                    self.long_coord_0 = 0.0
                    self.angle_step_rad = 0.5*np.pi/180.0
                    self.angle_start_rad = 0.0
                    self.angle_end_rad = self.angle_start_rad \
                                        + np.arcsin((400.0* g_config.unit_vector_scale_factor)/self.radius_outer)
            else:
                print("ERROR: scale factor of unit vector is invalid")
                exit()

            gl.glBegin(gl.GL_TRIANGLE_STRIP)
            gl.glColor4f(0.4, 0.4, 0.4, 0.0)
            
            for angle_rad in np.arange(self.angle_start_rad, self.angle_end_rad, self.angle_step_rad):
                lat_coord_inner = self.radius_inner * np.cos(angle_rad) + self.lat_coord_0
                long_coord_inner = self.radius_inner * np.sin(angle_rad) + self.long_coord_0
                gl.glVertex3f(lat_coord_inner, long_coord_inner, 0.0001)
        
                lat_coord_outer = self.radius_outer * np.cos(angle_rad) + self.lat_coord_0
                long_coord_outer = self.radius_outer * np.sin(angle_rad) + self.long_coord_0
                gl.glVertex3f(lat_coord_outer, long_coord_outer, 0.0001)

            gl.glEnd()
            gl.glFlush()

