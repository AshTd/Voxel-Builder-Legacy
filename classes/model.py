from typing import Union, NoReturn
import numpy as np
import os
from pathlib import Path

from pyvox.models import Vox
from pyvox.writer import VoxWriter

from classes.voxel import Voxel

from logging import basicConfig, INFO, warning
basicConfig(level=INFO, format='%(message)s')


class Model:
    _x_size = None
    _y_size = None
    _z_size = None
    _palette = None

    def __init__(self, model: Union[list[list[list[Voxel]]], tuple]):
        """ 3D voxel model class
        :param model: list [x, y, z] - voxels """
        if isinstance(model, tuple):
            if len(model) == 3:
                self._x_size, self._y_size, self._z_size = model
                self.model = np.ndarray(shape=(self._x_size, self._y_size, self._z_size), dtype=Voxel)
                self.set_empty_model()
            else:
                raise TypeError(f'Model shape must be int tuple with 3 dimensions, not {len(model)}')
        else:
            self._x_size = len(model[0])
            self._y_size = len(model[1])
            self._z_size = len(model[2])
            self.model = np.ndarray(shape=(self._x_size, self._y_size, self._z_size), dtype=Voxel)
            self.from_list(model)

    def set_empty_model(self) -> NoReturn:
        """ Fills entire model with empty voxels """
        for x, y, z in np.ndindex(*self.model.shape):
            self.model[x, y, z] = Voxel()

    def from_list(self, model: list[list[list[Voxel]]]):
        """ Sets model with 3D list of voxels
         :param model: 3D list of Voxel class objects """
        for x, y, z in np.ndindex(*self.model.shape):
            self.model[x, y, z] = model[x][y][z]

    def create_palette(self) -> list[tuple]:
        """ Creates a palette with maximum of 255 colors from a voxel model """
        unique_colors = set()
        # Search for unique colors in visible voxels
        for plane in self.model:
            for row in plane:
                for voxel in row:
                    if len(unique_colors) < 255 and voxel.is_visible():
                        unique_colors.add(voxel.color.get_rgba())
        self._palette = list(unique_colors)
        # Set voxels that do not fit within the palette invisible
        all_voxels_fit_into_palette = True
        for plane in self.model:
            for row in plane:
                for voxel in row:
                    if voxel.color.get_rgba() not in self._palette and voxel.is_visible():
                        voxel.set_visible(False)
                        all_voxels_fit_into_palette = False
        if not all_voxels_fit_into_palette:
            warning("Some voxels didn't fit into palette, so they are invisible")
        return self._palette

    def __str__(self) -> str:
        """ Returns class object string to work with """
        return str(self.model[0])

    def __repr__(self) -> str:
        """ Returns class object string for debugging """
        return f'Model({self.model})'

    def set_voxel(self, coords: tuple[int, int, int], voxel: type(Voxel)) -> NoReturn:
        """ Sets a specific voxel in specific coordinates
        :param coords: (x, y, z) coordinates tuple
        :param voxel: Voxel object to be set """
        x, y, z = coords
        if 0 <= x < self._x_size and 0 <= y < self._y_size and 0 <= z < self._z_size:
            self.model[x, y, z] = voxel
        else:
            raise ValueError(f'Voxel coordinates are out of model '
                             f'bounds [{self._x_size}, {self._y_size}, {self._z_size}]: ({x}, {y}, {z})')

    def get_voxel(self, coords: tuple[int, int, int]) -> type(Voxel):
        """ Sets a specific voxel in specific coordinates
        :param coords: (x, y, z) coordinates tuple """
        x, y, z = coords
        if 0 <= x < self._x_size and 0 <= y < self._y_size and 0 <= z < self._z_size:
            return self.model[x, y, z]
        else:
            raise ValueError(f'Voxel coordinates are out of model'
                             f'bounds [{self._x_size}, {self._y_size}, {self._z_size}]: ({x}, {y}, {z})')

    def save_to(self, path: Path, file: str) -> NoReturn:
        """ Saves the model into .vox file
        :param path: Save file path 'C:\\RandomDirectory'
        :param file: Save file name 'text.vox' """
        dense = self._to_dense()
        vox = Vox.from_dense(dense)
        vox.palette = self._palette
        if os.path.exists(path):
            if Path(file).suffix == '.vox':
                VoxWriter(f'{path}\\{file}', vox).write()
            else:
                raise NameError(f"File should have '.vox' format: {file}.vox")
        else:
            raise NotADirectoryError(f'Save file path not found: {path}')

    def _to_dense(self) -> np.ndarray:
        """ Converts Model to NumPy array with palette colors IDs """
        self.create_palette()
        # Creating empty array of color IDs
        dense = np.ndarray(shape=(self._y_size, self._z_size, self._x_size), dtype=int)
        # Set colors IDs
        for x, y, z in np.ndindex(*self.model.shape):
            if self.model[x, y, z].color.get_rgba() in self._palette and self.model[x, y, z].is_visible():
                dense[y, (self._z_size - 1 - z), x] = self._palette.index(self.model[x, y, z].color.get_rgba()) + 1
            else:
                # If voxel is invisible, color ID is 0
                dense[y, (self._z_size - 1 - z), x] = 0
        return dense
