import OpenGL.GL as gl              # python wrapping of OpenGL

import numpy as np
import OpenGL.arrays.vbo as glvbo       # used to store VBO data

import OpenGL.arrays.ctypesparameters


# import enum_g_config


class GraphicsGround(object):
    """
    This class defines a grid (triangular mesh) representing the ground plane. The render
    function must be called from the main paintGL rendering function.
    """

    def __init__(self, num_grid, grid_scale_factor):
        """ Initialize the ground graphics object.
        Initialize the ground graphics object.
        Args:
            length (float): Length of the ground grid, in meters.
            width (float): Width of the ground grid, in meters.
        Returns:
            (None)
        """
        # Store the grid dimensions and compute number of squares and vertices
        self.num_grid= int(num_grid)
        self.grid_scale_factor = float(grid_scale_factor)

        self.n_sq = self.num_grid * self.num_grid
        self.n_vert = 4 * self.n_sq

        # Define the vertex (x,y,z) values as a grid:
        self.vx = np.linspace(-(self.grid_scale_factor/2)*self.num_grid, (self.grid_scale_factor/2)*self.num_grid, self.num_grid + 1)
        self.vy = np.linspace(-(self.grid_scale_factor/2)*self.num_grid, (self.grid_scale_factor/2)*self.num_grid, self.num_grid + 1)
        self.vz = np.zeros((self.num_grid + 1, self.num_grid + 1))

        self.vert = np.zeros((self.n_vert, 3))

        # Organize the vertices into triangles for storing in a VBO:
        sq_ind = 0
        for i in range(self.num_grid):
            for j in range(self.num_grid):
                self.vert[4 * sq_ind,:] = np.array([self.vx[i], self.vy[j], self.vz[i, j]])
                self.vert[4 * sq_ind + 1,:] = np.array([self.vx[i], self.vy[j+1], self.vz[i, j+1]])
                self.vert[4 * sq_ind + 2,:] = np.array([self.vx[i+1], self.vy[j+1], self.vz[i+1, j+1]])
                self.vert[4 * sq_ind + 3,:] = np.array([self.vx[i+1], self.vy[j], self.vz[i+1, j]])

                sq_ind += 1

        # Pack the triangle vertices into a dedicated VBO:
        self.vert_stride = 12 # number of bytes between successive vertices
        self.vert_vbo = glvbo.VBO(np.reshape(self.vert, (1,-1), order='C').astype(np.float32))

        
    # def render(self, disp_opt):
    def render(self):
        """ Renders the ground plane graphics object.
        Render the ground plane graphics using the geometry defined in the constructor.
        This function must be called from the main paintGL rendering function.
        Args:
            (None)
        Returns:
            (None)
        """
        # if enum_g_config.EnumDispOpt.DISPLAY == disp_opt:
        gl.glPushMatrix()

        try:
            # Bind the vertex data buffer to the VBO all future rendering
            # (or until unbound with 'unbind'):
            self.vert_vbo.bind()

            # Set the vertex pointer for rendering:
            gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
            gl.glVertexPointer(3, gl.GL_FLOAT, self.vert_stride, self.vert_vbo)

            # Set the polygons to have front and back faces and to not be filled:
            gl.glColor4f(0.0, 0.0, 0.0, 0.0)
            gl.glLineWidth(3)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)

            # Render triangle edges using the loaded vertex pointer data:
            gl.glDrawArrays(gl.GL_QUADS, 0, self.n_vert)

            # Set the polygons to have front and back faces and to not be filled:
            gl.glColor3f(1, 1, 1)
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)

            # Render triangle faces using the loaded vertex pointer data:
            gl.glDrawArrays(gl.GL_QUADS, 0, self.n_vert)

        except Exception as e:
            print(e)

        finally:
            self.vert_vbo.unbind()
            gl.glDisableClientState(gl.GL_VERTEX_ARRAY)

            gl.glPopMatrix()