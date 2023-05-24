from dataclasses import dataclass
from typing import Dict

from .edge import Edge
from .vertex import Vertex


@dataclass(slots=True, frozen=True)
class Layer:
    edges: Dict[str, Edge]
    # faces: Dict[str, Face]
    vertices: Dict[str, Vertex]
