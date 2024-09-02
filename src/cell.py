from line import Line, Point

class Cell():
    def __init__(self,win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.center = None
        self._win = win

    def draw(self, top_left, bottom_right):
        assert type(top_left) is Point, "top_left should be of type Point"
        assert type(bottom_right) is Point, "bottom_right should be of type Point"

        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y
        self.center = Point((self._x2 + self._x1) / 2, (self._y2 + self._y1) / 2)

        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        color = "grey" if undo else "red"
        assert self._x1 is not None
        assert self._x2 is not None
        assert self._y1 is not None
        assert self._y2 is not None
        line = Line(self.center, to_cell.center)
        self._win.draw_line(line, color)

