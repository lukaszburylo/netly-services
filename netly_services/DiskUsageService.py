"""Disk Usage Service"""

import shutil
import time

from typing import Optional, Dict, Any, Tuple
from netly_shared import ServiceResult, Status

from .BaseService import BaseService


class DiskUsageService(BaseService):
    """Service to get disk usage statistics."""
    @staticmethod
    def get_service_name() -> str:
        return "disk_usage"

    @staticmethod
    def get_data(parameters: Optional[Dict[str, Any]]) -> ServiceResult:
        start = time.perf_counter_ns()
        result, output, metadata = DiskUsageService.__get_disk_usage(parameters)
        end = time.perf_counter_ns()

        return ServiceResult(
            service_name=DiskUsageService.get_service_name(),
            status=Status.SUCCESS if result is True else Status.FAILED,
            parameters_used=parameters,
            output=output,
            execution_time_ns=end - start,
            metadata=metadata,
        )

    @staticmethod
    def __get_disk_usage(
        parameters: Optional[Dict[str, Any]],
    ) -> Tuple[bool, Optional[str], Dict[str, Any]]:
        result = True
        output = None
        metadata = {}
        try:
            total, used, free = shutil.disk_usage(
                (parameters or {}).get("mount_point", "/")
            )
            metadata["total"] = total // (2**30)
            metadata["used"] = used // (2**30)
            metadata["free"] = free // (2**30)
            metadata["unit"] = "GB"
        except FileNotFoundError as e:
            result = False
            output = str(e)
        return result, output, metadata
