from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    context = {"request": request, "text": "Benvenuto nella Biblioteca"}
    return templates.TemplateResponse("home.html", context)
