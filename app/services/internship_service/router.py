import random
import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router
import services.internship_service.shemas


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.get(
    "/internship/list",
    response_model=services.internship_service.shemas.InternshipListResponse,
    tags=["Internship"],
)
async def get_all_internship():
    return services.internship_service.shemas.InternshipListResponse(
        status="ok",
        details=None,
        internships=[
            services.internship_service.shemas.InternshipData(
                owner=1,
                name="Энерго-коуч 3 разряда",
                logo=None,
                company_name="Синергия Дубай",
                platform="Микрон",
                speciality="Энерго-коуч",
                responsibilities="Быть вайбовым, порядочным, подходить под ауру коллектива",
                requirements="Диплом, Сертификат",
                official_employment=None,
                work_shedule=None,
                work_place="Коуч плейсах",
                map_place="Moscow City",
                probation=None,
                salary="Энергией",
                extra="Хотелось бы, чтобы коуч был по ЗЗ Девой, по опыту коллектива, самый топ",
                text_promo="#freeblinovskaya",
                web_link="https://max.ru",
                promo_link="https://max.ru",
                confidencial=True,
                mailings=True,
                sms_ad=True,
            )
        ]*random.randint(1, 10),
    )


# async def can_create_company(
#     db, user: services.user_service.models.User
# ) -> bool:
#     """Проверяет, может ли пользователь создавать компанию."""
#     return (
#         (user.role == services.user_service.models.UserRole.admin)
#         and (user.status == services.user_service.models.UserStatus.active)
#     ) or (
#         (user.role is None)
#         and (user.status == services.user_service.models.UserStatus.pending)
#     )


# async def can_read_company(
#     db, user: services.user_service.models.User
# ) -> bool:
#     """Проверяет, может ли пользователь читать информацию о компании."""
#     return (
#         (user.role == services.user_service.models.UserRole.admin)
#         and (user.status == services.user_service.models.UserStatus.active)
#     ) or (
#         (user.role == services.user_service.models.UserRole.company)
#         and (user.status == services.user_service.models.UserStatus.active)
#     )


# async def can_update_company(
#     db, user: services.user_service.models.User
# ) -> bool:
#     """Проверяет, может ли пользователь обновлять информацию о компании."""
#     return (user.role == services.user_service.models.UserRole.admin) and (
#         user.status == services.user_service.models.UserStatus.active
#     )


# async def can_delete_company(
#     db, user: services.user_service.models.User
# ) -> bool:
#     """Проверяет, может ли пользователь удалять компанию."""
#     return (user.role == services.user_service.models.UserRole.admin) and (
#         user.status == services.user_service.models.UserStatus.active
#     )


# @router.post(
#     "/company/create/",
#     response_model=services.company_service.shemas.CompanyUpdateSchema,
#     tags=["Company"],
# )
# async def create_company(
#     data: services.company_service.shemas.CompanyCreateSchema,
#     session_token: str = fastapi.Header(...),
#     db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
#         database.core.get_db
#     ),
# ):
#     user = await services.auth_service.io.get_user_from_token(
#         session_token,
#         db,
#     )
#     if not await can_create_company(db, user):
#         raise fastapi.HTTPException(
#             status_code=403,
#             detail="User is not allowed to create a company",
#         )
#     company: services.company_service.models.CompanyInfo = (
#         await services.company_service.io.create_company(
#             data,
#             db,
#         )
#     )
#     return company


# @router.get(
#     "/company/read/{{company_id}}/",
#     response_model=services.company_service.shemas.CompanyUpdateSchema,
#     tags=["Company"],
# )
# async def read_company(
#     company_id: int,
#     session_token: str = fastapi.Header(...),
#     db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
#         database.core.get_db
#     ),
# ):
#     user = await services.auth_service.io.get_user_from_token(
#         session_token,
#         db,
#     )
#     if not await can_read_company(db, user):
#         raise fastapi.HTTPException(
#             status_code=403,
#             detail="User is not allowed to read a company",
#         )
#     company: services.company_service.models.CompanyInfo = (
#         await database.io.base_old.get_object_by_id(
#             id=company_id,
#             object_class=services.company_service.models.CompanyInfo,
#         )
#     )
#     return company


# @router.put(
#     "/company/update/",
#     response_model=services.company_service.shemas.CompanyUpdateSchema,
#     tags=["Company"],
# )
# async def update_company(
#     data: services.company_service.shemas.CompanyUpdateSchema,
#     session_token: str = fastapi.Header(...),
#     db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
#         database.core.get_db
#     ),
# ):
#     user = await services.auth_service.io.get_user_from_token(
#         session_token,
#         db,
#     )
#     if not await can_update_company(db, user):
#         raise fastapi.HTTPException(
#             status_code=403,
#             detail="User is not allowed to create a company",
#         )
#     company: services.company_service.models.CompanyInfo = (
#         await services.company_service.io.update_company(
#             data,
#             db,
#         )
#     )
#     return company


# @router.delete(
#     "/company/delete/{{company_id}}/",
#     tags=["Company"],
# )
# async def delete_company(
#     company_id: int,
#     session_token: str = fastapi.Header(...),
#     db: sqlalchemy.ext.asyncio.AsyncSession = fastapi.Depends(
#         database.core.get_db
#     ),
# ):
#     user = await services.auth_service.io.get_user_from_token(
#         session_token,
#         db,
#     )
#     if not await can_read_company(db, user):
#         raise fastapi.HTTPException(
#             status_code=403,
#             detail="User is not allowed to read a company",
#         )
#     await services.company_service.io.delete_company(
#         company_id,
#         db,
#     )
#     return {
#         "status": "ok",
#         "detail": f"Company with id {company_id} has been deleted",
#     }
