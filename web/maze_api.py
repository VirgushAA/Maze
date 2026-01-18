import numpy as np
from fastapi import APIRouter
from maze.maze import Maze
from maze.processors import MazeBuilder, MazeSolver
from schemas.maze_requests import MazeBuildRequest, MazeSolveRequest

router = APIRouter(prefix='/api', tags=['api'])

@router.post("/maze/build")
def build_maze(req: MazeBuildRequest):
    maze = Maze(req.width, req.height)
    builder = MazeBuilder()
    builder.build_maze(maze)

    response = {
        'width': maze.width,
        'height': maze.height,
        'verticals': maze.verticals.tolist(),
        'horizontals': maze.horizontals.tolist(),
    }
    return response

@router.post("/maze/solve")
def solve_maze(req: MazeSolveRequest):
    m = req.maze
    maze = Maze(m.width, m.height)
    maze.verticals = np.array(m.verticals, dtype=np.uint8)
    maze.horizontals = np.array(m.horizontals, dtype=np.uint8)

    solver = MazeSolver()
    path = solver.solve_maze(maze, req.start, req.finish, req.algorithm)

    return path
