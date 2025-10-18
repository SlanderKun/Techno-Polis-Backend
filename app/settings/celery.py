import utils.linked_settings.base_settings


class Settings(utils.linked_settings.base_settings.BaseSettings):
    CELERY_RESULT_BACKEND: str
