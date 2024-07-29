from graphics import Window, Point

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.alive = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        #testing 
        #self.alive = True
        if self.alive:
            color = "white" #if self.alive else "black"
            self._win.Draw_square(self._x1, self._y1, self._x2, self._y2, color)