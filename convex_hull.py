from dataclasses import dataclass
from typing import List
from point import Point
from convex_hull_calculator import ConvexHullCalculator


@dataclass
class ConvexHull:
    vertex_list: List[Point]

    def __init__(self, points: List[Point], calculator: ConvexHullCalculator):
        self.vertex_list = calculator.calculate(points)
