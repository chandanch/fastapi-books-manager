from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "My Dillon Man", "author": "chandio", "category": "Deep Minds", "id": 1},
    {"title": "Findmens Gold", "author": "Fdio", "category": "Lean", "id": 2},
    {"title": "Visible Gold", "author": "Fdio", "category": "Lean", "id": 3},
    {"title": "Visible Sliver", "author": "chandio", "category": "Deep Minds", "id": 4},
]


# first API
@app.get("/healthcheck")
async def health_check():
    return {"status": "OK", "message": "Service is up!"}


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/favbooks")
def get_fav_book():
    return BOOKS[1]


@app.get("/books/{book_id}")
async def get_book_details(book_id: int):
    for book in BOOKS:
        if book.get("id") == book_id:
            return book
    return "Not Found"
