from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pathlib import Path

router = APIRouter()

router.get('/', response_class=HTMLResponse)
def index():
    return Path('../static/index.html').read_text()
