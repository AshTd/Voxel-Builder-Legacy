import numpy as np

from classes.model import Model
from classes.voxel import Voxel


size = 6
rgb_cube = Model((size, size, size))
for x, y, z in np.ndindex(size, size, size):
    r = x * 255 // (size - 1)
    g = y * 255 // (size - 1)
    b = z * 255 // (size - 1)
    rgb_cube.set_voxel((x, y, z), Voxel((r, g, b)))

"""
The rgb_cube is an RGB 6x6x6 cube consisting of a red, green and blue gradients align x y and z axis.
This model is an example how to create algorithmically generated models with this priject.
"""
