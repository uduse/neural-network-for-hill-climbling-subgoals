from nnhcs import Pos


class Scene(object):
    def __init__(self, start, goal, opt=None):
        self.start = start
        self.goal = goal
        self.opt = opt

    @classmethod
    def from_path(cls, path):
        scenes = []
        with open(path) as f:
            _, *lines = f.read().splitlines()
            for line in lines:
                _, _, _, _, x0, y0, x1, y1, opt = line.split('\t')
                x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
                scenes.append(Scene(Pos(x0, y0), Pos(x1, y1), float(opt)))
        return scenes

    def __repr__(self):
        return str(vars(self))
