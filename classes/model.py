from typing import Union, NoReturn
import numpy as np

from classes.voxel import Voxel


class Model:
    _x_size = None
    _y_size = None
    _z_size = None
    _palette = None

    def __init__(self, model: Union[list[list[list[Voxel]]], tuple]):
        """ 3D voxel model class
        :param model: list [x, y, z] - voxels """
        self._x_size = len(model[0])
        self._y_size = len(model[1])
        self._z_size = len(model[2])
        self.model = np.ndarray(shape=(self._x_size, self._z_size, self._z_size), dtype=Voxel)
        if isinstance(model, tuple):
            if len(model) == 3:
                self._x_size, self._y_size, self._z_size = model
                self.set_empty_model()
            else:
                raise TypeError(f'Model dimensions must be int tuple with 3 dimensions, not {len(model)}')
        else:
            self.from_list(model)
            self.create_palette()

    def set_empty_model(self) -> NoReturn:
        """ Fills entire model with empty voxels """
        for x, y, z in np.ndindex(*self.model.shape):
            self.model[x][y][z] = Voxel()

    def from_list(self, model: list[list[list[Voxel]]]):
        """ Sets model with 3D list of voxels
         :param model: 3D list of Voxel class objects """
        for x, y, z in np.ndindex(*self.model.shape):
            self.model[x][y][z] = model[x][y][z]

    def create_palette(self) -> list[tuple]:
        """ Creates a palette with maximum of 255 colors from a voxel model """
        unique_colors = set()
        # Search for unique colors in visible voxels
        for plane in self.model:
            for row in plane:
                for voxel in row:
                    if len(unique_colors) <= 255 and voxel.is_visible():
                        unique_colors.add(voxel.color.get_rgba())
        self._palette = []
        # Set color of voxels that do not fit within the palette invisible
        for plane in self.model:
            for row in plane:
                for voxel in row:
                    if voxel.color.get_rgba() not in self._palette:
                        voxel.set_visible(False)
        return self._palette

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
        x, y, z = coords
        if 0 <= x < self._x_size and 0 <= y < self._y_size and 0 <= z < self._z_size:
            self.model[x][y][z] = voxel
        else:
            raise ValueError(f'Voxel coordinates are out of model'
                             f'bounds [{self._x_size}, {self._y_size}, {self._z_size}]: ({x}, {y}, {z})')

    def get_voxel(self, coords: tuple[int, int, int]) -> type(Voxel):
        """ Sets _a specific voxel in specific coordinates
        :param coords: (x, y, z) coordinates tuple """
        x, y, z = coords
        if 0 <= x < self._x_size and 0 <= y < self._y_size and 0 <= z < self._z_size:
            return self.model[x][y][z]
        else:
            raise ValueError(f'Voxel coordinates are out of model'
                             f'bounds [{self._x_size}, {self._y_size}, {self._z_size}]: ({x}, {y}, {z})')
