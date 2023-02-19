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
            r, g, b = color[0], color[1], color[2]
            r, g, b = self.fit(r), self.fit(g), self.fit(b)
            self.r, self.g, self.b = r, g, b
        elif len(color) == 4:  # if alpha channel is present
            r, g, b, a = color[0], color[1], color[2], color[3]
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
        r = hex(self.r)[2:].zfill(2)
        g = hex(self.g)[2:].zfill(2)
        b = hex(self.b)[2:].zfill(2)
        return f'{r}{g}{b}'

    def get_hex_rgba(self):
        """ Converts red green and blue values to hex string with alpha channel
        :return: Hex color string """
        r = hex(self.r)[2:].zfill(2)
        g = hex(self.g)[2:].zfill(2)
        b = hex(self.b)[2:].zfill(2)
        a = hex(self.a)[2:].zfill(2)
        return f'{r}{g}{b}{a}'

    @staticmethod
    def fit(x):
        """ Fits color value to [0; 255] interval in case if function got incorrect color parameter
        :return: Normalized color value """
        if x < 0:
            return 0
        elif x > 255:
            return 255
        else:
            return x
