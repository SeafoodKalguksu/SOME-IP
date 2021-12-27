# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# SOME/IP Protocol Specification

from typing import List, Tuple
from header import HeaderForSOMEoverIP


class PacketForSOMEoverIP:
    """
    AUTOSAR Protocol 'Scalable service-Oriented MiddlewarE over IP(SOME/IP)'
    """

    def __init__(self) -> None:
        """
        Initialize a packet
        """
        self._header = HeaderForSOMEoverIP()

        # Payload [Variable size is up to 3K]
        self._payload: bytearray = None

        # length = HeaderForSOMEoverIP(16 bytes) + payload
        # the length info is located in HeaderForSOMEoverIP
        self._length: int = None

    def init_header() -> None:
        pass

    def get_header(self) -> HeaderForSOMEoverIP:
        return self._header

    def get_payload(self) -> int:
        return self._payload

    def set_payload(self, payload) -> None:
        self._payload = payload
