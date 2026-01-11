from pydantic import BaseModel
from maze.maze import Maze

class GenerateMazeRequest(BaseModel):
    width: int
    height: int
    algorithm: str


class GenerateMazeResponse(BaseModel):
    maze: Maze
