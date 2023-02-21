import numpy as np
import noise

from classes.model import Model
from classes.voxel import Voxel


size = 48, 48, 48
octaves = 1
freq = 32
noise_model = Model(size)
i = 0
for x, y, z in np.ndindex(size[0], size[1], size[2]):
    # Counting percentage for big models
    # WARNING: Big models need a lot of RAM
    # print(f'{round(i/(size[0]*size[1]*size[2]) * 1000) / 10}%')
    i += 1
    value = noise.snoise3(x / freq, y / freq, z / freq, octaves=octaves)
    if -0.1 <= value <= 0.1:
        noise_model.set_voxel((x, y, z), Voxel(255))

"""
The noise represents a model consisting of a Perlin noise-colored cube.
This model is an example how to create complex models with this priject.
"""
