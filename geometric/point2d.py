"""
`Point2D` module

This module defines the `Point2D` frozen data class, which represents a point in two-dimensional space.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterator


@dataclass(slots=True, frozen=True)
class Point2D:
    """A frozen data class representing a 2D point with x and y coordinates.

    Attributes:
        x (float): The x coordinate of the point.
        y (float): The y coordinate of the point.

    Example:
        >>> from geometric import Point2D
        >>> p = Point2D(1.0, 2.0)
        >>> p.x
        1.0
        >>> p.y
        2.0
        >>> p1 = Point2D(0, 0)
        >>> p2 = Point2D(3, 4)
        >>> distance = p1.distance_to(p2)
        >>> print(distance)
        5.0
    """
    x: float
    y: float

    def __repr__(self) -> str:
        """
        Returns a string representation of the `Point2D` object in the format (x, y).

        Returns:
            str: A string representation of the `Point2D` object.
        """
        return f"({self.x}, {self.y})"

    def __iter__(self) -> Iterator[float]:
        """
        Returns an iterator for the coordinates of the `Point2D`.

        Yields:
            float: The next coordinate value.
        """
        yield self.x
        yield self.y

    def __eq__(self, q: Point2D) -> bool:
        """
        Checks for the equality between this `Point2D` and another `Point2D`.

        Args:
            q (Point2D): The point to compare this point with.

        Raises:
            ArithmeticError: If the dimensions of the points are different.

        Returns:
            bool: The result of the equality check.
        """
        if not isinstance(q, Point2D):
            raise ArithmeticError("Points with different dimensions cannot be compared.")

        from geometric import epsilon

        p = self
        return all((abs(x1 - x2) < epsilon
                    for x1, x2 in zip((p.x, p.y), (q.x, q.y))))

    def distance_to(self, q: Point2D) -> float:
        """
        Calculates the distance between this `Point2D` and another `Point2D`.

        Args:
            q (Point2D): The other `Point2D`.

        Returns:
            float: The distance between both points.
        """
        p = self
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

    def is_left_of_line(self, p: Point2D, q: Point2D) -> bool:
        """
        Checks if this `Point2D` is to the left of a line in the plane defined by two `Point2D`.

        Args:
            p (Point2D): The first `Point2D` that defines the line.
            q (Point2D): The second `Point2D` that defines the line.

        Returns:
            bool: The result of the point to line comparison.
        """
        r = self

        # Calculate the vectors
        pq = Point2D(q.x - p.x, q.y - p.y)
        pr = Point2D(r.x - p.x, r.y - p.y)

        # Calculate the cross product of pq and pr
        cross_product = pq.x * pr.y - pq.y * pr.x

        # If the cross product is positive, r is to the left of pq
        return cross_product > 0
