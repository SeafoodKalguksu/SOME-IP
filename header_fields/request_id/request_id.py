# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from typing import Tuple
from client_id import ClientID
from session_id import SessionID


class RequestID:
    def __init__(
        self,
        client_id: int = ClientID.DEFAULT,
        session_id: int = SessionID.DEFAULT,
    ) -> None:
        self.client_id: ClientID = None
        self.session_id: SessionID = None

    def get_client_id(self) -> ClientID:
        return self.client_id

    def set_client_id(self, id: ClientID) -> None:
        self.client_id = id

    def get_session_id(self) -> SessionID:
        return self.session_id

    def set_session_id(self, id: SessionID) -> None:
        self.session_id = id
