from typing import Protocol, List
from geometric import Point


class ConvexHullCalculator(Protocol):
    def calculate(self, points: List[Point]) -> List[Point]:
        """Calculates and returns the convex hull of a list of points in the plane."""
