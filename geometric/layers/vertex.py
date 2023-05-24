from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Vertex:
    name: str
    x: float
    y: float
    incident_edge_name: str
