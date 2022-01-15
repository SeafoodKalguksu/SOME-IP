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
        self.client_id: ClientID | None = None
        self.session_id: SessionID | None = None

    def get_client_id(self) -> ClientID | None:
        return self.client_id

    def set_client_id(self, client_id: ClientID) -> None:
        self.client_id = client_id

    def get_session_id(self) -> SessionID | None:
        return self.session_id

    def set_session_id(self, session_id: SessionID) -> None:
        self.session_id = session_id
