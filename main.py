#!/usr/bin/env python

"""Convex hull algorithm demo"""

from random import randint, seed
from point import Point
from slow_convex_hull_calculator import SlowConvexHullCalculator
from matplotlib_plot import MatplotlibPlot
from convex_hull import ConvexHull


def main():
    seed(50771708)
    points = [Point(randint(-100, 100), randint(-100, 100)) for _ in range(300)]
    plot = MatplotlibPlot()
    plot.insert_convex_hull(points, ConvexHull(points, SlowConvexHullCalculator()))
    plot.show()


if __name__ == "__main__":
    main()
