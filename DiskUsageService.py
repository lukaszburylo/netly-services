from .BaseService import BaseService
from Helpers.ResponseTemplate import ResponseTemplate
import shutil


class DiskUsageService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "disk_usage"

    @staticmethod
    def get_data(input_data: str | None) -> str:
        return ResponseTemplate(
            service_name=DiskUsageService.get_service_name(),
            result_status=True,
            output_data=DiskUsageService.__get_disk_usage(),
        )

    @staticmethod
    def __get_disk_usage() -> str:
        total, used, free = shutil.disk_usage("/")
        response = dict()
        response["total"] = total // (2**30)
        response["used"] = used // (2**30)
        response["free"] = free // (2**30)
        response["unit"] = "GB"
        return response
