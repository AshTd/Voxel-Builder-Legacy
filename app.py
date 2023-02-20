import numpy as np

from pyvox.models import Vox
from pyvox.writer import VoxWriter

from os.path import expanduser

from classes.color import Color


class VoxelBuilder:
    default_model = np.array([
        [[13, 14, 15], [9,  0, 10], [1, 2, 3]],
        [[16, 0,  17], [0,  0, 0],  [4, 0, 5]],
        [[18, 19, 20], [11, 0, 12], [6, 7, 8]]])
    default_palette = [Color('#000').get_rgba(), Color('#800').get_rgba(), Color('#f00').get_rgba(),
                       Color('#080').get_rgba(), Color('#f80').get_rgba(), Color('#0f0').get_rgba(),
                       Color('#8f0').get_rgba(), Color('#ff0').get_rgba(), Color('#008').get_rgba(),
                       Color('#f08').get_rgba(), Color('#0f8').get_rgba(), Color('#ff8').get_rgba(),
                       Color('#00f').get_rgba(), Color('#80f').get_rgba(), Color('#f0f').get_rgba(),
                       Color('#08f').get_rgba(), Color('#f8f').get_rgba(), Color('#0ff').get_rgba(),
                       Color('#8ff').get_rgba(), Color('#fff').get_rgba()]

    def run(self):
        vox = Vox.from_dense(np.array(self.default_model))
        vox.palette = self.default_palette
        VoxWriter(f'{expanduser("~")}\\Desktop\\test.vox', vox).write()
