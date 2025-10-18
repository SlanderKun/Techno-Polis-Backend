import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok"}
