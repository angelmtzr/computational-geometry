from typing import List
from geometric import Point


class FastConvexHullCalculator:
    @classmethod
    def calculate(cls, points: List[Point]) -> List[Point]:
        raise NotImplementedError()
        # points = sorted(points, key=lambda p: p.x)  # Could be part of the point class
        # return []
