from line import Point
from cell import Cell
from time import sleep
class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for i in range(self._num_cols)] for j in range(self._num_rows)]
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        x1 = i * self._cell_size_x + self._x1
        x2 = i * self._cell_size_x + self._x1 + self._cell_size_x
        y1 = j * self._cell_size_y + self._y1
        y2 = j * self._cell_size_y + self._y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(0,0)
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.02)





