from dataclasses import dataclass
from typing import List
from geometric import Point


@dataclass(slots=True, frozen=True)
class ConvexHull:
    points: List[Point]
    vertices: List[Point]
