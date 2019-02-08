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
        plot_x_size = self.ui.cols - 7
        plot_x_size -= plot_x_size % 2
        small_plot_x_size = int(plot_x_size / 2 - 3)
        second_graph_column = small_plot_x_size + 6

        with open("input.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                data.append(row)

            main_graph = ui.Graph(scr, "loop_load", top_graph_y=0,
                                  top_graph_x=0, plot_y_size=20,
                                  plot_x_size=plot_x_size, y_step=5,
                                  mv_avg_y=7, show_mv_avg_y=True, bar=True)
            extra_graph = ui.Graph(scr, "loop_load", top_graph_y=23,
                                   top_graph_x=0, plot_y_size=10,
                                   plot_x_size=small_plot_x_size, y_step=10,
                                   show_y=False, show_mv_avg_y=True)
            third_graph = ui.Graph(scr, "loop_load", top_graph_y=23,
                                   top_graph_x=second_graph_column,
                                   plot_y_size=10,
                                   plot_x_size=small_plot_x_size, y_step=10,
                                   bar=True)
            fourth_graph = ui.Graph(scr, "loop_load", top_graph_y=36,
                                    top_graph_x=0, plot_y_size=10,
                                    plot_x_size=small_plot_x_size, y_step=10,
                                    show_mv_avg_y=True)
            fifth_graph = ui.Graph(scr, "loop_load", top_graph_y=36,
                                   top_graph_x=second_graph_column,
                                   plot_y_size=10,
                                   plot_x_size=small_plot_x_size, y_step=10)

            self.ui.add_graph(main_graph)
            self.ui.add_graph(extra_graph)
            self.ui.add_graph(third_graph)
            self.ui.add_graph(fourth_graph)
            self.ui.add_graph(fifth_graph)
            self.ui.refresh(data)

            while True:
                for row in csv_reader:
                    data.append(row)
                    self.ui.refresh(data)
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
