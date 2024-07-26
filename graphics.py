from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()  # This creates the main window for our application
        self.__root.title("Game of Life")  # This sets the name of the window to "Game of Life"
        self.__canvas = Canvas(self.__root, bg="black", width=width, height=height)  # Creates a canvas within the root window with specified width and height. Cells are white therefore is the bg black.
        self.__canvas.pack(fill=BOTH, expand=1)  # This line ensures the canvas fills the window
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = False  # Initializes the running state of the window

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window closed.")

    def close(self):
        self.__running = False
    
    def start(self):
        self.__running = True

    def Draw_square(self, x1, y1, x2, y2, color="white"):
        self.__canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y