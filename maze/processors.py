from maze.maze import Maze
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

        last_y = maze.height - 1

        for x in range(maze.width - 1):
            if sets[x] != sets[x + 1]:
                maze.verticals[last_y, x] = 0

                old = sets[x + 1]
                new = sets[x]
                for i in range(maze.width):
                    if sets[i] == old:
                        sets[i] = new


class MazeSolver:
    def solve_maze(self, maze: Maze, start: tuple[int, int], finish: tuple[int, int],
                   algorithm='astar') -> list[tuple[int, int]]:
        solution = []
        if algorithm == 'astar':
            solution = self.solve_a(maze, start, finish)
        return solution

    def solve_a(self, maze: Maze, start: tuple[int, int], finish: tuple[int, int]) -> list[tuple[int, int]]:

        open_set = {start}
        closed_set = set()
        g_score = {start: 0}
        came_from = {start: start}

        while open_set:
            current = min(open_set, key=lambda x: g_score[x] + abs(x[0] - finish[0]) + abs(x[1] - finish[1]))

            if current == finish:
                break

            open_set.remove(current)
            closed_set.add(current)

            for n in maze.neighbors(current[0], current[1]):

                if n in closed_set:
                    continue

                temp_g = g_score[current] + 1
                if n not in g_score or temp_g < g_score[n]:
                    came_from[n] = current
                    g_score[n] = temp_g
                    open_set.add(n)


        if finish not in came_from:
            return []

        path = []

        current = finish
        while current != start:
            path.append(current)
            current = came_from[current]

        path.append(start)
        path.reverse()

        return path
