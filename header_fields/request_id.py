# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from typing import Tuple


class ClientID:
    """
    2 bytes
    """

    DEFAULT = 0x3001


class SessionID:
    """
    2 bytes
    """

    DEFAULT = 0x4001


class RequestID:
    def __init__(self) -> None:
        self.client_id: ClientID = None
        self.session_id: SessionID = None

    def get_request_id(self) -> Tuple[ClientID, SessionID]:
        return self.client_id, self.session_id

    def set_request_id(self, request_id: Tuple[ClientID, SessionID]) -> None:
        self.client_id, self.session_id = request_id
