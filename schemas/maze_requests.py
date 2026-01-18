from pydantic import BaseModel
from typing import Tuple, List
from maze.maze import Maze

class MazeBuildRequest(BaseModel):
    width: int
    height: int
    algorithm: str

class MazeData(BaseModel):
    width: int
    height: int
    verticals: List[List[int]]
    horizontals: List[List[int]]

class MazeSolveRequest(BaseModel):
    maze: MazeData
    algorithm: str
    start: Tuple[int, int]
    finish: Tuple[int, int]
