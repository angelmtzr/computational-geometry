"""
The geometric package features a series of modules and classes for geometric pruposes.
An epsilon value, that may be overwritten to alter precison with floats, is used throughout the codebase.
You can modify it doing the following:

>>> import geometric
>>> geometric.epsilon = 1e-9
"""
from .line import Line
from .points import Point2D, Point3D
from .segment import Segment

epsilon = 1e-4

__all__ = [name for name in dir() if not name.startswith("_")]
