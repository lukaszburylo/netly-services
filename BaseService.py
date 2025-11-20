from abc import ABC, abstractmethod
from ..Helpers.ResponseTemplate import ResponseTemplate


class BaseService(ABC):
    @staticmethod
    @abstractmethod
    def get_service_name() -> str: ...

    @staticmethod
    @abstractmethod
    def get_data(parameters: str = None) -> ResponseTemplate: ...
