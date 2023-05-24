"""
`Segment` module

This module defines the `Segment` frozen data class, which represents a line segment in two-dimensional space.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from geometric import Point2D


class Segment(NamedTuple):
    """
    A frozen data class representing a line segment between two `Point2D`.

    Attributes:
        p1: The starting point of the line segment.
        p2: The ending point of the line segment.

    Example:
        >>> from geometric import Segment
        >>> s = Segment(Point2D(0, 0), Point2D(1, 1))
        >>> s.p1
        (0, 0)
        >>> s.p2
        (1, 1)
    """
    p1: Point2D
    p2: Point2D

    def __contains__(self, p: Point2D) -> bool:
        p1, p2 = self.p1, self.p2
        if (max(p1.x, p2.x) >= p.x >= min(p1.x, p2.x) and
                max(p1.y, p2.y) >= p.y >= min(p1.y, p2.y)):
            return True


def segment_intersect(s1: Segment, s2: Segment) -> Point2D | None:
    """
    Calculates the intersection of the given line segments if any. If segments are parallel `None` is returned.

    Args:
       s1: The first line segment.
       s2: The second line segment.

    Returns:
       `None` if parallel, the intersection otherwise.
    """
    from geometric.lines.line import Line, line_intersect
    p = line_intersect(Line(s1.p1, s1.p2), Line(s2.p1, s2.p2))

    if p is None:
        return None

    if p not in s1 or p not in s2:
        return None

    return p
