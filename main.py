import random
from typing import List
from geometric import Point
from geometric.convex import ConvexHull, SlowConvexHullCalculator


def generate_random_points(*, n: int = 10, lower_limit: int = -100,
                           upper_limit: int = 100, seed: int = None) -> List[Point]:
    """Returns a list with n random Points."""
    if seed is not None:
        random.seed(seed)
    return [Point(random.randint(lower_limit, upper_limit),
                  random.randint(lower_limit, upper_limit)) for _ in range(n)]


def main():
    points = generate_random_points(n=50)
    convex_hull = ConvexHull(points, SlowConvexHullCalculator())
    convex_hull.display()


if __name__ == "__main__":
    main()
