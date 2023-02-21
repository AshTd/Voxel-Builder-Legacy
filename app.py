from typing import NoReturn

from os.path import expanduser

from models.default_model import default_model
from models.rgb_cube import rgb_cube


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        self.model = default_model

    @staticmethod
    def run() -> NoReturn:
        default_model.save_to(f'{expanduser("~")}\\Desktop', 'Default Model.vox')
        rgb_cube.save_to(f'{expanduser("~")}\\Desktop', 'RGB Cube.vox')
