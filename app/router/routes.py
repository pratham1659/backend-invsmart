from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from app.schemas.schemas import Book, BookCreateModel, BookUpdateModel
from app.service.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from app.config.dbconfig import get_session


book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)
    return new_book


@book_router.get("/{book_uid}", response_model=Book)
async def get_book(book_uid: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)

    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book is not found"
        )


@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update_data, session)

    if updated_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book is not found"
        )
    else:
        return updated_book


@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str,  session: AsyncSession = Depends(get_session)):
    deleted_book = await book_service.delete_book(book_uid, session)

    if deleted_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Book not found")
    else:
        return {"message": "Deleted Successfully"}

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
