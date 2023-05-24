from typing import Dict, List

from geometric import Segment, Point2D
from geometric.intersection import brute_force_segment_intersection, display_segment_intersections
from geometric.layers import Vertex, Edge

WIDTH = 700
HEIGHT = 700

PATH = "./data/layers/"


def read_vertices(layer_number: int) -> Dict[str, Vertex]:
    vertices: Dict[str, Vertex] = dict()
    with open(f"{PATH}layer0{layer_number}.vertices") as f:
        for line in f.readlines()[4:]:
            name, x, y, incident_edge = line.split()
            vertex = Vertex(name, float(x), float(y), incident_edge)
            vertices[name] = vertex
    return vertices


def read_edges(layer_number: int) -> Dict[str, Edge]:
    edges: Dict[str, Edge] = dict()
    with open(f"{PATH}layer0{layer_number}.aristas") as f:
        for line in f.readlines()[4:]:
            name, origin, pair_edge, face, next_edge, prev_edge = line.split()
            edge = Edge(name, origin, pair_edge, face, next_edge, prev_edge)
            edges[name] = edge
    return edges


def read_layers(n: int) -> List[Segment]:
    segments: List[Segment] = []
    for layer_number in range(1, n + 1):
        vertices_dict: Dict[str, Vertex] = read_vertices(layer_number)
        edges_dict: Dict[str, Edge] = read_edges(layer_number)
        for edge_name in edges_dict:
            origin_vertex_name = edges_dict[edge_name].origin_vertex_name
            v1 = vertices_dict[origin_vertex_name]
            pair_edge_name = edges_dict[edge_name].pair_edge_name
            dest_vertex_name = edges_dict[pair_edge_name].origin_vertex_name
            v2 = vertices_dict[dest_vertex_name]
            segment = Segment(Point2D(v1.x, v1.y), Point2D(v2.x, v2.y))
            segments.append(segment)
    return segments


def layer_overlapping_demo():
    segments = read_layers(n=5)
    intersections = brute_force_segment_intersection(segments)
    display_segment_intersections(segments, intersections)


if __name__ == '__main__':
    layer_overlapping_demo()
