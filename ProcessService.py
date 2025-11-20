from .BaseService import BaseService
from Helpers.ResponseTemplate import ResponseTemplate
import psutil
import json


class ProcessService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "process"

    @staticmethod
    def get_data(input: str | None) -> str:
        result, data = ProcessService.__get_processes(input)
        return ResponseTemplate(
            service_name=ProcessService.get_service_name(),
            result_status=result,
            input_data=input,
            output_data=data,
        )

    @staticmethod
    def __get_processes(input) -> str:
        #input = json.loads(input)
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                if proc.info["name"] == input.get("process_name"):
                    response = dict()
                    response['pid'] = proc.pid
                    response['name'] = proc.info["name"]
                    return True, response
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                return "False", ""
        return "False", ""
