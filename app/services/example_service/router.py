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


@router.get("/health_2", tags=["Health Check 2"])
async def health_check_2():
    return {"status": "ok"}

@router.get("/health_3", tags=["Health Check 3"])
async def health_check_3():
    return {"status": "ok", "detail": "All systems operational"}