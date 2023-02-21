from typing import NoReturn

from models.default_model import default_model
from models.rgb_cube import rgb_cube


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        self.model = default_model

    @staticmethod
    def run(path: str) -> NoReturn:
        """ Saves models to a specific path
         :param path: Path to save files to """
        default_model.save_to(path, 'Default Model.vox')
        rgb_cube.save_to(path, 'RGB Cube.vox')
