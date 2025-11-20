from typing import Tuple
from .BaseService import BaseService
from ..Helpers.ResponseTemplate import ResponseTemplate
import docker


class DockerService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "docker"

    @staticmethod
    def get_data(parameters: str = None) -> ResponseTemplate:
        result, data = DockerService.__get_container(parameters)
        return ResponseTemplate(
            service_name=DockerService.get_service_name(),
            result_status=result,
            input_data=input,
            output_data=data,
        )

    @staticmethod
    def __get_container(parameters) -> Tuple[bool, str]:
        container_name = input.get("container_name")
        try:
            client = docker.from_env()
            container = client.containers.get(container_name)
            if container.status == "running":
                print(f"Container '{container_name}' is running.")
                return True, None
            else:
                return (
                    False,
                    f"Container '{container_name}' is NOT running. Status: {container.status}",
                )
        except docker.errors.NotFound:
            return False, f"Container '{container_name}' does not exist."
        except docker.errors.DockerException:
            return False, "Docker service does not exist."
