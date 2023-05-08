from typing import List

from geometric import Point2D


class FastConvexHullCalculator:
    @classmethod
    def calculate(cls, points: List[Point2D]) -> List[Point2D]:
        raise NotImplementedError()
        # points = sorted(points, key=lambda p: p.x)  # Could be part of the point class
        # return []
