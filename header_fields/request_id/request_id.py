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
        self._request_id: Tuple[int, int] = (client_id, session_id)

    def get_request_id(self) -> Tuple[int, int]:
        return self._request_id
