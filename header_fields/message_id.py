# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Tuple


class ServiceID:
    """
    16 bit
    """

    DEFAULT: int = 0x1001


class MethodID:
    """
    16 bit
    """

    DEFAULT: int = 0x2001


class MessageID:
    """
    (Service ID + Method ID) [32 bit]
    """
    def __init__(self) -> None:
        self.service_id: ServiceID | None = None
        self.method_id: MethodID | None = None

    def get_service_id(self) -> ServiceID | None:
        return self.service_id

    def set_service_id(self, service_id: ServiceID) -> None:
        self.servie_id = service_id

    def get_method_id(self) -> MethodID | None:
        return self.method_id

    def set_method_id(self, method_id: MethodID) -> None:
        self.method_id = method_id
