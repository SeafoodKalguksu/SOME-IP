# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Tuple


class ServiceID:
    """
    2 bytes
    """

    DEFAULT = 0x1001


class MethodID:
    """
    2 bytes
    """

    DEFAULT = 0x2001


class MessageID:
    def __init__(self) -> None:
        self.service_id: ServiceID = None
        self.method_id: MethodID = None

    def get_message_id(self) -> Tuple[ServiceID, MethodID]:
        return self.service_id, self.method_id

    def set_message_id(self, message_id: Tuple[ServiceID, MethodID]) -> None:
        self.servie_id, self.method_id = message_id
