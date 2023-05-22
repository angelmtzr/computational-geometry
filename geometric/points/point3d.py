"""
`Point3D` module

This module defines the `Point3D` frozen data class, which represents a point in three-dimensional space.
"""
from __future__ import annotations

import math
from typing import NamedTuple


class Point3D(NamedTuple):
    """A frozen data class representing a 3D point with x, y, and z coordinates.

    Attributes:
        x: The x coordinate of the point.
        y: The y coordinate of the point.
        z: The z coordinate of the point.

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
        >>> p1.distance_to(p2)
        5.196152422706632
    """
    x: float
    y: float
    z: float

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __eq__(self, q: Point3D) -> bool:
        from geometric import epsilon
        p = self
        return all((abs(x1 - x2) < epsilon
                    for x1, x2 in zip([p.x, p.y, p.z], [q.x, q.y, p.z])))

    def distance_to(self, q: Point3D) -> float:
        """
        Calculates the distance between this `Point3D` and another `Point3D`.

        Args:
            q: The other `Point3D`.

        Returns:
            The distance between both points.
        """
        p = self
        return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2 + (q.z - p.z) ** 2)
