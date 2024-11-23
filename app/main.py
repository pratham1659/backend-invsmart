from typing import Optional, List
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, Header, status, HTTPException
from app.data.book_data import books
from app.repository.schemas import Book


def init_app():
    # db.init()

    app = FastAPI(
        title="Inventory Insight App",
        description="Login Page",
        version="1.0"
    )

    return app


app = init_app()


@app.get("/")
async def root():
    return {"message": "Welcomt to FastAPI"}


@app.get("/get_headers", status_code=201)
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)

):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers


@app.get("/greet")
async def greet_name(name: str) -> dict:
    return {"message": f"Hello {name}"}
# http://localhost:8888/greet?name=pratham


@app.get("/greet/{name}")
async def greet_name1(name: str, age: int) -> dict:
    return {"message": f"Hello {name} and Age is {age}"}
# http://localhost:8888/greet/Pratham?age=23


@app.get("/greet")
async def greet_name2(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name} and Age is {age}"}


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books")
async def create_a_book() -> dict:
    pass


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    pass


@app.get("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Book not found")

    # @app.get("/posts")
    # async def get_posts():
    #     cursor.execute("""SELECT * FROM posts ORDER BY id ASC""")
    #     posts = cursor.fetchall()
    #     return {"message": posts}

    # @app.post("/posts", status_code=status.HTTP_201_CREATED)
    # async def create_posts(payLoad: Post):
    #     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #                    (payLoad.title, payLoad.content, payLoad.published))
    #     new_posts = cursor.fetchone()

    #     conn.commit()  # This will help you to commit the changes
    #     return {"data": new_posts}

    # @app.get("/posts/latest")
    # async def get_latest_post():
    #     post = my_posts[len(my_posts) - 1]
    #     return {"message": post}

    # @app.get("/posts/{id}")
    # async def get_post(id: str):
    #     cursor.execute("""SELECT * FROM posts WHERE id = %s """,
    #                    (str(id),))  # Note the trailing comma
    #     post = cursor.fetchone()
    #     if not post:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                             detail=f"post with id: {id} was not found")
    #     return {"post_details": post}

    # @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
    # async def delete_posts(id: int, response: Response):
    #     cursor.execute(
    #         """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    #     deleted_post = cursor.fetchone()
    #     conn.commit()  # This will commit the changes
    #     if deleted_post is None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                             detail=f"Post with id: {id} does not exist")
    #     return Response(status_code=status.HTTP_404_NOT_FOUND)

    # @app.put("/posts/{id}")
    # def update_post(id: int, post: Post):
    #     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
    #                    (post.title, post.content, post.published, str(id),))
    #     updated_post = cursor.fetchone()
    #     conn.commit()

    #     if updated_post is None:
    #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                             detail=f"Post with id: {id} does not exist")
    #     return {"data": updated_post}


def start():
    """Launched with 'poetry run start' at root level """
    uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
