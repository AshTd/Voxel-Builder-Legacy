import numpy as np
import noise
from tqdm import tqdm

from classes.model import Model
from classes.voxel import Voxel


size = 128
octaves = 1
freq = 48
noise_model = Model((size, size, size))
for x, y, z in tqdm(np.ndindex(size, size, size), ncols=69, ascii=' 123456789#', total=size**3,
                    bar_format='Processing model: |{bar}| {percentage:3.0f}%'):
    value = noise.snoise3(x / freq, y / freq, z / freq, octaves=octaves)
    if -0.1 <= value <= 0.1:
        noise_model.set_voxel((x, y, z), Voxel(255))

"""
The noise represents a model consisting of a Perlin noise cube.
This model is an example how to create complex models with this priject.
"""
