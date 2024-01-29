import unittest
from maze import Maze
from cell import Cell
from graphics import Window


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_position_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        for i, column in enumerate(m1._cells):
            for j, cell in enumerate(column):
                test_cell = Cell(Window(800, 600))
                test_cell._x1 = m1._cell_size_x * i + m1._x1
                test_cell._y1 = m1._cell_size_y * j + m1._y1
                test_cell._x2 = m1._cell_size_x * (i + 1) + m1._x1
                test_cell._y2 = m1._cell_size_y * (j + 1) + m1._y1
                self.assertEqual(test_cell._x1, cell._x1)
                self.assertEqual(test_cell._y1, cell._y1)
                self.assertEqual(test_cell._x2, cell._x2)
                self.assertEqual(test_cell._y2, cell._y2)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                self.assertEqual(
                    m1._cells[i][j].visited,
                    False
                )


if __name__ == "__main__":
    unittest.main()
