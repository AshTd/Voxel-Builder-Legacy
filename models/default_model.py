from classes.voxel import Voxel
from classes.model import Model

color = Voxel('#ea5')
empty = Voxel()
default_model = Model([[[color, color, color], [color, empty, color], [color, color, color]],
                       [[color, empty, color], [empty, empty, empty], [color, empty, color]],
                       [[color, color, color], [color, empty, color], [color, color, color]]])

"""
The default_model represents a 3D model consisting of a yellow-brown colored cube with empty inner space.
This model is an example how to create simple models with this priject.
"""
