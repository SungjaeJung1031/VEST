import math

import OpenGL.GL as gl              # python wrapping of OpenGL

class FovGraphics(object):
    def __init__(self):
        self.pos_lat = 0.0
        self.pos_long = 0.1

        self.fov_angle_lat = 75.0
        self.fov_angle_vert = 20.0
        self.fov_angle_lat_half = self.fov_angle_lat / 2.0
        self.fov_angle_vert_half = self.fov_angle_vert / 2.0
        self.max_long_scan_dist = 0.6
        self.pos_lat_max_range = self.max_long_scan_dist * math.tan(self.fov_angle_lat_half)
        self.pos_vert_max_range = self.max_long_scan_dist * math.tan(self.fov_angle_vert_half)

        self.pos_lat_fov_left = self.pos_lat - self.pos_lat_max_range
        self.pos_lat_fov_right = self.pos_lat + self.pos_lat_max_range

    def render(self):
        gl.glBegin(gl.GL_LINES)
        gl.glVertex3f(self.pos_lat, self.pos_long, 0.0)
        gl.glVertex3f(self.pos_lat_fov_left, self.max_long_scan_dist,0.0)

        gl.glVertex3f(self.pos_lat, self.pos_long, 0.0)
        gl.glVertex3f(self.pos_lat_fov_right, self.max_long_scan_dist,0.0)

        gl.glVertex3f(self.pos_lat, self.pos_long, 0.0)
        gl.glVertex3f(self.pos_lat_fov_left, self.max_long_scan_dist,self.pos_vert_max_range)

        gl.glVertex3f(self.pos_lat, self.pos_long, 0.0)
        gl.glVertex3f(self.pos_lat_fov_right, self.max_long_scan_dist,self.pos_vert_max_range)

        gl.glEnd()