"""
`Line` module

This module defines the `Line` frozen data class, which represents a line in two-dimensional space.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from geometric import Point2D


@dataclass(frozen=True, slots=True)
class Line:
    """
    A frozen data class representing a line defined by two `Point2D`.

    Attributes:
        p1: The first `Point2D`.
        p2: The second `Point2D`.

    Example:
        >>> from geometric import Line
        >>> line = Line(Point2D(0, 0), Point2D(1, 1))
        >>> line.p1
        (0, 0)
        >>> line.p2
        (1, 1)
    """
    p1: Point2D
    p2: Point2D

    def __contains__(self, p: Point2D) -> bool:
        """
        Checks if this `Line` contains a given point.

        Args:
           p: The point.

        Returns:
            True if this `Line` contains the point, False otherwise.
        """
        return p.y == self.get_y(p.x)

    def get_slope(self) -> float:
        """
        Calculates the slope of this `Line`. If the line is vertical, `math.inf` is returned.

        Returns:
           The slope.
        """
        p1 = self.p1
        p2 = self.p2
        if self.is_vertical():
            return math.inf
        return (p2.y - p1.y) / (p2.x - p1.x)

    def get_y_intercept(self) -> float | None:
        """
        Calculates the y intercept of this `Line`. If the line is vertical, `None` is returned.

        Returns:
           `None` if the line is vertical, the y intercept otherwise.
        """
        if self.is_vertical():
            return None
        p = self.p1
        m = self.get_slope()
        return p.y - m * p.x

    def is_vertical(self) -> bool:
        """
        Checks if this `Line` is vertical.

        Returns:
           `True` if vertical, `False` otherwise.
        """
        return self.p1.x == self.p2.x

    def get_y(self, x: float) -> float | None:
        """
        Calculates the y value of this `Line` at the given x value. If the line is vertical, `None` is returned.

        Args:
           x: The x value.

        Returns:
           `None` if the line is vertical, the y value otherwise.
        """
        if self.is_vertical():
            return None
        m = self.get_slope()
        b = self.get_y_intercept()
        return m * x + b


def line_intersect(l1: Line, l2: Line) -> Point2D | None:
    """
    Calculates the intersection of the given lines if any.
    If lines are parallel `None` is returned.

    Args:
       l1: The first line.
       l2: The second line.

    Returns:
       `None` if parallel, the intersection otherwise.
    """
    from geometric import Point2D
    if lines_are_parallel(l1, l2):
        return None

    if l1.is_vertical():
        x = l1.p1.x
        y = l2.get_y(x)
        return Point2D(x, y)

    if l2.is_vertical():
        x = l2.p1.x
        y = l1.get_y(x)
        return Point2D(x, y)

    m1 = l1.get_slope()
    b1 = l1.get_y_intercept()
    m2 = l2.get_slope()
    b2 = l2.get_y_intercept()
    x = (b2 - b1) / (m1 - m2)
    y = l1.get_y(x)
    return Point2D(x, y)


def lines_are_parallel(l1: Line, l2: Line) -> bool:
    """
    Checks wether the given lines are parallel.

    Args:
       l1: The first line.
       l2: The second line.

    Returns:
       `True` if parallel, `False` otherwise.
    """
    return l1.get_slope() == l2.get_slope()
