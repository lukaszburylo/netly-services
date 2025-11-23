"""BaseService class"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

from netly_shared import ServiceResult


class BaseService(ABC):
    """BaseService class"""

    @staticmethod
    @abstractmethod
    def get_service_name() -> str:
        """Return service name"""

    @staticmethod
    @abstractmethod
    def get_data(parameters: Optional[Dict[str, Any]]) -> ServiceResult:
        """get_data"""
