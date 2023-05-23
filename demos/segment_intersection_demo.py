import random
from typing import Tuple, List

from geometric import Point2D as Point, Segment
from geometric.intersection import brute_force_segment_intersection, display_segment_intersections


def generate_random_segments(*, n: int = 10, limits: Tuple[int] = (0, 100),
                             seed: int = None) -> List[Segment]:
    """
    Generates a list with n random line segments.

    Args:
        n: The line segments quantity.
        limits: The x and y random limits.
        seed: The random seed.

    Returns:
        The list with the line segments.
    """
    if seed is not None:
        random.seed(seed)
    return [Segment(p1=Point(random.randint(*limits), random.randint(*limits)),
                    p2=Point(random.randint(*limits), random.randint(*limits)))
            for _ in range(n)]


def segment_intersection_demo():
    segments = generate_random_segments(n=20)
    intersections = brute_force_segment_intersection(segments)
    display_segment_intersections(segments, intersections)


if __name__ == '__main__':
    segment_intersection_demo()
