from typing import NoReturn

from logging import basicConfig, INFO, info
basicConfig(level=INFO, format='%(message)s')


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        from models.terrain_model import terrain_model
        self.model = terrain_model

    def run(self, path: str) -> NoReturn:
        """ Saves models to a specific path
         :param path: Path to save files to """
        info(f'Saving model to {path}...')
        self.model.save_to(path, 'Terrain.vox')
