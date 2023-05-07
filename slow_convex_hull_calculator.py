from typing import List
from convex_hull_calculator import ConvexHullCalculator
from matplotlib_plot import MatplotlibPlot
from point import Point
from edge import Edge


class SlowConvexHullCalculator(ConvexHullCalculator):
    def calculate(self, points: List[Point]) -> List[Point]:
        """Calculates and returns the convex hull of a list of points in the plane. Given that its total running time
        is O(n^3) it is considered to be a slow algorithm."""
        points = list(set(points))  # Remove duplicate points
        convex_hull_edges = self.get_convex_hull_edges(points)
        convex_hull_vertices = self.get_convex_hull_vertices(convex_hull_edges)
        return convex_hull_vertices

    @staticmethod
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
                    if r.is_left_of_line(p, q):
                        valid = False
                if valid:
                    convex_hull_edges.append(Edge(p, q))
        return convex_hull_edges

    @staticmethod
    def get_convex_hull_vertices(edges: List[Edge]) -> List[Point]:  # TODO: Check correctness
        e1 = edges[0]
        convex_hull_vertices = [e1.origin, e1.dest]
        while convex_hull_vertices[0] != convex_hull_vertices[-1]:
            for e2 in edges:
                if e1.dest == e2.origin:
                    convex_hull_vertices.append(e2.dest)
                    edges.remove(e2)
                    e1 = e2
                    break

        return convex_hull_vertices
