import typing
import pydantic_settings


class BaseSettings(pydantic_settings.BaseSettings):
    registry: typing.ClassVar[typing.List[typing.Type["BaseSettings"]]] = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls is not BaseSettings:
            BaseSettings.registry.append(cls)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
