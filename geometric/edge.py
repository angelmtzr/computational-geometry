from dataclasses import dataclass
from geometric import Point


@dataclass(frozen=True, slots=True)
class Edge:
    origin: Point
    dest: Point
