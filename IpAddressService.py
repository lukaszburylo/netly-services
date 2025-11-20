from .BaseService import BaseService
from Helpers.ResponseTemplate import ResponseTemplate
import socket


class IpAddressService(BaseService):
    @staticmethod
    def get_service_name() -> str:
        return "ip_address"

    @staticmethod
    def get_data(input_data: str = None) -> str:
        return ResponseTemplate(
            IpAddressService.get_service_name(), IpAddressService.__get_ip()
        )

    @staticmethod
    def __get_ip() -> str:
        try:
            # Use a UDP socket to obtain the outbound IP without sending data.
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                # The address doesn't need to be reachable; no packets are sent.
                s.connect(("8.8.8.8", 80))
                return s.getsockname()[0]
        except Exception:
            try:
                hostname = socket.gethostname()
                for ip in socket.gethostbyname_ex(hostname)[2]:
                    if not ip.startswith("127."):
                        return ip
            except Exception:
                pass
        return "127.0.0.1"
