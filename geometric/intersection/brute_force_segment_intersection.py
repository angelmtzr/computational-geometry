import itertools
from typing import Iterable

from .segment import segment_intersect, Segment


def brute_force_segment_intersection(segments: Iterable[Segment]):
    combinations = itertools.combinations(segments, 2)

    intersections = []
    for s1, s2 in combinations:
        intersection = segment_intersect(s1, s2)
        if intersection is None:
            continue
        intersections.append(intersection)

    return intersections
