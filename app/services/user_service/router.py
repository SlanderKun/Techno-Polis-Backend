import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url
    )
)


@router.get("/user", tags=["User Info"])
async def health_check():
    return {"status": "ok"}
