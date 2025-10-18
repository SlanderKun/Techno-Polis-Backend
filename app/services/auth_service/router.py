import fastapi
import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router
import services.auth_service.shemas
import services.auth_service.logic
import services.auth_service.io


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
    tags=["Register"],
)
async def register_endpoint(
    data: services.auth_service.shemas.RegisterRequestSchema,
):
    if not services.auth_service.logic.validate_password(data.password):
        return fastapi.HTTPException(
            status_code=400, detail="Password does not meet criteria"
        )
    if await services.auth_service.io.email_exists(data.email):
        return fastapi.HTTPException(
            status_code=400, detail="Email already registered"
        )
    await services.auth_service.logic.create_account(data)
    return services.auth_service.shemas.RegisterResponse(
        status="ok", detail="User registered successfully"
    )


@router.post("/login", tags=["Login"])
async def login_endpoint(
    data: services.auth_service.shemas.LoginRequestSchema,
):
    return {"status": "ok"}
