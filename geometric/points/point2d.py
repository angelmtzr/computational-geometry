"""
`Point2D` module

This module defines the `Point2D` frozen data class, which represents a point in two-dimensional space.
"""
from __future__ import annotations

import math
from typing import NamedTuple, TYPE_CHECKING

if TYPE_CHECKING:
    from geometric import Line


class Point2D(NamedTuple):
    """A frozen data class representing a 2D point with x and y coordinates.

    Attributes:
        x: The x coordinate of the point.
        y: The y coordinate of the point.

    Example:
        >>> from geometric import Point2D as Point
        >>> p = Point(1.0, 2.0)
        >>> p.x
        1.0
        >>> p.y
        2.0
        >>> p1 = Point(0, 0)
        >>> p2 = Point(3, 4)
        >>> p1.distance_to(p2)
        5.0
    """
    x: float
    y: float

    def __repr__(self) -> str:
        """
        Returns a string representation of this `Point2D` object in the format "(x, y)".

        Returns:
            The string.
        """
        return f"({self.x}, {self.y})"

    def __eq__(self, q: Point2D) -> bool:
        from geometric import epsilon
        p = self
        return all((abs(x1 - x2) < epsilon
                    for x1, x2 in zip((p.x, p.y), (q.x, q.y))))

    def distance_to(self, q: Point2D) -> float:
        """
        Calculates the distance between this `Point2D` and another `Point2D`.

        Args:
            q: The other `Point2D`.

        Returns:
            The distance between both points.
        """
        p = self
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

    def is_left_of_line(self, line: Line) -> bool:
        """
        Checks if this `Point2D` is to the left of a `Line`.

        Args:
            line: The line.

        Returns:
            `True` if point is to the left of the line, `False` otherwise.
        """
        r = self
        p = line.p1
        q = line.p2
        # Calculate the vectors
        pq = Point2D(q.x - p.x, q.y - p.y)
        pr = Point2D(r.x - p.x, r.y - p.y)

        # Calculate the cross product of pq and pr
        cross_product = pq.x * pr.y - pq.y * pr.x

        # If the cross product is positive, r is to the left of pq
        return cross_product > 0
