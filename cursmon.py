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

        # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # data.extend(data)
        # data.extend(data)

        # for i in range(0, 10):
        #     self.ui.display_graph(data[i:i+20])
        #     self.ui.refresh()
        #     time.sleep(1)

        data = []

        with open("input.txt", "r") as input_file:
            for line in input_file:
                num = int(line)
                data.append(num)
                self.ui.display_graph(data)
                self.ui.refresh()
                time.sleep(0.2)


def main(scr):
    app().run(scr)

curses.wrapper(main)
