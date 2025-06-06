from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

books = []

@router.get("/book_list")
async def book_list(request: Request):
    context = {"request": request, "books": books}
    return templates.TemplateResponse("list.html", context)

@router.get("/add_book")
async def add_book(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

@router.post("/books_form")
async def books_form(title: str = Form(...), author: str = Form(...)):
    books.append({"title": title, "author": author})
    return RedirectResponse(url="/book_list", status_code=303)
