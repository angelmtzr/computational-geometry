"""
`ConvexHull` module

This module defines the `ConvexHull` data class, which represents a convex hull of a set of points.
Also, there is a display method provided in order to show the geometry: it uses matplotlib.
"""
from dataclasses import dataclass
from typing import List

import matplotlib.pyplot as plt

from geometric import Point2D
from .convex_hull_calculator import ConvexHullCalculator


@dataclass(slots=True)
class ConvexHull:
    """
    A data class representing a convex hull of a set of points. It also provides a display method that uses matplotlib.

    Attributes:
        points (List[Point2D]): A list of `Point2D` representing the points used to calculate the convex hull.
        vertices (List[Point2D]): A list of `Point2D` representing the vertices of the convex hull.
    """
    points: List[Point2D]
    vertices: List[Point2D]

    def __init__(self, points: List[Point2D], calculator: ConvexHullCalculator) -> None:
        """
        Initializes a `ConvexHull` object.

        Args:
            points (List[Point2D]): A list of `Point2D` representing the points used to calculate the convex hull.
            calculator (ConvexHullCalculator): An object implementing the `ConvexHullCalculator` protocol
            that calculates the convex hull of the given points.
        """
        self.points = points
        self.vertices = calculator.calculate(points)

    def display(self) -> None:
        """
        Displays this `ConvexHull` using matplotlib.
        """

        _, ax = plt.subplots()

        plt.style.use('seaborn')
        plt.title('CONVEX HULL')

        x, y = zip(*self.points)
        ax.scatter(x, y, c="blue", label="Points")

        x, y = zip(*self.vertices)
        ax.scatter(x, y, c="green", label="Convex Hull Vertices")

        # We need to add the first vertex at the end to close the convex hull
        vertices = self.vertices.copy()
        vertices.append(vertices[0])

        x, y = zip(*vertices)
        ax.plot(x, y, c="red", label="Convex Hull Edges")

        ax.legend(loc="lower left", bbox_to_anchor=(0.6, -0.37))
        plt.subplots_adjust(bottom=0.25)
        plt.show()
