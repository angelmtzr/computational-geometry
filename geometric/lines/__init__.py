from .line import Line
from .segment import Segment

epsilon = 1e-4

__all__ = [name for name in dir() if not name.startswith("_")]
