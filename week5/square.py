from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name, side):
        # call the constructor of the super class, passing same side for width and height
        super().__init__(name, width=side, height=side)
        self._type = 'Square'
    
    @property
    def side(self):
        return self._width # or self._height because they are the same