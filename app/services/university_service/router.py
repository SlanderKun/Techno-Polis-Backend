import config
import database.core
import database.io.base_old
import fastapi
import faststream.rabbit.fastapi
import services.auth_service.io
import services.company_service.models
import services.university_service.io
import services.university_service.models
import services.university_service.shemas
import services.user_service.models
import sqlalchemy.ext.asyncio
import utils.linked_routers.faststream_router

router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


async def can_create_university(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь создавать университет."""
    return (
        (user.role == services.user_service.models.UserRole.admin)
        and (user.status == services.user_service.models.UserStatus.active)
    ) or (
        (user.role is None)
        and (user.status == services.user_service.models.UserStatus.pending)
    )


async def can_read_university(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь читать информацию о университетах."""
    return (
        (user.role == services.user_service.models.UserRole.admin)
        and (user.status == services.user_service.models.UserStatus.active)
    ) or (
        (user.role == services.user_service.models.UserRole.university)
        and (user.status == services.user_service.models.UserStatus.active)
    )


async def can_update_university(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь обновлять информацию о университетах."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


async def can_delete_university(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь удалять университеты."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


@router.post(
    "/university/create/",
    response_model=services.university_service.shemas.UniversityUpdateSchema,
    tags=["University"],
)
async def create_university(
    data: services.university_service.shemas.UniversityCreateSchema,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_create_university(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to create a university",
        )
    company: services.company_service.models.CompanyInfo = (
        await services.university_service.io.create_university(
            data,
            db,
        )
    )
    # await services.user_service.io.set_user_role(
    #     db,
    #     user.id,
    #     services.user_service.models.UserRole.company,
    # )
    # await services.user_service.io.set_user_status(
    #     db,
    #     user.id,
    #     services.user_service.models.UserStatus.active,
    # )
    # await services.user_service.io.set_user_external_id(
    #     db,
    #     user.id,
    #     company.id,
    # )
    return company


@router.get(
    "/university/info/",
    response_model=services.university_service.shemas.UniversityUpdateSchema,
    tags=["University"],
)
async def read_university(
    company_id: int,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_read_university(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to read a university",
        )
    company: services.company_service.models.CompanyInfo = (
        await database.io.base_old.get_object_by_id(
            id=company_id,
            object_class=services.university_service.models.UniversityInfo,
        )
    )
    return company


@router.put(
    "/university/update/",
    response_model=services.university_service.shemas.UniversityUpdateSchema,
    tags=["University"],
)
async def update_university(
    data: services.university_service.shemas.UniversityUpdateSchema,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_update_university(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to create a university",
        )
    company: services.company_service.models.CompanyInfo = (
        await services.university_service.io.update_university(
            data,
            db,
        )
    )
    return company


@router.delete(
    "/university/delete/{{university_id}}/",
    tags=["University"],
)
async def delete_university(
    university_id: int,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_read_university(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to read a university",
        )
    await services.university_service.io.delete_university(
        university_id,
        db,
    )
    return {
        "status": "ok",
        "detail": f"University with id {university_id} has been deleted",
    }
