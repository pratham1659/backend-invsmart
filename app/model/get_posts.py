from fastapi import APIRouter

# Create a router instance
router = APIRouter()

# Sample data
my_posts = [
    {"id": 1, "title": "title of post 1", "content": "content of post 1"},
    {"id": 2, "title": "favorite foods", "content": "I like pizza"},
]

# Define the endpoint


@router.get("/posts")
async def get_posts():
    return {"message": my_posts}
