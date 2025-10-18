from utils.linked_settings import base_settings
import importlib
import pkgutil


def load_settings():
    package_name = "settings"
    package = importlib.import_module(package_name)
    package_path = package.__path__

    for _, module_name, _ in pkgutil.iter_modules(package_path):
        importlib.import_module(f"{package_name}.{module_name}")

    class SettingsLoader:
        def __init__(self):
            for cls in base_settings.BaseSettings.registry:
                module_name = cls.__module__.split(".")[-1]
                setattr(self, module_name, cls())

    return SettingsLoader()
