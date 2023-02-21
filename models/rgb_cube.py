import numpy as np
from classes.model import Model
from classes.voxel import Voxel


size = 6
rgb_cube = Model((size, size, size))
for x, y, z in np.ndindex(size, size, size):
    r = z * (255 // size)
    g = x * (255 // size)
    b = (size - y - 1) * (255 // size)
    rgb_cube.set_voxel((x, y, z), Voxel((r, g, b)))
