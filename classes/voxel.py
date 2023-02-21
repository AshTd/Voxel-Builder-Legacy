from typing import Union, NoReturn

from classes.color import Color


class Voxel:
    def __init__(self,
                 color: Union[type(Color), tuple[int, int, int], tuple[int, int, int, int], str, int] = None
                 ) -> NoReturn:
        """ Voxel class which represents a voxel
        :param color: Color object, (r, g, b) or (r, g, b, a) int tuple or hex-string or int """
        self.color = None
        self._visible = None
        if color is None:  # If color is unset, voxel is invisible
            self.set_color('#fff')
            self.set_visible(False)
        else:  # If color is present, voxel is visible
            self.set_color(color)
            self.set_visible(True)

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

    def set_visible(self, visibility: bool) -> NoReturn:
        """ Makes the voxel _visible or hidden
         :param visibility: Boolean, shows the state to set voxel to """
        if visibility:
            self._visible = True
        else:
            self._visible = False

    def is_visible(self) -> bool:
        """ Shows the voxel visibility """
        return self._visible

    def set_alpha(self, alpha: int) -> NoReturn:
        """ Sets voxel alpha value
        :param alpha: New alpha value """
        self.color.set_alpha(alpha)
