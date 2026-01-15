from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from web.maze_api import router as maze_api_router
from web.pages import router as pages_router


app = FastAPI()
app.include_router(maze_api_router)
app.include_router(pages_router)

app.mount("/",
          StaticFiles(directory="static", html=True),
          name="static",
          )
