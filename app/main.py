import fastapi
import fastapi.middleware.cors
import utils.linked_routers

app = fastapi.FastAPI()

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
)

utils.linked_routers.load_all_service_routers()

for router in utils.linked_routers.BaseRouter.registry:
    app.include_router(router)
