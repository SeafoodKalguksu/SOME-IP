# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

from service_id import ServiceID
from method_id import MethodID


class MessageID:
    def __init__(self) -> None:
        self.service_id: ServiceID = None
        self.method_id: MethodID = None

    def get_service_id(self) -> ServiceID:
        return self.service_id

    def set_service_id(self, id: ServiceID) -> None:
        self.servie_id = id

    def get_method_id(self) -> MethodID:
        return self.method_id

    def set_method_id(self, id: MethodID) -> None:
        self.method_id = id
