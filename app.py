import numpy as np

from os.path import expanduser

from classes.color import Color
from classes.model import Model
from classes.voxel import Voxel


class VoxelBuilder:
    default_model = np.array([
        [[13, 14, 15], [9,  0, 10], [1, 2, 3]],
        [[16, 0,  17], [0,  0, 0],  [4, 0, 5]],
        [[18, 19, 20], [11, 0, 12], [6, 7, 8]]])
    colors = np.array([
        [[Voxel('#00f'), Voxel('#80f'), Voxel('#f0f')], [Voxel('#008'), Voxel(), Voxel('#f08')],  [Voxel('#000'), Voxel('#800'), Voxel('#f00')]],
        [[Voxel('#08f'), Voxel(),       Voxel('#f8f')], [Voxel(),       Voxel(), Voxel()],        [Voxel('#080'), Voxel(),       Voxel('#f80')]],
        [[Voxel('#0ff'), Voxel('#8ff'), Voxel('#fff')], [Voxel('#0f8'), Voxel(), Voxel('#ff8')],  [Voxel('#0f0'), Voxel('#8f0'), Voxel('#ff0')]]])
    default_palette = [Color('#000').get_rgba(), Color('#800').get_rgba(), Color('#f00').get_rgba(),
                       Color('#080').get_rgba(), Color('#f80').get_rgba(), Color('#0f0').get_rgba(),
                       Color('#8f0').get_rgba(), Color('#ff0').get_rgba(), Color('#008').get_rgba(),
                       Color('#f08').get_rgba(), Color('#0f8').get_rgba(), Color('#ff8').get_rgba(),
                       Color('#00f').get_rgba(), Color('#80f').get_rgba(), Color('#f0f').get_rgba(),
                       Color('#08f').get_rgba(), Color('#f8f').get_rgba(), Color('#0ff').get_rgba(),
                       Color('#8ff').get_rgba(), Color('#fff').get_rgba()]

    def run(self):
        model = [[[voxel for voxel in row] for row in plane] for plane in self.colors]
        m = Model(model)
        m.save_to(f'{expanduser("~")}\\Desktop', 'test.vox')
