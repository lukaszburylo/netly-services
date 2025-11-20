import pkgutil
import importlib
import inspect
import os
from .BaseService import BaseService

__all__ = []
SERVICES = {}  # map: service_name -> service class

_pkg_path = os.path.dirname(__file__)
_package = __package__ if __package__ else __name__

for _finder, module_name, _ispkg in pkgutil.iter_modules([_pkg_path]):
    # pomiń pliki specjalne
    if module_name.startswith("_"):
        continue
    try:
        module = importlib.import_module(f"{_package}.{module_name}")
    except Exception:
        # pomiń moduły które nie dają się zaimportować
        continue
    __all__.append(module_name)
    # znajdź klasy będące usługami
    for _, obj in inspect.getmembers(module, inspect.isclass):
        if obj is BaseService:
            continue
        try:
            if issubclass(obj, BaseService):
                # oczekujemy, że klasa ma statyczną/metodę get_service_name()
                try:
                    name = obj.get_service_name()
                except Exception:
                    continue
                SERVICES[name] = obj
        except TypeError:
            # obj nie jest klasą lub nie można sprawdzić issubclass
            continue
