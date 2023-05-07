from dataclasses import dataclass
from point import Point


@dataclass
class Line:
    p: Point
    q: Point
