import faststream.rabbit.fastapi
import utils.linked_routers.base_router

FastStreamRouter = utils.linked_routers.base_router.create_router_type(
    faststream.rabbit.fastapi.RabbitRouter
)
