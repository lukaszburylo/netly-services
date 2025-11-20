from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def get_service_name(self) -> str:
        pass

    @abstractmethod
    def get_data(self, input_data: str | None) -> str:
        return ""
