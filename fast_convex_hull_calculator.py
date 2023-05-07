from typing import List
from point import Point
from convex_hull_calculator import ConvexHullCalculator


class FastConvexHullCalculator(ConvexHullCalculator):
    @classmethod
    def calculate(cls, points: List[Point]) -> List[Point]:
        points = sorted(points, key=lambda p: p.x)  # TODO: could be part of the point class
        return []
