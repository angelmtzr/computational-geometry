from typing import List

from geometric import Segment as Edge, Point2D as Point, Line


def slow_convex_hull_calculator(points: List[Point]) -> List[Point]:
    """
    Calculates and returns the vertices of the convex hull of a list of points in the plane.
    Given that its total running time is O(n^3) it is considered to be a slow algorithm.
    Any duplicate poins are removed.

    Args:
        points: The list of points.

    Returns:
        The vertices of the convex hull.
    """
    points = list(set(points))  # Remove duplicate points
    convex_hull_edges = get_convex_hull_edges(points)
    convex_hull_vertices = get_convex_hull_vertices(convex_hull_edges)
    return convex_hull_vertices


def get_convex_hull_edges(points: List[Point]) -> List[Edge]:
    convex_hull_edges: List[Edge] = []
    for p in points:
        for q in points:
            if p == q:
                continue
            valid = True
            for r in points:
                if r == p or r == q:
                    continue
                if r.is_left_of_line(Line(p, q)):
                    valid = False
            if valid:
                convex_hull_edges.append(Edge(p, q))
    return convex_hull_edges


def get_convex_hull_vertices(edges: List[Edge]) -> List[Point]:
    e1 = edges[0]
    convex_hull_vertices = [e1.p1, e1.p2]
    while convex_hull_vertices[0] != convex_hull_vertices[-1]:
        for e2 in edges:
            if e1.p2 == e2.p1:
                convex_hull_vertices.append(e2.p2)
                edges.remove(e2)
                e1 = e2
                break

    return convex_hull_vertices
