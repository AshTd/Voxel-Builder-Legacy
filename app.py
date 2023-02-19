import numpy as np

from pyvox.models import Vox
from pyvox.writer import VoxWriter

from os.path import expanduser

from classes.color import Color


class VoxelBuilder:
    default_model = np.array([
        [[1, 2, 3], [1, 0, 3], [1, 2, 3]],
        [[2, 0, 4], [0, 0, 0], [2, 0, 4]],
        [[3, 4, 5], [3, 0, 5], [3, 4, 5]]])
    default_palette = [Color('#ff0000').get_rgba(),
                       Color('#ff8800').get_rgba(),
                       Color('#ffff00').get_rgba(),
                       Color('#88ff00').get_rgba(),
                       Color('#00ff00').get_rgba(),
                       Color('#00ff88').get_rgba(),
                       Color('#00ffff').get_rgba(),
                       Color('#0088ff').get_rgba(),
                       Color('#0000ff').get_rgba(),
                       Color('#8800ff').get_rgba(),
                       Color('#ff00ff').get_rgba(),
                       Color('#ff0088').get_rgba()]

    def run(self):
        vox = Vox.from_dense(np.array(self.default_model))
        vox.palette = self.default_palette
        VoxWriter(f'{expanduser("~")}\\Desktop\\test.vox', vox).write()
