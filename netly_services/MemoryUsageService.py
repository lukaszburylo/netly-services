"""Memory Usage Service"""

import time
from typing import Optional, Dict, Any, Tuple

import psutil

from netly_shared import ServiceResult, Status
from .BaseService import BaseService


class MemoryUsageService(BaseService):
    """Memory Usage Service"""

    @staticmethod
    def get_service_name() -> str:
        return "memory_usage"

    @staticmethod
    def get_data(parameters: Optional[Dict[str, Any]]) -> ServiceResult:
        start = time.perf_counter_ns()
        result, output, metadata = MemoryUsageService.__get_memory_usage(parameters)
        end = time.perf_counter_ns()

        return ServiceResult(
            service_name=MemoryUsageService.get_service_name(),
            status=Status.SUCCESS if result is True else Status.FAILED,
            parameters_used=parameters,
            output=output,
            execution_time_ns=end - start,
            metadata=metadata,
        )

    @staticmethod
    def __get_memory_usage(
        parameters: Optional[Dict[str, Any]],  # pylint: disable=unused-argument
    ) -> Tuple[bool, Optional[str], Dict[str, Any]]:
        memory = psutil.virtual_memory()
        metadata = {
            "total": f"{memory.total / (1024 ** 3):.2f}",
            "used": f"{memory.used / (1024 ** 3):.2f}",
            "free": f"{memory.free / (1024 ** 3):.2f}",
            "unit": "GB",
        }
        return True, None, metadata
