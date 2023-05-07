from dataclasses import dataclass
from point import Point


@dataclass
class Edge:
    origin: Point
    dest: Point
