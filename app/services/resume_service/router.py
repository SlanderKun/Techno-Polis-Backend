import config
import database.core
import database.io.base_old
import fastapi
import faststream.rabbit.fastapi
import services.auth_service.io
import services.user_service.io
import services.user_service.models
import sqlalchemy.ext.asyncio
import utils.linked_routers.faststream_router
import services.resume_service.io
import services.resume_service.models
import services.resume_service.shemas


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


async def can_create_resume(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь создавать резюме."""
    return True


async def can_read_resume(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь читать информацию о резюме."""
    return (
        (user.role == services.user_service.models.UserRole.admin)
        and (user.status == services.user_service.models.UserStatus.active)
    ) or (
        (user.role == services.user_service.models.UserRole.company)
        and (user.status == services.user_service.models.UserStatus.active)
    )


async def can_update_resume(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь обновлять информацию о резюме."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


async def can_delete_resume(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь удалять резюме."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


@router.post(
    "/resume/create/",
    response_model=services.resume_service.shemas.ResumeInfoResponse,
    tags=["Resume"],
)
async def create_resume(
    data: services.resume_service.shemas.ResumeCreateInfo,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_create_resume(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to create a resume",
        )
    resume: services.resume_service.models.Resume = (
        await services.resume_service.io.create_resume(
            data,
            db,
        )
    )
    return services.resume_service.shemas.ResumeInfoResponse(
        status="ok",
        details=None,
        resume=resume,
    )


@router.get(
    "/resume/info/",
    response_model=services.resume_service.shemas.ResumeInfoResponse,
    tags=["Resume"],
)
async def read_resume(
    resume_id: int,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_read_resume(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to read a resume",
        )
    resume: services.resume_service.models.Resume = (
        await database.io.base_old.get_object_by_id(
            id=resume_id,
            object_class=services.resume_service.models.Resume,
        )
    )
    return services.resume_service.shemas.ResumeInfoResponse(
        status="ok",
        details=None,
        resume=resume,
    )


@router.put(
    "/resume/update/",
    response_model=services.resume_service.shemas.ResumeInfoResponse,
    tags=["Resume"],
)
async def update_resume(
    data: services.resume_service.shemas.ResumeUpdate,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_update_resume(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to create a resume",
        )
    resume: services.resume_service.models.Resume = (
        await services.resume_service.io.update_resume(
            data,
            db,
        )
    )
    return services.resume_service.shemas.ResumeInfoResponse(
        status="ok",
        details=None,
        resume=resume,
    )


@router.delete(
    "/resume/delete/{{resume_id}}/",
    response_model=services.resume_service.shemas.ResumeInfoResponse,
    tags=["Resume"],
)
async def delete_resume(
    resume_id: int,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_delete_resume(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to read a resume",
        )
    await services.resume_service.io.delete_resume(
        resume_id,
        db,
    )
    return services.resume_service.shemas.ResumeInfoResponse(
        status="ok",
        detail=f"Resume with id {resume_id} has been deleted",
        resume=None,
    )
