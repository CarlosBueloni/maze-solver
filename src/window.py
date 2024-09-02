from tkinter import Tk, BOTH, Canvas
from line import Line, Point

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
    line1 = Line(Point(2, 3), Point(10, 20))
    line2 = Line(Point(10, 20), Point(100, 200))
    line3 = Line(Point(100, 200), Point(150, 120))
    win = Window(800, 600)
    win.draw_line(line1, "red")
    win.draw_line(line2, "red")
    win.draw_line(line3, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
