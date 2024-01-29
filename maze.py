from cell import Cell
import random
from time import sleep


class Maze:
    def __init__(
        self,
        x1, y1,
        num_rows, num_cols,
        cell_size_x, cell_size_y,
        win=None,
        seed=None
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells: list[list[Cell]] = []
        for i in range(self._num_cols):
            self._cells.append([Cell(self._win)])
            for j in range(1, self._num_rows):
                self._cells[i].append(Cell(self._win))
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _break_entrance_and_exit(self):
        last_col_idx = len(self._cells) - 1
        last_row_idx = len(self._cells[last_col_idx]) - 1
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[last_col_idx][last_row_idx].has_bottom_wall = False
        self._draw_cell(last_col_idx, last_row_idx)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i != 0:
                if self._cells[i-1][j].visited is False:
                    to_visit.append((i-1, j))
            if j != 0:
                if self._cells[i][j-1].visited is False:
                    to_visit.append((i, j-1))
            if i != len(self._cells) - 1:
                if self._cells[i + 1][j].visited is False:
                    to_visit.append((i+1, j))
            if j != len(self._cells[i]) - 1:
                if self._cells[i][j+1].visited is False:
                    to_visit.append((i, j+1))
            if to_visit == []:
                self._draw_cell(i, j)
                break
            new_i, new_j = to_visit[random.randrange(len(to_visit))]
            if new_i < i:
                self._cells[i][j].has_left_wall = False
            elif new_i > i:
                self._cells[i][j].has_right_wall = False
            elif new_j < j:
                self._cells[i][j].has_top_wall = False
            else:
                self._cells[i][j].has_bottom_wall = False
            self._draw_cell(i, j)
            self._break_walls_r(new_i, new_j)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def _draw_cell(self, i: int, j: int):
        self._cells[i][j].draw(
            self._cell_size_x * i + self._x1,
            self._cell_size_y * j + self._y1,
            self._cell_size_x * (i + 1) + self._x1,
            self._cell_size_y * (j + 1) + self._y1
        )
        if self._win is None:
            return
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.03)

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i, j) -> bool:
        self._animate()
        self._cells[i][j].visited = True

        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            return True

        if j < len(self._cells[i]) - 1 \
                and not self._cells[i][j+1].visited \
                and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            res = self._solve_r(i, j + 1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)

        if i < len(self._cells) - 1 \
                and not self._cells[i+1][j].visited \
                and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            res = self._solve_r(i + 1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)

        if i > 0 \
                and not self._cells[i-1][j].visited \
                and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            res = self._solve_r(i - 1, j)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)

        if j > 0 \
                and not self._cells[i][j-1].visited \
                and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            res = self._solve_r(i, j - 1)
            if res:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)

        return False
