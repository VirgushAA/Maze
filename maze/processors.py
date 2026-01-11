from maze import Maze
from random import random, randint, sample

class MazeBuilder:
    def build_maze(self, maze: Maze, algorithm='eller') -> None:
        if algorithm == 'eller':
            self.build_eller(maze)


    def build_eller(self, maze: Maze) -> None:
        sets = list(range(maze.width))
        new_set_id = maze.width

        for y in range(maze.height - 1):

            for x in range(maze.width - 1):
                if sets[x] != sets[x + 1] and random() < 0.5:
                    maze.verticals[y, x] = 0
                    for i in range(maze.width):
                        if sets[i] == sets[x + 1]:
                            sets[i] = sets[x]

            unique_ids = set(sets)
            for set_id in unique_ids:
                cells = [x for x in range(maze.width) if sets[x] == set_id]
                k = randint(1, len(cells))
                chosen = sample(cells, k)
                for x in chosen:
                    maze.horizontals[y, x] = 0

            for x in range(maze.width):
                if maze.horizontals[y, x] == 0:
                    sets[x] = sets[x]
                else:
                    sets[x] = new_set_id
                    new_set_id += 1

        for x in range(maze.width - 1):
            if sets[x] != sets[x + 1]:
                maze.verticals[y, x] = 0
                for i in range(maze.width):
                    if sets[i] == sets[x + 1]:
                        sets[i] = sets[x]


class MazeSolver:
    def solve_maze(self, maze: Maze, start: tuple[int, int], finish: tuple[int, int],
                   algorithm='A*') -> list[tuple[int, int]]:
        solution = []
        if algorithm == 'A*':
            solution = self.solve_A(maze, start, finish)
        return solution

    def solve_A(self, maze: Maze, start: tuple[int, int], finish: tuple[int, int]) -> list[tuple[int, int]]:
        pass
