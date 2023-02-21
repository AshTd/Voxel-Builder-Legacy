from typing import NoReturn

from logging import basicConfig, INFO, info
basicConfig(level=INFO, format='%(message)s')


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        from models.noise_model import noise_model
        self.model = noise_model

    def run(self, path: str) -> NoReturn:
        """ Saves models to a specific path
         :param path: Path to save files to """
        info(f'Saving model to {path}...')
        self.model.save_to(path, 'Noise.vox')
