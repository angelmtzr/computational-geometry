"""
`Point3D` module

This module defines the `Point3D` frozen data class, which represents a point in three-dimensional space.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Point3D:
    """A frozen data class representing a 3D point with x, y, and z coordinates.

    Attributes:
        x (float): The x coordinate of the point.
        y (float): The y coordinate of the point.
        z (float): The z coordinate of the point.

    Example:
        >>> from geometric import Point3D
        >>> p = Point3D(1, 2, 3)
        >>> p.x
        1
        >>> p.y
        2
        >>> p.z
        3
        >>> p1 = Point3D(1, 2, 3)
        >>> p2 = Point3D(4, 5, 6)
        >>> distance = p1.distance_to(p2)
        >>> print(distance)
        5.196152422706632
    """
    x: float
    y: float
    z: float

    def __repr__(self):
        """
        Returns a string representation of the `Point3D` object in the format (x, y, z).

        Returns:
            str: A string representation of the `Point3D` object.
        """
        return f"({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        """
        Returns an iterator for the coordinates of the `Point3D`.

        Yields:
            float: The next coordinate value.
        """
        yield self.x
        yield self.y
        yield self.z

    def __eq__(self, q: Point3D):
        """
        Checks for the equality between this `Point3D` and another `Point3D`.

        Args:
            q (Point3D): The point to compare this point with.

        Raises:
            ArithmeticError: If the dimensions of the points are different.

        Returns:
            bool: The result of the equality check.
        """
        if not isinstance(q, Point3D):
            raise ArithmeticError("Points with different dimensions cannot be compared.")
        from geometric import epsilon
        p = self
        return all((abs(x1 - x2) < epsilon
                    for x1, x2 in zip([p.x, p.y, p.z], [q.x, q.y, p.z])))

    def distance_to(self, q: Point3D) -> float:
        """
        Calculates the distance between this `Point3D` and another `Point3D`.

        Args:
            q (Point3D): The other `Point3D`.

        Returns:
            float: The distance between both points.
        """
        p = self
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2 + (q.z - p.z) ** 2)
