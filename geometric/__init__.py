from .point2d import Point2D
from .point3d import Point3D
from .segment import Segment

epsilon = 1e-4

__all__ = [name for name in dir() if not name.startswith("_")]
