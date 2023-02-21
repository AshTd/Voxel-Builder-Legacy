from typing import NoReturn

from models.noise_model import noise_model


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        self.model = noise_model

    def run(self, path: str) -> NoReturn:
        """ Saves models to a specific path
         :param path: Path to save files to """
        self.model.save_to(path, 'Noise.vox')
