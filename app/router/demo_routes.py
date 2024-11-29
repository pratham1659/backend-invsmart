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
