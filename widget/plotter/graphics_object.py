"""Detection Graphics

Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
import sys

import OpenGL.GL as gl                # python wrapping of OpenGL
import OpenGL.GLU as glu

from OpenGL.arrays import vbo       # used to store VBO data
import numpy as np                  # general matrix/array math

from value_types.enum_color import EnumColor
from value_types.valtype_object import DataclsObject

import dataclasses

class GraphicsObject(object):
    def __init__(self, datacls_obj:DataclsObject, scale_factor:float, color_code:EnumColor):
        """ Initialize the detection graphics object.
        Initialize the ground graphics object.
        Args:
            pos_lat      (float): lateral position of the detection 
            pos_long     (float): longitudinal position of the detection
            scale_factor (float): rendering scale factor
            color_code   (float): color code for detecion color
        """
        self.datacls_obj = DataclsObject()
        # self.datacls_obj = dataclasses.replace(datacls_obj)
        self.datacls_obj.id = datacls_obj.id
        self.datacls_obj.pos_lat = float(-0.5)
        self.datacls_obj.pos_long = float(0.5)
        self.datacls_obj.pos_vert = float(0.0)
        self.datacls_obj.len = float(1.5)
        self.datacls_obj.width = float(0.5)
        self.datacls_obj.height = float(0.5)
        self.datacls_obj.yawrate = datacls_obj.yawrate
        self.datacls_obj.velocity = datacls_obj.velocity
        self.datacls_obj.accel = datacls_obj.accel
        self.datacls_obj.confid = datacls_obj.confid
        self.datacls_obj.status = datacls_obj.status
        self.datacls_obj.type = datacls_obj.type
        self.datacls_obj.ref_pnt = datacls_obj.ref_pnt
        self.datacls_obj.rdr_pos = datacls_obj.rdr_pos

        self.scale_factor = float(1.0)
        self.color_code = color_code

        self.n_vert = 24 # 24 = 4 (points) * 6 (faces), the number of vertices for cube or cuboid shape object
        self.n_dim = 3 # the number of dimensions

        self.vert = np.zeros((self.n_vert, self.n_dim))
        self.set_verticies()

    def set_verticies(self):
        '''
        vertice plan

         upper face                 bottom face    
             ↑ vehicle direction       width
        a┏━━━━━━━┓b                 e┏━━━━━━━┓f
         ┃       ┃                   ┃       ┃
         ┃	 *   ┃                   ┃   *   ┃ length
         ┃       ┃                   ┃       ┃
        d┗━━━━━━━┛c                 h┗━━━━━━━┛g

        * : (pos_lat, pos_long, pos_vert)
        '''
        scaled_pos_lat = self.datacls_obj.pos_lat * self.scale_factor
        scaled_pos_long = self.datacls_obj.pos_long * self.scale_factor
        scaled_pos_vert = self.datacls_obj.pos_vert * self.scale_factor
        scaled_half_len = self.datacls_obj.len * self.scale_factor/2.0
        scaled_half_width = self.datacls_obj.width * self.scale_factor/2.0
        scaled_height = self.datacls_obj.height * self.scale_factor

        # set vertice a
        vert_a = np.array([scaled_pos_lat - scaled_half_width, \
                        scaled_pos_long + scaled_half_len, \
                        scaled_pos_vert + scaled_height])
        # set vertice b
        vert_b = np.array([scaled_pos_lat + scaled_half_width, \
                        scaled_pos_long + scaled_half_len, \
                        scaled_pos_vert + scaled_height])
        # set vertice c
        vert_c = np.array([scaled_pos_lat + scaled_half_width, \
                        scaled_pos_long - scaled_half_len, \
                        scaled_pos_vert + scaled_height])
        # set vertice d
        vert_d = np.array([scaled_pos_lat - scaled_half_width, \
                        scaled_pos_long - scaled_half_len, \
                        scaled_pos_vert + scaled_height])
        # set vertice e
        vert_e = np.array([scaled_pos_lat - scaled_half_width, \
                        scaled_pos_long + scaled_half_len, \
                        scaled_pos_vert])
        # set vertice f
        vert_f = np.array([scaled_pos_lat + scaled_half_width, \
                        scaled_pos_long + scaled_half_len, \
                        scaled_pos_vert])
        # set vertice g
        vert_g = np.array([scaled_pos_lat + scaled_half_width, \
                        scaled_pos_long - scaled_half_len, \
                        scaled_pos_vert])
        # set vertice h
        vert_h = np.array([scaled_pos_lat - scaled_half_width, \
                        scaled_pos_long - scaled_half_len, \
                        scaled_pos_vert])

        # upper face, abcd
        self.vert[0, :] = vert_a
        self.vert[1, :] = vert_b
        self.vert[2, :] = vert_c
        self.vert[3, :] = vert_d

        # bottom face, efgh
        self.vert[4, :] = vert_e
        self.vert[5, :] = vert_f
        self.vert[6, :] = vert_g
        self.vert[7, :] = vert_h
        
        # front face, aefb
        self.vert[8, :] = vert_a
        self.vert[9, :] = vert_e
        self.vert[10, :] = vert_f
        self.vert[11, :] = vert_b

        # rear face, dhgc
        self.vert[12, :] = vert_d
        self.vert[13, :] = vert_h
        self.vert[14, :] = vert_g
        self.vert[15, :] = vert_c

        # left face, cgea
        self.vert[16, :] = vert_c
        self.vert[17, :] = vert_g
        self.vert[18, :] = vert_e
        self.vert[19, :] = vert_a

        # right face, bfhd
        self.vert[20, :] = vert_b
        self.vert[21, :] = vert_f
        self.vert[22, :] = vert_h
        self.vert[23, :] = vert_d

        self.vert_stride = 12 # number of bytes between successive vertices
        self.vert_vbo = vbo.VBO(np.reshape(self.vert, (1,-1), order='C').astype(np.float32))

    def render(self):
        gl.glPushMatrix()

        try:
            # Bind the vertex data buffer to the VBO all future rendering
            # (or until unbound with 'unbind'):
            self.vert_vbo.bind()

            # Set the vertex pointer for rendering:
            gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
            gl.glVertexPointer(3, gl.GL_FLOAT, self.vert_stride, self.vert_vbo)

            # Set the polygons to have front and back faces and to not be filled:
            gl.glColor4f(1.0, 0.0, 0.0, 0.0)
            gl.glLineWidth(3)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)

            # Render triangle edges using the loaded vertex pointer data:
            gl.glDrawArrays(gl.GL_QUADS, 0, self.n_vert)

            # Set the polygons to have front and back faces and to not be filled:
            gl.glColor3f(0, 0, 0)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)

            # Render triangle faces using the loaded vertex pointer data:
            gl.glDrawArrays(gl.GL_QUADS, 0, self.n_vert)

        except Exception as e:
            print(e)

        finally:
            self.vert_vbo.unbind()
            gl.glDisableClientState(gl.GL_VERTEX_ARRAY)

            gl.glPopMatrix()