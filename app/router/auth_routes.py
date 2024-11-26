from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel. ext. asyncio.session import AsyncSession
from app.schemas.auth_schemas import UserCreateModel, UserModel
from app.service.auth_service import UserService
from app.config.dbconfig import get_session


auth_router = APIRouter()
user_service = UserService()


@auth_router.post("/signup", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user_Account(
    user_data: UserCreateModel,
    session: AsyncSession = Depends(get_session),
):
    """
    Create user account using email, username, first_name, last_name
    params: user_data: UserCreateModel
    """
    email = user_data.email

    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User with email already exists",
        )

    new_user = await user_service.create_user(user_data, session)

    return new_user
