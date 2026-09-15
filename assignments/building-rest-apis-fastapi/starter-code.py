from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookCreate(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "Python for Everybody", "author": "Charles Severance"},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}


# TODO: Implement GET /books


# TODO: Implement GET /books/{book_id}


# TODO: Implement POST /books


# TODO: Implement PUT /books/{book_id}


# TODO: Implement DELETE /books/{book_id}
