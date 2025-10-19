import fastapi
import fastapi.middleware.cors
import utils.linked_routers

app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

utils.linked_routers.load_all_service_routers()

for router in utils.linked_routers.BaseRouter.registry:
    app.include_router(router)
