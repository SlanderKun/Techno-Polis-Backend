import random
import fastapi
import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router
import services.user_service.shemas
import services.auth_service.io
import services.user_service.models


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.get(
    "/user/info",
    response_model=services.user_service.shemas.UserInfoResponse,
    tags=["User Info"],
)
async def user_info(
    session_token: str = fastapi.Header(...),
):
    user: services.user_service.models.User = (
        await services.auth_service.io.get_user_by_session_token(
            session_token=session_token,
        )
    )
    if user is None:
        return services.user_service.shemas.UserInfoResponse(
            status="error",
            details="Unauthorize",
            data=None,
        )
    additional_info = None
    # if user.role == services.user_service.models.UserRole.company:
    #     company = await services.company_service.io.get_company_by_user_id(
    #         user_id=user.id,
    #     )
    #     if company is not None:
    #         additional_info = company
    # elif user.role == services.user_service.models.UserRole.university:
    #     university = (
    #         await services.university_service.io.get_representative_by_user_id(
    #             user_id=user.id,
    #         )
    #     )
    #     if university is not None:
    #         additional_info = university
    # elif user.role == services.user_service.models.UserRole.admin:
    #     internship_manager = (
    #         await services.internship_manager_service.io.get_internship_manager_by_user_id(
    #             user_id=user.id,
    #         )
    #     )
    #     if internship_manager is not None:
    #         additional_info = internship_manager
    s = [
        "unverified",
        "pending",
        "hr",
        "university",
        "company",
    ]
    status = random.choice(s)
    data = services.user_service.shemas.UserInfoSchema(
        email=user.email,
        status=status,
        representative_name="Михаил",
        representative_surname="Зубенко",
        company_name="Лит-Энерджи",
        logo=None,
        inn="22813371488",
        contact_number="+7 (812) 228-52-52",
        contact_email="mihail@lit.ru",
    )
    return services.user_service.shemas.UserInfoResponse(
        status="ok",
        details=None,
        data=data,
    )
