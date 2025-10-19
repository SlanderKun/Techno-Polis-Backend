import config
import database.io.base_old
import fastapi
import faststream.rabbit.fastapi
import services.auth_service.io
import services.auth_service.logic
import services.auth_service.shemas
import services.user_service.models
import utils.linked_routers.faststream_router

router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.post(
    "/register",
    response_model=services.auth_service.shemas.RegisterResponse,
    responses={
        400: {
            "model": services.auth_service.shemas.ErrorResponse,
        }
    },
    tags=["Auth"],
)
async def register_endpoint(
    data: services.auth_service.shemas.RegisterRequestSchema,
):
    if not services.auth_service.logic.validate_password(data.password):
        raise fastapi.HTTPException(
            status_code=400,
            detail={
                "status": "error",
                "detail": "Password does not meet criteria",
            },
        )
    if await services.auth_service.io.email_exists(data.email):
        raise fastapi.HTTPException(
            status_code=400,
            detail={"status": "error", "detail": "Email already registered"},
        )
    await services.auth_service.logic.create_account(data)
    return services.auth_service.shemas.RegisterResponse(
        status="ok", detail="User registered successfully"
    )


@router.post(
    "/login",
    response_model=services.auth_service.shemas.LoginResponse,
    responses={
        400: {
            "model": services.auth_service.shemas.ErrorResponse,
        }
    },
    tags=["Auth"],
)
async def login_endpoint(
    data: services.auth_service.shemas.LoginRequestSchema,
    request: fastapi.Request,
):
    if not (await services.auth_service.io.email_exists(data.email)):
        raise fastapi.HTTPException(
            status_code=400,
            detail={"status": "error", "detail": "Invalid email or password"},
        )
    user: services.user_service.models.User = (
        await database.io.base_old.get_object_by_field(
            object_class=services.user_service.models.User,
            value=data.email,
            field=services.user_service.models.User.email,
        )
    )
    if not services.auth_service.logic.validate_hash_password(
        data.password, user.password_hash
    ):
        raise fastapi.HTTPException(
            status_code=400,
            detail={"status": "error", "detail": "Invalid email or password"},
        )
    location = request.client.host
    location = request.headers.get("X-Forwarded-For", location)
    session_token = await services.auth_service.logic.create_session_token(
        user.id, location
    )
    return services.auth_service.shemas.LoginResponse(
        session_token=session_token,
        status="ok",
        detail="Login successful",
    )
