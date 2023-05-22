"""
`convex_hull` module

This module defines a simple function to display a convex hull using matplotlib.
"""
from typing import List

import matplotlib.pyplot as plt

from geometric import Point2D as Point


def display_convex_hull(points: List[Point], convex_hull_vertices: List[Point]) -> None:
    """
    Displays the given points and its convex hull defined by the given vertices,
    using matplotlib.
    
    Args:
        points: The points.
        convex_hull_vertices: The convex hull vertices.
    """
    _, ax = plt.subplots()

    plt.style.use('seaborn')
    plt.title('CONVEX HULL')

    x, y = zip(*points)
    ax.scatter(x, y, c="blue", label="Points")

    x, y = zip(*convex_hull_vertices)
    ax.scatter(x, y, c="green", label="Convex Hull Vertices")

    # We need to add the first vertex at the end to close the convex hull
    convex_hull_vertices = convex_hull_vertices.copy()
    convex_hull_vertices.append(convex_hull_vertices[0])

    x, y = zip(*convex_hull_vertices)
    ax.plot(x, y, c="red", label="Convex Hull Edges")

    ax.legend(loc="lower left", bbox_to_anchor=(0.6, -0.37))
    plt.subplots_adjust(bottom=0.25)
    plt.show()
