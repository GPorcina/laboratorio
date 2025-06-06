from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import frontend, books

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(frontend.router)
app.include_router(books.router)
