import database.core
import services.auth_service.models
import services.user_service.models
import sqlalchemy
import sqlalchemy.ext.asyncio


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


async def create_session_token(
    user_id: int,
    session_token: str = None,
    location: str = "default",
) -> str:
    """Создаёт сессионный токен для пользователя и
    сохраняет его в базе данных."""
    async with database.core.async_session_factory() as session:
        user_session = services.auth_service.models.Session(
            user_id=user_id,
            key=session_token,
            location=location,
        )
        session.add(user_session)
        await session.commit()
    return session_token


async def session_token_exists(session_token: str) -> bool:
    """Проверяет, существует ли сессионный токен в базе данных."""
    async with database.core.async_session_factory() as session:
        result = await session.execute(
            sqlalchemy.select(services.auth_service.models.Session).where(
                services.auth_service.models.Session.key == session_token
            )
        )
        user_session = result.scalar_one_or_none()
        return user_session is not None


async def get_user_by_session_token(
    session_token: str,
) -> services.user_service.models.User | None:
    """Возвращает пользователя по сессионному токену."""
    async with database.core.async_session_factory() as session:
        result = await session.execute(
            sqlalchemy.select(services.auth_service.models.Session).where(
                services.auth_service.models.Session.key == session_token
            )
        )
        user_session = result.scalar_one_or_none()
        if user_session is None:
            return None
        result = await session.execute(
            sqlalchemy.select(services.user_service.models.User).where(
                services.user_service.models.User.id == user_session.user_id
            )
        )
        user = result.scalar_one_or_none()
        return user


async def get_user_from_token(
    session_token: str,
    db: sqlalchemy.ext.asyncio.AsyncSession,
) -> services.user_service.models.User | None:
    """Возвращает пользователя по сессионному токену."""
    result = await db.execute(
        sqlalchemy.select(services.auth_service.models.Session).where(
            services.auth_service.models.Session.key == session_token
        )
    )
    user_session = result.scalar_one_or_none()
    if not user_session:
        return None
    result = await db.execute(
        sqlalchemy.select(services.user_service.models.User).where(
            services.user_service.models.User.id == user_session.user_id
        )
    )
    user = result.scalar_one_or_none()
    return user
