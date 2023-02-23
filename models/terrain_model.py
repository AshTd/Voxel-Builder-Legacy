import numpy as np
import noise
from tqdm import tqdm

from classes.model import Model
from classes.voxel import Voxel


size = 256, 256, 96
octaves = 5
freq = 196
sea_level = 32
terrain_model = Model((size[0], size[1], size[2]))
for x, y, z in tqdm(np.ndindex(size[0], size[1], size[2]), ncols=69, ascii=' 123456789#', total=size[0]*size[1]*size[2],
                    bar_format='Processing model: |{bar}| {percentage:3.0f}%'):
    value = noise.snoise2(x / freq, y / freq, octaves=octaves, base=0)
    value = (value + 1) / 2
    if value * size[2] > z:
        if value * size[2] <= sea_level + 2:
            terrain_model.set_voxel((x, y, z), Voxel((108, 108, 86)))  # Sand
        elif value > 0.75:
            terrain_model.set_voxel((x, y, z), Voxel((128, 64, 64)))  # Top red
        elif value > 0.70:
            terrain_model.set_voxel((x, y, z), Voxel((255, 96, 0)))  # Orange
        elif value > 0.65:
            terrain_model.set_voxel((x, y, z), Voxel((128, 64, 64)))  # Bottom red
        elif 0.48 < value < 0.5:
            terrain_model.set_voxel((x, y, z), Voxel((94, 92, 92)))  # Light light gray
        elif 0.45 < value < 0.48:
            terrain_model.set_voxel((x, y, z), Voxel((82, 80, 80)))  # Light gray
        else:
            terrain_model.set_voxel((x, y, z), Voxel((68, 64, 64)))  # Gray
    elif z < sea_level:
        terrain_model.set_voxel((x, y, z), Voxel((153, 175, 255)))  # Water

"""
The terrain_model represents a model consisting of procedurally generated landscape.
This model is an example how to create beautyful scenes with this project.
"""
