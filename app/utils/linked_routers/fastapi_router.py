import fastapi
import utils.linked_routers.base_router

FastAPIRouter = utils.linked_routers.base_router.create_router_type(
    fastapi.APIRouter
)
