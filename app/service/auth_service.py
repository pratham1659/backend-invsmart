from sqlmodel import select
from app.model.authmodel import User
from app.schemas.auth_schemas import UserCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from app.utils.auth_utils import generate_passwd_hash


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email == email)

        result = await session.exec(statement)

        user = result.first()

        return user

    async def user_exists(self, email, session: AsyncSession):
        user = await self.get_user_by_email(email, session)

        return True if user is not None else False

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.password_hash = generate_passwd_hash(
            user_data_dict["password"])

        session.add(new_user)

        await session.commit()

        return new_user

    async def update_user(self, user: User, user_data: dict, session: AsyncSession):

        for k, v in user_data.items():
            setattr(user, k, v)

        await session.commit()

        return user
