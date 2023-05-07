import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List
from geometric import Point
from .convex_hull_calculator import ConvexHullCalculator


@dataclass(slots=True)
class ConvexHull:
    points: List[Point]
    vertices: List[Point]

    def __init__(self, points: List[Point], calculator: ConvexHullCalculator):
        self.points = points
        self.vertices = calculator.calculate(points)

    def display(self):
        """Displays the convex hull using matplotlib."""
        x, y = zip(*self.points)
        plt.scatter(x, y)  # Draws the points
        vertices = self.vertices.copy()
        vertices.append(vertices[0])  # We need to add the first vertex at the end to close the convex hull
        x, y = zip(*vertices)
        plt.plot(x, y, c="orange")  # Draws the edges
        plt.show()
