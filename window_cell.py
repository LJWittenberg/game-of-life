from graphics import Window, Point

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self._p1 = Point(x1, y1)
        self._p2 = Point(x2, y2)
        self._win = win
        self.alive = False

    def draw(self):
        if self._win is None:
            return
        #testing 
        self.alive = True
        color = "white" if self.alive else "black"
        self._win.Draw_square(self._p1.x, self._p1.y, self._p2.x, self._p2.y, color)