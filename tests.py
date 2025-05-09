import unittest
from maze import Maze
from graphics import Window

class Test(unittest.TestCase):
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

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_generation(self):
        num_cols = 8
        num_rows = 6
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        visited_cells = sum(
            cell.visited for col in maze._cells for cell in col
        )
        self.assertEqual(visited_cells, 0)

    def test_reset_visited_cells(self):
        num_cols = 10
        num_rows = 10
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in maze._cells:
            for cell in col:
                cell.visited = True
        maze._reset_cell_visited()
        for col in maze._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
