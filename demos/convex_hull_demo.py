import random
from typing import List, Tuple

from geometric import Point2D as Point
from geometric.convex import display_convex_hull, slow_convex_hull_calculator


def generate_random_points(*, n: int = 10, limits: Tuple[int] = (-100, 100),
                           seed: int = None) -> List[Point]:
    """
    Generates n random points.

    Args:
        n: The point quantity.
        limits: The x and y random limits.
        seed: The random seed.

    Returns:
        A list with random points.
    """
    if seed is not None:
        random.seed(seed)
    return [Point(random.randint(*limits),
                  random.randint(*limits)) for _ in range(n)]


def convex_hull_demo():
    points = generate_random_points(n=50)
    convex_hull_vertices = slow_convex_hull_calculator(points)
    display_convex_hull(points, convex_hull_vertices)


if __name__ == "__main__":
    convex_hull_demo()
