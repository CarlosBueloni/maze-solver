from tkinter import Tk, BOTH, Canvas
from line import Line, Point
from cell import Cell

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white")
        self.canvas.pack()
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(Point(10,20), Point(110, 120))
    win.wait_for_close()

if __name__ == "__main__":
    main()
