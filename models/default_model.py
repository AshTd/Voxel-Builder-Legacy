from classes.voxel import Voxel
from classes.model import Model

C = Voxel('#ea5')  # Color
A = Voxel()        # Air
default_model = Model([[[C, C, C], [C, A, C], [C, C, C]],
                       [[C, A, C], [A, A, A], [C, A, C]],
                       [[C, C, C], [C, A, C], [C, C, C]]])
