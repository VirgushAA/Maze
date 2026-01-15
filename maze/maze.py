import numpy as np

class Maze:
    def __init__(self, width=50, height=50):
        self.width = width
        self.height = height
        self.horizontals = np.ones((height, width), dtype=np.uint8)
        self.verticals = np.ones((height, width), dtype=np.uint8)


    def neighbors(self, x, y) -> list[tuple[int, int]]:
        ns = []
        if x < self.width - 1 and self.verticals[y, x] == 0:
            ns.append((x + 1, y))
        if x > 0 and self.verticals[y, x - 1] == 0:
            ns.append((x - 1, y))
        if y < self.height - 1 and self.horizontals[y, x] == 0:
            ns.append((x, y + 1))
        if y > 0 and self.horizontals[y - 1, x] == 0:
            ns.append((x, y - 1))
        return ns
