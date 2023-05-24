from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Edge:
    name: str
    origin_vertex_name: str
    pair_edge_name: str
    face_name: str
    next_edge_name: str
    prev_edge_name: str
