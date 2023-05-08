from typing import Protocol, List

from geometric import Point2D


class ConvexHullCalculator(Protocol):
    def calculate(self, points: List[Point2D]) -> List[Point2D]:
        """Calculates and returns the convex hull of a list of points in the plane."""
