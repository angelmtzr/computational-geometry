"""
`Segment` module

This module defines the `Segment` frozen data class, which represents a line segment in two-dimensional space.
"""

from dataclasses import dataclass

from .point2d import Point2D


@dataclass(frozen=True, slots=True)
class Segment:
    """
    A frozen data class representing a line segment between two `Point2D`.

    Attributes:
        origin (Point2D): The starting point of the line segment.
        dest (Point2D): The ending point of the line segment.

    Example:
        >>> from geometric import Segment as Edge
        >>> edge = Edge(Point2D(0, 0), Point2D(1, 1))
        >>> edge.origin
        (0, 0)
        >>> edge.dest
        (1, 1)
    """
    origin: Point2D
    dest: Point2D
