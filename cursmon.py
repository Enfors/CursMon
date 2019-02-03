#!/usr/bin/env python3

"""
CursMon by Christer Enfors © 2019
"""

import curses
import time

import curs_ui as ui


class app(object):
    """
    The application object.
    """

    def run(self, scr):
        self.ui = ui.UI(scr)

        data = []

        with open("input.txt", "r") as input_file:
            for line in input_file:
                num = int(line)
                data.append(num)

            self.ui.display_graph(data)
            self.ui.refresh()

            while True:
                line = input_file.readline()
                if line:
                    data.append(int(line))
                    self.ui.display_graph(data)
                    self.ui.refresh()
                time.sleep(0.1)


def main(scr):
    app().run(scr)

curses.wrapper(main)
