import numpy as np

from pyvox.models import Vox
from pyvox.writer import VoxWriter

from os.path import expanduser


class VoxelBuilder:
    def __init__(self):
        """ Main app class """
        self.model = [[
                [1, 2, 3],
                [1, 0, 3],
                [1, 2, 3]],
            [
                [2, 0, 4],
                [0, 0, 0],
                [2, 0, 4]],
            [
                [3, 4, 5],
                [3, 0, 5],
                [3, 4, 5]]]

    def run(self):
        vox = Vox.from_dense(np.array(self.model))
        VoxWriter(f'{expanduser("~")}\\Desktop\\test.vox', vox).write()
