import random
from typing import List

from geometric import ConvexHull, SlowConvexHullCalculator
from geometric import Point2D


def generate_random_points(*, n: int = 10, lower_limit: int = -100,
                           upper_limit: int = 100, seed: int = None) -> List[Point2D]:
    """Returns a list with n random Points."""
    if seed is not None:
        random.seed(seed)
    return [Point2D(random.randint(lower_limit, upper_limit),
                    random.randint(lower_limit, upper_limit)) for _ in range(n)]


def convex_hull_demo():
    points = generate_random_points(n=50)
    convex_hull = ConvexHull(points, SlowConvexHullCalculator())
    convex_hull.display()


if __name__ == "__main__":
    convex_hull_demo()
