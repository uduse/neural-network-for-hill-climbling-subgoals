import pathlib
import numpy as np

from nnhcs.tile_type import TileType
from nnhcs import Pos


class World(object):
    ROAD = 0
    WALL = 1

    @classmethod
    def from_path(cls, path):
        with open(path) as f:
            _, height, width, _, *data = f.read().splitlines()
            data = np.asarray([[TileType(char) for char in row] for row in data]).T
        vf = np.vectorize(lambda x: not TileType.passable(x))
        bitmap = vf(data).astype(int)
        return World(path.name, bitmap)

    def __init__(self, name=None, bitmap=None):
        self.name = name
        self.bitmap = bitmap
        self.bitmap.setflags(write=False)

    @property
    def shape(self):
        return self.bitmap.shape

    def __iter__(self):
        x_max, y_max = self.shape
        for x in range(x_max):
            for y in range(y_max):
                yield Pos(x, y)

    def get(self, pos):
        return self.bitmap[pos.x, pos.y]

    def _valid(self, pos):
        return self.in_bound(pos) and (self.get(pos) == World.ROAD)

    def get_adjs(self, pos):
        adj_poses = [
            Pos(pos.x + 1, pos.y),
            Pos(pos.x - 1, pos.y),
            Pos(pos.x, pos.y - 1),
            Pos(pos.x, pos.y + 1)
        ]
        return list(filter(self._valid, adj_poses))

    def get_all_adjs(self, pos):
        adj_poses = [
            Pos(pos.x + 1, pos.y),
            Pos(pos.x - 1, pos.y),
            Pos(pos.x, pos.y - 1),
            Pos(pos.x, pos.y + 1)
        ]
        return list(filter(self.in_bound, adj_poses))

    def in_bound(self, pos):
        xs, ys = self.shape
        return (0 <= pos.x < xs) and (0 <= pos.y < ys)

    def is_adj(self, source, target):
        return target in self.get_adjs(source)

    def get_cost(self, source, target):
        if not self.is_adj(source, target):
            raise ValueError
        else:
            return 1


#             return ((source.x - target.x) ** 2 + (source.y - target.y) ** 2) ** 0.5

def get_selected():
    # use_cache = False
    use_problems = ["selected"]

    maps_root = pathlib.Path('maps')
    problems = {}
    for map_set_root in maps_root.iterdir():
        if map_set_root.name in use_problems:
            print(map_set_root)
            world_set = {}
            map_set_maps_dir = map_set_root / (map_set_root.name + '-map')
            for map_path in list(map_set_maps_dir.iterdir()):
                print(map_path)
                world = World.from_path(map_path)
                world_set[world.name] = world
            print()
            problems[map_set_root.name] = world_set
    selected = problems['selected']
    return selected
