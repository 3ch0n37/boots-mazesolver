from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    line_a = Line(Point(100, 100), Point(200, 200))
    win.draw_line(line_a, "black")
    line_b = Line(Point(100, 200), Point(200, 100))
    win.draw_line(line_b, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()
