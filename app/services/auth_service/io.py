import sqlalchemy
import database.core
import services.user_service.models


async def create_user(
    email: str,
    password_hash: str,
):
    """Сохраняет пользователя в базе данных."""
    async with database.core.async_session_factory() as session:
        user = services.user_service.models.User(
            email=email,
            password_hash=password_hash,
        )
        session.add(user)
        await session.commit()


async def email_exists(email: str) -> bool:
    """Проверяет, существует ли пользователь с таким email."""
    async with database.core.async_session_factory() as session:
        result = await session.execute(
            sqlalchemy.select(services.user_service.models.User).where(
                services.user_service.models.User.email == email
            )
        )
        user = result.scalar_one_or_none()
        return user is not None
