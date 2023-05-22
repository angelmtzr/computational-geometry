import pytest

import geometric
from geometric import Point2D


@pytest.mark.parametrize("p, q, epsilon, expected", [
    (Point2D(2, 1), Point2D(2, 1.000001), 1e-4, True),
    (Point2D(2, 1), Point2D(2, 1.000001), 1e-10, False),
    (Point2D(2, 1), Point2D(2, 1.001), 1e-4, False),
    (Point2D(2, 1), Point2D(2, 1.001), 1e-10, False),
    (Point2D(2, 3), Point2D(1.9999999, 3.0000001), 1e-4, True),
    (Point2D(2, 3), Point2D(1.9999999, 3.0000001), 1e-10, False),
    (Point2D(2, 3), Point2D(1.999, 3.001), 1e-4, False),
    (Point2D(2, 3), Point2D(1.999, 3.001), 1e-10, False)
])
def test_epsilon_precision(p: Point2D, q: Point2D, epsilon: float, expected: bool) -> None:
    geometric.epsilon = epsilon
    assert (p == q) == expected


@pytest.mark.parametrize("p, q, expected", [
    (Point2D(1, 2), Point2D(4, 6), 5),
    (Point2D(0, 0), Point2D(0, 0), 0),
    (Point2D(3, 4), Point2D(0, 0), 5)
])
def test_point2d_distance(p: Point2D, q: Point2D, expected: float) -> None:
    assert p.distance_to(q) == expected


if __name__ == "__main__":
    pytest.main()
