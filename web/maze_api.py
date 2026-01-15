from fastapi import APIRouter
from maze.maze import Maze
from maze.processors import MazeBuilder, MazeSolver

router = APIRouter(prefix='/api', tags=['api'])
@router.get("/maze")
def get_maze():
    maze = Maze()
    builder = MazeBuilder()
    builder.build_maze(maze)
    solver = MazeSolver()
    path = solver.solve_maze(maze, (0, 0), (49, 49))

    response = {
        'width': maze.width,
        'height': maze.height,
        'verticals': maze.verticals.tolist(),
        'horizontals': maze.horizontals.tolist(),
        'path': path,
    }
    return response
