import numpy as np
from classes.voxel import Voxel


class Model:
    def __init__(self, model_scale):
        """ 3D voxel model class
        :param model_scale: tuple (x, y, z) - model sizes """
        self.model = np.ndarray(shape=model_scale, dtype=Voxel)

    def __str__(self):
        return str(self.model[0])

    def set_voxel(self, coords, voxel):
        """ Sets a specific voxel in specific coordinates
        :param coords: tuple (x, y, z)
        :param voxel: Color object """
        x, y, z = coords[0], coords[1], coords[2]
        self.model[x][y][z] = voxel
