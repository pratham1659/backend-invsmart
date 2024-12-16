# # import time
# # import uvicorn
# # from fastapi import FastAPI, Response, status, HTTPException
# # from app.config.dbconfig import db
# # from dotenv import load_dotenv
# # import os
# # from app.model.posts import Post
# # from random import randrange
# # import psycopg2
# # from psycopg2.extras import RealDictCursor

# # load_dotenv()

# # SECRET_KEY = os.getenv("SECRET_KEY")
# # if not SECRET_KEY:
# #     raise ValueError("SECRET_KEY is not set in the .env file")

# # ALGORITHM = "HS256"

# # ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # while True:
# #     try:
# #         conn = psycopg2.connect(
# #             host='localhost', database='fastapi', user='postgres', password='mysql', cursor_factory=RealDictCursor)
# #         cursor = conn.cursor()
# #         print("Database Connection was Successfull")
# #         break
# #     except Exception as e:
# #         print("Connecting to Database failed....")
# #         print("Error: ", e)
# #         time.sleep(2)


# # def init_app():
# #     db.init()

# #     app = FastAPI(
# #         title="Inventory Insight App",
# #         description="Login Page",
# #         version="1.0"
# #     )

# #     @app.on_event("startup")
# #     async def startup():
# #         await db.create_all()

# #     @app.on_event("shutdown")
# #     async def shutdown():
# #         await db.close()

# #     return app


# # app = init_app()


# # @app.get("/")
# # async def root():
# #     return {"message": "Welcomt to FastAPI"}


# # @app.get("/test/{item_id}/")
# # async def test(item_id: str):
# #     return {"Hello ": item_id}


# # my_posts = [{"id": 1, "title": "title of post 1", "content": "content of post 1", "published": False, "rating": 4},
# #             {"id": 2, "title": "favorite foods", "content": "I like pizza", "published": True, "rating": 5}]


# # @app.get("/posts")
# # async def get_posts():
# #     cursor.execute("""SELECT * FROM posts""")
# #     posts = cursor.fetchall()
# #     return {"message": posts}


# # @app.post("/posts", status_code=status.HTTP_201_CREATED)
# # async def create_posts(payLoad: Post):
# #     post_dict = payLoad.dict()
# #     post_dict['id'] = randrange(0, 1000000)
# #     my_posts.append(post_dict)
# #     print(payLoad.model_dump_json)
# #     return {"data": post_dict}


# # def find_post(id):
# #     for p in my_posts:
# #         if p["id"] == id:
# #             return p


# # @app.get("/posts/latest")
# # async def get_latest_post():
# #     post = my_posts[len(my_posts) - 1]
# #     return {"message": post}


# # @app.get("/posts/{id}")
# # async def get_post(id: int, response: Response):
# #     post = find_post(id)
# #     if not post:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"post with id: {id} was not found")
# #     return {"post_details": post}


# # def find_index_post(id):
# #     for i, p in enumerate(my_posts):
# #         if p["id"] == id:
# #             return i


# # @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_posts(id: int, response: Response):
# #     # deleting a post
# #     # find the index in the array that has required ID
# #     # my_posts.pop(index)
# #     index = find_index_post(id)
# #     if index is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Post with id: {id} does not exist")
# #     my_posts.pop(index)
# #     return Response(status_code=status.HTTP_404_NOT_FOUND)


# # @app.put("/posts/{id}")
# # def update_post(id: int, post: Post):
# #     print(post)
# #     index = find_index_post(id)
# #     if index is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Post with id: {id} does not exist")
# #     post_dict = post.dict()
# #     post_dict['id'] = id
# #     my_posts[index] = post_dict
# #     return {"data": post_dict}


# # def start():
# #     """Launched with 'poetry run start' at root level """
# #     uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)


# # @app.get("/posts")
# # async def get_posts():
# #     cursor.execute("""SELECT * FROM posts ORDER BY id ASC""")
# #     posts = cursor.fetchall()
# #     return {"message": posts}


# # @app.post("/posts", status_code=status.HTTP_201_CREATED)
# # async def create_posts(payLoad: Post):
# #     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
# #                    (payLoad.title, payLoad.content, payLoad.published))
# #     new_posts = cursor.fetchone()

# #     conn.commit()  # This will help you to commit the changes
# #     return {"data": new_posts}


# # @app.get("/posts/latest")
# # async def get_latest_post():
# #     post = my_posts[len(my_posts) - 1]
# #     return {"message": post}


# # @app.get("/posts/{id}")
# # async def get_post(id: str):
# #     cursor.execute("""SELECT * FROM posts WHERE id = %s """,
# #                    (str(id),))  # Note the trailing comma
# #     post = cursor.fetchone()
# #     if not post:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"post with id: {id} was not found")
# #     return {"post_details": post}


