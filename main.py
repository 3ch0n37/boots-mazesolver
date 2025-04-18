from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
    cell = Cell(20, 20, 30, 30, win)
    cell.draw()
    cell_2 = Cell(40, 20, 50, 30, win)
    cell_2.has_right_wall = False
    cell_2.draw()
    cell_3 = Cell(30, 40, 50, 60, win)
    cell_3.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()
