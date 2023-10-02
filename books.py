from fastapi import FastAPI, Body

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
    """
    Health Check
    """
    return {"status": "OK", "message": "Service is up!"}


@app.get("/books")
async def get_all_books():
    return BOOKS


@app.get("/books/favbooks")
def get_fav_book():
    return BOOKS[1]


# Search Books by category using Query Param
@app.get("/books/search")
async def search_books_by_category(category: str):
    """
    Search books based on category or author
    """
    books_list = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_list.append(book)
    return books_list


# Get Books by Id using Path Param.
# Path params are enclosed wth {<PARAM_NAME>} in the route
# the path param name must match the parameter name in the function
@app.get("/books/{book_id}")
async def get_book_details(book_id: int):
    """
    Get Books details by ID
    """
    for book in BOOKS:
        if book.get("id") == book_id:
            return book
    return "Not Found"


# Add new book
# Use the POST HTTP method and BODY to extract the request body
# Assign the value returned from BODY() to a function parameter
@app.post("/books")
async def add_book(new_book=Body()):
    """
    Create a new book
    """
    BOOKS.append(new_book)
    return {"status": "success", "data": new_book}


# Update book
# Use the same BODY() to extract the request body
@app.put("/books/{book_id}")
async def update_book(book_id: int, book=Body()):
    """
    Update book based on ID
    """
    for i, book_item in enumerate(BOOKS):
        if book_item.get("id") == book_id:
            BOOKS[i] = book
    return {"status": "sucess", "data": book}


# Delete Book
# use the DELETE HTTP method
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(BOOKS):
        if book.get("id") == book_id:
            BOOKS.pop(i)
    return {"status": "Success", "id": book_id}