# # def find_index_post(id):
# #     for i, p in enumerate(my_posts):
# #         if p["id"] == id:
# #             return i


# # @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# # async def delete_posts(id: int, response: Response):
# #     cursor.execute(
# #         """DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
# #     deleted_post = cursor.fetchone()
# #     conn.commit()  # This will commit the changes
# #     if deleted_post is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Post with id: {id} does not exist")
# #     return Response(status_code=status.HTTP_404_NOT_FOUND)


# # @app.put("/posts/{id}")
# # def update_post(id: int, post: Post):
# #     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
# #                    (post.title, post.content, post.published, str(id),))
# #     updated_post = cursor.fetchone()
# #     conn.commit()

# #     if updated_post is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Post with id: {id} does not exist")
# #     return {"data": updated_post}


# # def start():
# #     """Launched with 'poetry run start' at root level """
# #     uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)


# import time
# from typing import Optional
# from pydantic import BaseModel
# import uvicorn
# from fastapi import FastAPI, Header, Response, status, HTTPException
# from app.config.dbconfig import db
# from dotenv import load_dotenv
# import os
# import psycopg2
# from psycopg2.extras import RealDictCursor

# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY")
# if not SECRET_KEY:
#     raise ValueError("SECRET_KEY is not set in the .env file")

# ALGORITHM = "HS256"

# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='mysql', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database Connection was Successfull")
#         break
#     except Exception as e:
#         print("Connecting to Database failed....")
#         print("Error: ", e)
#         time.sleep(2)


# def init_app():
#     # db.init()

#     app = FastAPI(
#         title="Inventory Insight App",
#         description="Login Page",
#         version="1.0"
#     )

#     # @app.on_event("startup")
#     # async def startup():
#     #     await db.create_all()

#     # @app.on_event("shutdown")
#     # async def shutdown():
#     #     await db.close()

#     return app


# app = init_app()


# # @app.get("/greet")
# # async def greet_name(name: str) -> dict:
# #     return {"message": f"Hello {name}"}
# # http://localhost:8888/greet?name=pratham


# @app.get("/greet/{name}")
# async def greet_name1(name: str, age: int) -> dict:
#     return {"message": f"Hello {name} and Age is {age}"}
# # http://localhost:8888/greet/Pratham?age=23


# @app.get("/greet")
# async def greet_name2(name: Optional[str] = "User", age: int = 0) -> dict:
#     return {"message": f"Hello {name} and Age is {age}"}


# @app.get("/")
# async def root():
#     return {"message": "Welcomt to FastAPI"}


# @app.get("/test/{item_id}/")
# async def test(item_id: str):
#     return {"Hello ": item_id}


# @app.get("/posts")
# async def get_posts():
#     cursor.execute("""SELECT * FROM posts ORDER BY id ASC""")
#     posts = cursor.fetchall()
#     return {"message": posts}


# # @app.post("/posts", status_code=status.HTTP_201_CREATED)
# # async def create_posts(payLoad: Post):
# #     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
# #                    (payLoad.title, payLoad.content, payLoad.published))
# #     new_posts = cursor.fetchone()

# #     conn.commit()  # This will help you to commit the changes
# #     return {"data": new_posts}


# # @app.get("/posts/latest")
# # async def get_latest_post():
# #     post = my_posts[len(my_posts) - 1]
# #     return {"message": post}


# class BookCreateModel(BaseModel):
#     title: str
#     author: str


# @app.post("/create_book")
# async def create_book(book_data: BookCreateModel):
#     return {
#         "title": book_data.title,
#         "author": book_data.author
#     }


# @app.get("/get_headers", status_code=201)
# async def get_header(
#     accept: str = Header(None),
#     content_type: str = Header(None),
#     user_agent: str = Header(None),
#     host: str = Header(None)

# ):
#     request_headers = {}
#     request_headers["Accept"] = accept
#     request_headers["Content-Type"] = content_type
#     request_headers["User-Agent"] = user_agent
#     request_headers["Host"] = host

#     return request_headers


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


# # @app.put("/posts/{id}")
# # def update_post(id: int, post: Post):
# #     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
# #                    (post.title, post.content, post.published, str(id),))
# #     updated_post = cursor.fetchone()
# #     conn.commit()

# #     if updated_post is None:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Post with id: {id} does not exist")
# #     return {"data": updated_post}


# def start():
#     """Launched with 'poetry run start' at root level """
#     uvicorn.run("app.main:app", host="localhost", port=8888, reload=True)
