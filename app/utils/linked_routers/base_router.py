import typing
import fastapi


class BaseRouter:
    registry: typing.List[fastapi.APIRouter] = []

    @classmethod
    def include_router(cls, router: fastapi.APIRouter):
        cls.registry.append(router)


def create_router_type(parent_class: typing.Type) -> typing.Type:
    class CustomRouter(parent_class):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            BaseRouter.include_router(self)

    return CustomRouter
