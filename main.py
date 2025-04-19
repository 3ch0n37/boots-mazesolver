from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(100, 100, 300, 300)
    cell_2 = Cell(win)
    cell_2.has_right_wall = False
    cell_2.draw(500, 300, 700, 500)
    cell_3 = Cell(win)
    cell_3.draw(600, 100, 700, 200)
    cell.draw_move(cell_3)
    cell.draw_move(cell_2, True)
    cell_2.draw_move(cell_3)
    win.wait_for_close()

if __name__ == "__main__":
    main()
