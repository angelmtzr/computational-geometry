"""
The display segment intersections module defines a simple function to display line segment intersections
using matplotlib.
"""
from __future__ import annotations

from typing import List
from typing import TYPE_CHECKING

import matplotlib.pyplot as plt

if TYPE_CHECKING:
    from geometric import Point2D, Segment


def display_segment_intersections(segments: List[Segment], intersections: List[Point2D]) -> None:
    """
    Displays the given line segments and all their intersections using matplotlib.

    Args:
        segments: The line segments.
        intersections: The intersection points.
    """
    _, ax = plt.subplots()

    plt.style.use('seaborn')
    plt.title('SEGMENT INTERSECTIONS')

    for s in segments:
        x = [s.p1.x, s.p2.x]
        y = [s.p1.y, s.p2.y]
        plt.plot(x, y, linewidth=0.75)

    x, y = zip(*intersections)
    s = [10] * len(intersections)
    ax.scatter(x, y, c="red", label="Intersections", s=s)

    ax.legend(loc="lower left", bbox_to_anchor=(0.6, -0.37))
    plt.subplots_adjust(bottom=0.25)
    plt.show()
