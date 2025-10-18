import fastapi
import utils.linked_routers

app = fastapi.FastAPI()

utils.linked_routers.load_all_service_routers()

for router in utils.linked_routers.BaseRouter.registry:
    app.include_router(router)
