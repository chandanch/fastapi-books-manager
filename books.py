from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "My Dion Man", "author": "chandio", "category": "Deep Minds"},
    {"title": "Findmens Gold", "author": "Fdio", "category": "Lean"},
    {"title": "Visible Gold", "author": "Fdio", "category": "Lean"},
    {"title": "Visible Sliver", "author": "chandio", "category": "Deep Minds"},
]


# first API
@app.get("/healthcheck")
async def health_check():
    return {"status": "OK", "message": "Service is up!"}


@app.get("/books")
async def get_all_books():
    return BOOKS
