# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import Tuple

from service_id import ServiceID
from method_id import MethodID


class MessageID:
    def __init__(
        self,
        service_id: int = ServiceID.DEFAULT,
        method_id: int = MethodID.DEFAULT,
    ) -> None:
        self._msg_id: Tuple[int, int] = (service_id, method_id)

    def get_msg_id(self) -> Tuple[int, int]:
        return self._msg_id
