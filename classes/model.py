from typing import Union, NoReturn
import numpy as np

from classes.voxel import Voxel


class Model:
    _x_size = None
    _y_size = None
    _z_size = None

    def __init__(self, model: list) -> NoReturn:
        """ 3D voxel model class
        :param model: list [x, y, z] - voxels """
        self._x_size = len(model[0])
        self._y_size = len(model[1])
        self._z_size = len(model[2])
        self.model = np.ndarray(shape=(self._x_size, self._z_size, self._z_size), dtype=Voxel)
        self._init_model()

    def _init_model(self) -> NoReturn:
        """ Fills entire model with empty voxels """

    def __str__(self) -> str:
        """ Returns class object string to work with """
        return str(self.model[0])

    def __repr__(self) -> str:
        """ Returns class object string for debugging """
        return f'Model({self.model})'

    def set_voxel(self, coords: tuple[int, int, int], voxel: type(Voxel)) -> NoReturn:
        """ Sets _a specific voxel in specific coordinates
        :param coords: (x, y, z) coordinates tuple
        :param voxel: Voxel object to be set """
        x, y, z = coords[0], coords[1], coords[2]
        self.model[x][y][z] = voxel
