from __future__ import annotations
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def is_left_of_line(self, p: Point, q: Point) -> bool:
        """Check if the point is to the left of a line in the plane defined by two points."""
        r = self

        # Calculate the vectors
        pq = Point(q.x - p.x, q.y - p.y)
        pr = Point(r.x - p.x, r.y - p.y)

        # Calculate the cross product of pq and pr
        cross_product = pq.x * pr.y - pq.y * pr.x

        # If the cross product is positive, r is to the left of pq
        return cross_product > 0
