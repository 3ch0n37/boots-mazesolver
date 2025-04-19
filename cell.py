from graphics import Line, Point

class Cell:
    def __init__(self, window = None):
        self._win = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        left_color = "black" if self.has_left_wall else "white"
        self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), left_color)
        top_color = "black" if self.has_top_wall else "white"
        self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), top_color)
        right_color = "black" if self.has_right_wall else "white"
        self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), right_color)
        bottom_color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), bottom_color)

    def get_center(self):
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1
        return Point(x_center, y_center)

    def draw_move(self, to_cell, undo=False):
        center_1 = self.get_center()
        center_2 = to_cell.get_center()

        color = "red" if undo else "black"

        self._win.draw_line(Line(center_1, center_2), color)