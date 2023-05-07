from typing import Protocol, List
from convex_hull import ConvexHull
from point import Point


class ConvexHullDisplayer(Protocol):  # TODO: Might erase
    def display(self, points: List[Point], convex_hull: ConvexHull) -> None:
        """Displays a convex hull."""
