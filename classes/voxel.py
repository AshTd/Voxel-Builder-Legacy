from typing import Union, NoReturn

from classes.color import Color


class Voxel:
    def __init__(self,
                 color: Union[type(Color), tuple[int, int, int], tuple[int, int, int, int], str, int] = '#fff'
                 ) -> NoReturn:
        """ Voxel class which represents a voxel
        :param color: Color object, (r, g, b) or (r, g, b, a) int tuple or hex-string or int """
        self.color = None
        self.set_color(color)

    def __str__(self) -> str:
        """ Returns class object string to work with """
        return self.color.__str__()

    def __repr__(self) -> str:
        """ Returns class object string for debugging """
        return f'Voxel({self.color.__repr__()})'

    def set_color(self,
                  color: Union[type(Color), tuple[int, int, int], tuple[int, int, int, int], str, int]
                  ) -> NoReturn:
        """ Sets voxel color
        :param color: Color object, (r, g, b) or (r, g, b, a) int tuple or hex-string or int """
        if isinstance(color, Color):
            self.color = color
        else:
            self.color = Color(color)

    def set_alpha(self, alpha: int) -> NoReturn:
        """ Sets voxel alpha value
        :param alpha: New alpha value """
        self.color.set_alpha(alpha)
