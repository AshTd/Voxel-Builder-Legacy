from classes.color import Color


class Voxel:
    def __init__(self, color):
        """ Voxel class
        :param color: tuple (_r, _g, _b)"""
        self.color = Color(color)

    def __str__(self):
        return self.color.get_hex()

    def set_color(self, color):
        """ Sets voxel color
        :param color: Color object """
        self.color = color
