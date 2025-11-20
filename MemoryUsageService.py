from .BaseService import BaseService
from Helpers.ResponseTemplate import ResponseTemplate
import psutil


class MemoryUsageService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "memory_usage"

    @staticmethod
    def get_data(input_data: str | None) -> str:
        return ResponseTemplate(
            MemoryUsageService.get_service_name(),
            MemoryUsageService.__get_memory_usage(),
        )

    @staticmethod
    def __get_memory_usage() -> str:
        memory = psutil.virtual_memory()
        response = dict()
        response["total"] = f"{memory.total / (1024**3):.2f}"
        response["used"] = f"{memory.used / (1024**3):.2f}"
        response["free"] = f"{memory.free / (1024**3):.2f}"
        response["unit"] = "GB"
        return str(response)
