from line import Point
from cell import Cell
from time import sleep
import random

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
            seed=None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = i * self._cell_size_x + self._x1
        x2 = i * self._cell_size_x + self._x1 + self._cell_size_x
        y1 = j * self._cell_size_y + self._y1
        y2 = j * self._cell_size_y + self._y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2))
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(0,0)
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i-1 >= 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append([i-1, j])
            if i+1 < self._num_cols:
                if not self._cells[i+1][j].visited:
                    to_visit.append([i+1, j])
            if j-1 >= 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append([i, j-1])
            if j+1 < self._num_rows:
                if not self._cells[i][j+1].visited:
                    to_visit.append([i, j+1])
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return 
            dir = to_visit[random.randrange(0, len(to_visit))]
            if dir[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[dir[0]][dir[1]].has_right_wall = False
            elif dir[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[dir[0]][dir[1]].has_left_wall = False
            elif dir[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[dir[0]][dir[1]].has_bottom_wall = False
            elif dir[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[dir[0]][dir[1]].has_top_wall = False
            self._break_walls_r(dir[0],dir[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                    self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        self._animate()
        current_cell.visited = True
        if j == self._num_rows - 1 and i == self._num_cols - 1:
            return True
        if i - 1 >=0:
            next_cell = self._cells[i-1][j]
            if not next_cell.visited and not next_cell.has_right_wall and not current_cell.has_left_wall:
                current_cell.draw_move(next_cell)
                if self._solve_r(i-1, j):
                    return True
                current_cell.draw_move(next_cell, True)
        if i + 1 < self._num_cols:
            next_cell = self._cells[i+1][j]
            if not next_cell.visited and not next_cell.has_left_wall and not current_cell.has_right_wall:
                current_cell.draw_move(next_cell)
                if self._solve_r(i+1, j):
                    return True
                current_cell.draw_move(next_cell, True)
        if j - 1 >=0:
            next_cell = self._cells[i][j-1]
            if not next_cell.visited and not next_cell.has_bottom_wall and not current_cell.has_top_wall:
                current_cell.draw_move(next_cell)
                if self._solve_r(i, j-1):
                    return True
                current_cell.draw_move(next_cell, True)
        if j + 1 < self._num_rows:
            next_cell = self._cells[i][j+1]
            if not next_cell.visited and not next_cell.has_top_wall and not current_cell.has_bottom_wall:
                current_cell.draw_move(next_cell)
                if self._solve_r(i, j+1):
                    return True
                current_cell.draw_move(next_cell, True)

        return False


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.02)





