"""
The geometric package features a series of modules and classes for geometric pruposes.
An `epsilon` value, that may be overwritten to alter precison with floats, is used throughout the codebase.
"""
from .lines import Line, Segment
from .points import Point2D, Point3D

epsilon = 1e-4

__all__ = [name for name in dir() if not name.startswith("_")]
