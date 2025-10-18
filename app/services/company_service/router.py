import services.company_service.models
import fastapi
import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router
import database.core
import services.company_service.io
import services.company_service.shemas
import services.auth_service.io
import services.user_service.models
import sqlalchemy.ext.asyncio
import services.user_service.io


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


async def can_create_company(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь создавать компанию."""
    return (
        (user.role == services.user_service.models.UserRole.admin)
        and (user.status == services.user_service.models.UserStatus.active)
    ) or (
        (user.role is None)
        and (user.status == services.user_service.models.UserStatus.pending)
    )


async def can_read_company(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь читать информацию о компании."""
    return (
        (user.role == services.user_service.models.UserRole.admin)
        and (user.status == services.user_service.models.UserStatus.active)
    ) or (
        (user.role == services.user_service.models.UserRole.company)
        and (user.status == services.user_service.models.UserStatus.active)
    )


async def can_update_company(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь обновлять информацию о компании."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


async def can_delete_company(
    db, user: services.user_service.models.User
) -> bool:
    """Проверяет, может ли пользователь удалять компанию."""
    return (user.role == services.user_service.models.UserRole.admin) and (
        user.status == services.user_service.models.UserStatus.active
    )


@router.post(
    "/company/create/",
    response_model=services.company_service.shemas.CompanyUpdateSchema,
    tags=["Company"],
)
async def create_company(
    data: services.company_service.shemas.CompanyCreateSchema,
    session_token: str = fastapi.Header(...),
    db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
        database.core.get_db
    ),
):
    user = await services.auth_service.io.get_user_from_token(
        session_token,
        db,
    )
    if not await can_create_company(db, user):
        raise fastapi.HTTPException(
            status_code=403,
            detail="User is not allowed to create a company",
        )
    company: services.company_service.models.CompanyInfo = (
        await services.company_service.io.create_company(
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
