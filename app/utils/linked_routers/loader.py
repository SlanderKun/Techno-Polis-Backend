import importlib
import pathlib
import sys


def load_all_service_routers(root_package: str = "services"):
    root_path = (
        pathlib.Path(__file__).resolve().parent.parent.parent / root_package
    )
    for path in root_path.glob("*/router.py"):
        relative = path.relative_to(root_path.parent)
        module = ".".join(relative.with_suffix("").parts)
        if module not in sys.modules:
            importlib.import_module(module)
