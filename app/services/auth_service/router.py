import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router
import services.auth_service.shemas


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.post("/register", tags=["Register"])
async def register_endpoint(
    data: services.auth_service.shemas.RegisterRequestSchema,
):
    return {"status": "ok"}


@router.post("/login", tags=["Login"])
async def login_endpoint(
    data: services.auth_service.shemas.LoginRequestSchema,
):
    return {"status": "ok"}
