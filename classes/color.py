from typing import NoReturn


class Color:
    _r: int = None
    _g: int = None
    _b: int = None
    _a: int = 255

    def __init__(self, color: tuple[int, int, int] | tuple[int, int, int, int] | str | int):
        """ Class which processes RGB colors
        :param color: (r, g, b) or (r, g, b, a) int tuple or hex-string or int """
        if color is not None:
            self.set_color(color)

    def __str__(self) -> str:
        """ Returns class object string to work with  """
        if self._a == 255:
            return f'#{self.get_hex_rgb()}'
        else:
            return f'#{self.get_hex_rgba()}'

    def __repr__(self) -> str:
        """ Returns class object string for debugging """
        return f"Color({self._r}, {self._g}, {self._b}, {self._a})"

    def set_color(self, color: tuple[int, int, int] | tuple[int, int, int, int] | str | int) -> NoReturn:
        """ Sets the class colors
        :param color: (r, g, b) or (r, g, b, a) int tuple or hex-string or int """
        if isinstance(color, tuple):
            self._set_rgb(color)
        elif isinstance(color, str):
            self._set_hex(color)
        elif isinstance(color, int):
            self._a, self._g, self._b, self._a = color, color, color, 255
        else:
            raise ValueError(f'Color must be int tuple, hex string or int, not {type(color)}')

    def _set_rgb(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> NoReturn:
        """ Private method
         Sets color with RGB/RGBA int tuple"""
        if len(color) == 3:  # if there is no alpha channel
            r, g, b = color
            r, g, b = self.fit(r), self.fit(g), self.fit(b)
            self._r, self._g, self._b, self._a = r, g, b, 255
        elif len(color) == 4:  # if alpha channel is present
            r, g, b, a = color
            r, g, b, a = self.fit(r), self.fit(g), self.fit(b), self.fit(a)
            self._r, self._g, self._b, self._a = r, g, b, a
        else:
            raise ValueError(f'Color must contain 3 or 4 integer values, not {len(color)}')

    def _set_hex(self, color: str) -> NoReturn:
        """ Private method
         Sets color with hex string
         :param color: Hex color string """
        color = color.lstrip('#')
        if len(color) == 1:  # Example: #a
            grayscale = int(color * 2, 16)
            self._r, self._g, self._b, self._a = grayscale, grayscale, grayscale, 255
        elif len(color) == 2:  # Example: #40
            grayscale = int(color, 16)
            self._r, self._g, self._b, self._a = grayscale, grayscale, grayscale, 255
        elif len(color) == 3:  # Example: #0f0
            self._r = int(color[0] * 2, 16)
            self._g = int(color[1] * 2, 16)
            self._b = int(color[2] * 2, 16)
        elif len(color) == 4:  # Example: #c248
            self._r = int(color[0] * 2, 16)
            self._g = int(color[1] * 2, 16)
            self._b = int(color[2] * 2, 16)
            self._a = int(color[3] * 2, 16)
        elif len(color) == 6:  # Example: #ff8800
            self._r = int(color[0:2], 16)
            self._g = int(color[2:4], 16)
            self._b = int(color[4:6], 16)
        elif len(color) == 8:  # Example: #00ffff88
            self._r = int(color[0:2], 16)
            self._g = int(color[2:4], 16)
            self._b = int(color[4:6], 16)
            self._a = int(color[6:8], 16)
        else:
            raise ValueError(f'Invalid hex color string: {color}')

    def set_alpha(self, alpha: int) -> NoReturn:
        """Sets the alpha value of the class
        :param alpha: int value between 0 and 255"""
        self._a = self.fit(alpha)

    def get_rgb(self) -> tuple[int, int, int]:
        """ Returns _a tuple of (_r, _g, _b) color values"""
        return self._r, self._g, self._b

    def get_rgba(self) -> tuple[int, int, int, int]:
        """ Returns _a tuple of (_r, _g, _b, _a) color values"""
        return self._r, self._g, self._b, self._a

    def get_hex_rgb(self) -> str:
        """ Converts red green and blue values to hex string
        :return: Hex color string """
        r, g, b = self.get_rgb()
        return f'{r:02x}{g:02x}{b:02x}'

    def get_hex_rgba(self) -> str:
        """ Converts red green and blue values to hex string with alpha channel
        :return: Hex color string """
        r, g, b, a = self.get_rgba()
        return f'{r:02x}{g:02x}{b:02x}{a:02x}'

    @staticmethod
    def fit(x: int | float) -> int:
        """ Fits color value to [0; 255] interval in case if function got incorrect color parameter
        :return: Returns normalized color value """
        x = int(x)
        return max(0, min(x, 255))

    def blend(self, color: callable, proportion: float = 0.5) -> callable:
        """ Blends two colors with proportions
         :param color: Color object to blend with
         :param proportion: Proportion of the second color to be blended with first"""
        if not (0 <= proportion <= 1):
            raise ValueError(f'Propotion must be float between 0 and 1, not {proportion}')
        else:
            r2, g2, b2, a2 = color.get_rgba()
            r = int(self._r * (1 - proportion)) + int(r2 * proportion)
            g = int(self._g * (1 - proportion)) + int(g2 * proportion)
            b = int(self._b * (1 - proportion)) + int(b2 * proportion)
            a = int(self._a * (1 - proportion)) + int(a2 * proportion)
            return Color((r, g, b, a))

    def invert(self) -> NoReturn:
        """ Makes the color opposite to current """
        self._r = 255 - self._r
        self._g = 255 - self._g
        self._b = 255 - self._b

    def __add__(self, other: callable) -> callable:
        """ Overloads "+" method
        :param other: Color to be added """
        r2, g2, b2, a2 = other.get_rgba()
        r = self.fit(self._r + r2)
        g = self.fit(self._g + g2)
        b = self.fit(self._b + b2)
        a = self.fit(self._a + a2)
        return Color((r, g, b, a))

    def __sub__(self, other: callable) -> callable:
        """ Overloads "-" method
        :param other: Color to be subtracted """
        r2, g2, b2, a2 = other.get_rgba()
        r = self.fit(self._r - r2)
        g = self.fit(self._g - g2)
        b = self.fit(self._b - b2)
        a = self.fit(self._a - a2)
        return Color((r, g, b, a))

    def __mul__(self, other: callable | int | float) -> callable:
        """ Overloads "*" method
        :param other: Color or number to be multiplied """
        if isinstance(other, int) or isinstance(other, float):
            r = self.fit(self._r * other)
            g = self.fit(self._g * other)
            b = self.fit(self._b * other)
            return Color((r, g, b, self._a))
        else:
            r2, g2, b2, a2 = other.get_rgba()
            r = self.fit(self._r * (r2 / 255))
            g = self.fit(self._g * (g2 / 255))
            b = self.fit(self._b * (b2 / 255))
            a = self.fit(self._a * (a2 / 255))
            return Color((r, g, b, a))
