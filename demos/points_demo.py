from geometric import Point2D, Point3D


def points_demo():
    p = Point2D(2, 1)
    q = Point2D(2, 1.1)
    print(f"Float vs integer check: {p} == {q} -> {p == q}")  # -> False
    p = Point2D(2, 1)
    q = Point2D(2, 1.000001)
    print(f"Epsilon precision check 2D: {p} == {q} -> {p == q}")  # -> True
    p = Point3D(2, 3, 5)
    q = Point3D(1.9999999, 3.0000001, 5)
    print(f"Epsilon precision check 3D: {p} == {q} -> {p == q}")  # -> True
    p = Point3D(1, 2, 3)
    q = Point3D(1, 3, 2)
    print(f"Order equality check: {p} == {q} -> {p == q}")  # -> False
    p = Point2D(0, 0)
    q = Point3D(0, 0, 0)
    print(f"Different dimensions check: {p} == {q} -> {p == q}")  # -> ArithmeticError


if __name__ == "__main__":
    points_demo()
