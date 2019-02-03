"""
Curses-based User Interface for CursMon.
"""

import curses

WHITE = 1
RED = 2
BLUE = 3
YELLOW = 4
CYAN = 5
GREEN = 6
MAGENTA = 7


class UI(object):
    """
    The Curses-based User Interface class.
    """

    def __init__(self, scr):
        self.lines = curses.LINES
        self.cols = curses.COLS
        curses.init_pair(WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        self.scr = scr
        self.scr.clear()

        plot_x_size = self.cols - 5 - (self.cols % 5)

        self.main_graph = Graph(self.scr, "loop_load", top_graph_y=0,
                                top_graph_x=0, plot_y_size=20,
                                plot_x_size=plot_x_size, y_step=5)
        self.scr.refresh()

    def refresh(self):
        self.scr.refresh()

    def display_graph(self, data):
        self.main_graph.display(data)

    def wait_for_input_char(self):
        return self.scr.getch()


class Graph(object):
    def __init__(self, scr, title, top_graph_y=0, top_graph_x=0,
                 plot_y_size=10, plot_x_size=10, y_step=1):
        self.title = title
        self.scr = scr
        self.left_margin = 5
        self.top_margin = 1
        self.top_graph_y = top_graph_y
        self.top_graph_x = top_graph_x
        self.top_plot_y = top_graph_y + self.top_margin
        self.top_plot_x = top_graph_x + self.left_margin
        self.plot_y_size = plot_y_size
        self.plot_x_size = plot_x_size
        self.y_step = y_step

        self.plot_win = curses.newwin(plot_y_size, plot_x_size + 1,
                                      self.top_margin, self.left_margin)
        assert curses.has_colors()

    def display(self, data):
        self.draw_title()
        self.draw_y_axis()
        self.draw_x_axis()

        self.plot_win.clear()
        self.draw_grid()
        self.plot_data(data)
        self.plot_win.refresh()

    def draw_title(self):
        x = int(((self.plot_x_size - len(self.title)) / 2) + self.left_margin)

        self.scr.addstr(self.top_graph_y, x, self.title)

        extra_space = x - self.left_margin

        """
        ====[ loopload ]====
        +---++---++---++---+
        x = 6
        """

        if extra_space < 3:
            return

        left = "=" * (extra_space - 2) + "["

        self.scr.addstr(self.top_graph_y, self.left_margin, left,
                        curses.color_pair(MAGENTA))
        right_x = self.plot_x_size - extra_space + self.left_margin

        if (len(self.title) + self.plot_x_size) % 2 == 0:
            rounding = 0
        else:
            rounding = 1
        right = " ]" + "=" * (extra_space - 2 + rounding)

        self.scr.addstr(self.top_graph_y, right_x - rounding,
                        right, curses.color_pair(MAGENTA))

    def plot_data(self, data):

        if len(data) > self.plot_x_size:
            plot_data = data[-self.plot_x_size:]
        else:
            plot_data = data

        for i in range(0, len(plot_data)):
            # self.scr.addstr(21, 0, "      data: %d\n" % (data[i]))
            if plot_data[i] > 0:
                y = int((plot_data[i] + self.y_step / 2) / self.y_step)
            else:
                y = 0

            self.plot(y=y, x=i, char="*", color=GREEN)
            # self.scr.addstr(22, 0, "y: %d, data: %d\n" % (y, data[i]))
            # self.scr.getch()

    def draw_grid(self):
        y = 5

        while y <= self.plot_y_size:
            x = 5

            while x <= self.plot_x_size:
                self.plot(y, x - 1, "+")
                x = x + 5
            y = y + 5

    def draw_y_axis(self):
        for row in range(1, self.plot_y_size + 1):
            y = self.plot_y_size - row + self.top_margin
            x = self.left_margin - 4

            if row == self.plot_y_size:
                char = "^"
            else:
                if row % 5 == 0:
                    char = "+"
                else:
                    char = "|"

            self.scr.addstr(y, x, "%3d" % (row * self.y_step),
                            curses.color_pair(CYAN))
            self.scr.addstr(y, x + 3, "%s" % char,
                            curses.color_pair(MAGENTA))

    def draw_x_axis(self):
        for col in range(0, self.plot_x_size + 1):
            x = col + self.left_margin - 1
            y = self.plot_y_size + self.top_margin

            if col == self.plot_x_size:
                char = ">"
            else:
                if col % 5 == 0:
                    char = "+"
                else:
                    char = "-"

            self.scr.addch(y, x, char, curses.color_pair(MAGENTA))
            # self.scr.addstr(25, 0, "col: %d\n" % col)
            # self.scr.addstr(26, 0, "  x: %d\n" % x)
            # self.scr.getch()

    def plot(self, y: int, x: int, char: str, color: int=0):
        # self.scr.addstr("y: %d, x: %d\n" % (y, x))
        data = y
        y = self.plot_y_size - y

        if y < 0:
            y = 0

        if x < 0:
            x = 0

        if y >= self.plot_y_size:
            y = self.plot_y_size - 1

        if x >= self.plot_x_size:
            x = self.plot_x_size - 1

        self.plot_win.addstr(y, x, char, curses.color_pair(color))
        self.plot_win.refresh()
