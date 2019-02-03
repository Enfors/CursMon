#!/usr/bin/env python3

"""
CursMon by Christer Enfors © 2019
"""

import csv
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

        with open("input.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

            self.ui.display_graph(data)
            self.ui.refresh()

            while True:
                for row in csv_reader:
                    data.append(row)
                    self.ui.display_graph(data)
                    self.ui.refresh()
                time.sleep(0.1)
            #     line = input_file.readline()
            #     if line:
            #         data.append(int(line))
            #         self.ui.display_graph(data)
            #         self.ui.refresh()
            #     time.sleep(0.1)


def main(scr):
    app().run(scr)

curses.wrapper(main)
