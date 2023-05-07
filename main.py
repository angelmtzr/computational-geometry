import random
import matplotlib.pyplot as plt
from typing import List
from geometric import Point
from geometric.convex import ConvexHullCalculator, ConvexHull, SlowConvexHullCalculator


def generate_random_points(*, n: int = 10, lower_limit: int = -100,
                           upper_limit: int = 100, seed: int = None) -> List[Point]:
    """Returns a list with n random Points."""
    if seed is not None:
        random.seed(seed)
    return [Point(random.randint(lower_limit, upper_limit),
                  random.randint(lower_limit, upper_limit)) for _ in range(n)]


def display_convex_hull(convex_hull: ConvexHull) -> None:
    """Displays a convex hull."""
    x, y = zip(*convex_hull.points)
    plt.scatter(x, y)
    vertices = convex_hull.vertices.copy()
    vertices.append(vertices[0])  # We need to add the first vertex at the end to close the convex hull
    x, y = zip(*vertices)
    plt.plot(x, y, c="orange")  # Draws the edges
    plt.show()


def calculate_convex_hull(points: List[Point], calculator: ConvexHullCalculator) -> ConvexHull:
    return ConvexHull(points, calculator.calculate(points))


def main():
    points = generate_random_points(seed=50771708)
    convex_hull = calculate_convex_hull(points, SlowConvexHullCalculator())
    display_convex_hull(convex_hull)


if __name__ == "__main__":
    main()
