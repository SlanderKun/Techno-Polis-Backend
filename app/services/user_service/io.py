from typing import Any
import sqlalchemy.ext.asyncio
import services.user_service.models


async def update_user_field(
    db: sqlalchemy.ext.asyncio.AsyncSession,
    user_id: int,
    field: str,
    value: Any,
):
    """Обновляет любое поле пользователя."""
    result = await db.execute(
        sqlalchemy.select(services.user_service.models.User).where(
            services.user_service.models.User.id == user_id
        )
    )
    user = result.scalar_one_or_none()
    if not user:
        return None

    setattr(user, field, value)
    await db.commit()
    await db.refresh(user)
    return user


async def set_user_status(db, user_id, status):
    return await update_user_field(db, user_id, "status", status)


async def set_user_role(db, user_id, role):
    return await update_user_field(db, user_id, "role", role)


async def set_user_external_id(db, user_id, external_id):
    return await update_user_field(db, user_id, "external_id", external_id)
