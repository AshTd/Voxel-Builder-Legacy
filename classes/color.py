class Color:
    r, g, b, a = 0, 0, 0, 255

    def __init__(self, color):
        """ Class which processes RGB colors
        :param color: int tuple (r, g, b) / (r, g, b, a) """
        self.set_color(color)

    def set_color(self, color):
        """ Sets the class colors
        :param color: int tuple (r, g, b) / (r, g, b, a) """
        if len(color) == 3:  # if there is no alpha channel
            r, g, b = color
            r, g, b = self.fit(r), self.fit(g), self.fit(b)
            self.r, self.g, self.b, self.a = r, g, b, 255
        elif len(color) == 4:  # if alpha channel is present
            r, g, b, a = color
            r, g, b, a = self.fit(r), self.fit(g), self.fit(b), self.fit(a)
            self.r, self.g, self.b, self.a = r, g, b, a

    def get_rgb(self):
        """ Returns a tuple of (r, g, b) color values"""
        return self.r, self.g, self.b

    def get_rgba(self):
        """ Returns a tuple of (r, g, b, a) color values"""
        return self.r, self.g, self.b, self.a

    def get_hex_rgb(self):
        """ Converts red green and blue values to hex string
        :return: Hex color string """
        r, g, b = self.get_rgb()
        return f'{r:02x}{g:02x}{b:02x}'

    def get_hex_rgba(self):
        """ Converts red green and blue values to hex string with alpha channel
        :return: Hex color string """
        r, g, b, a = self.get_rgba()
        return f'{r:02x}{g:02x}{b:02x}{a:02x}'

    @staticmethod
    def fit(x):
        """ Fits color value to [0; 255] interval in case if function got incorrect color parameter
        :return: Normalized color value """
        return max(0, min(255, x))
