import enum


class TileType(enum.Enum):
    PASSABLE_TERRAIN_1 = "."
    PASSABLE_TERRAIN_2 = "G"
    OUT_OF_BOUNDS_1 = "@"
    OUT_OF_BOUNDS_2 = "O"
    TREES = "T"
    SWAMP = "S"
    WATER = "W"

    @classmethod
    def passable(cls, tile_type):
        assert isinstance(tile_type, TileType)
        return tile_type in [
            cls.PASSABLE_TERRAIN_1,
            cls.PASSABLE_TERRAIN_2,
        ]
