import numpy as np


class Pos(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def heuristic(cls, a, b):
        return cls.manhattan(a, b)

    @classmethod
    def manhattan(cls, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    @classmethod
    def euclidean(cls, a, b):
        return np.hypot((a.x - b.x), (a.y - b.y))

    def __repr__(self):
        return f"<{self.x}, {self.y}>"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __iter__(self):
        yield self.x
        yield self.y
