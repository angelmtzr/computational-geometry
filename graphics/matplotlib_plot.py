import matplotlib.pyplot as plt
from geometric.convex.convex_hull import ConvexHull
from typing import List
from geometric.point import Point
from geometric.edge import Edge


class MatplotlibPlot:

    @staticmethod
    def show() -> None:
        """Displays the plot."""
        plt.show()

    @staticmethod
    def insert_points(points: List[Point]) -> None:
        """Inserts to the plot a set of points."""
        x, y = zip(*points)
        plt.scatter(x, y)

    @staticmethod
    def insert_all_edges(points: List[Point]) -> None:
        """Inserts to the plot all possible edges that can be drawn given a set of points."""
        for p in points:
            for q in points:
                plt.plot([p.x, q.x], [p.y, q.y])

    @staticmethod
    def insert_edges(edges: List[Edge]) -> None:
        """Inserts to the plot a set of edges."""
        for e in edges:
            plt.plot([e.origin.x, e.dest.x], [e.origin.y, e.dest.y])

    def insert_convex_hull(self, points: List[Point], convex_hull: ConvexHull) -> None:
        """Displays a convex hull. It uses matplotlib."""
        self.insert_points(points)
        edges_vertices = convex_hull.vertex_list.copy()
        edges_vertices.append(edges_vertices[0])  # We need to add the first vertex at the end to close the convex hull
        x, y = zip(*edges_vertices)
        plt.plot(x, y, c="orange")  # Draws the edges
