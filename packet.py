# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
AUTOSAR Protocol 'Scalable service-Oriented MiddlewarE over IP(SOME/IP)'
"""

from typing import List, Tuple
from header import Header


class Packet:
    """
    SOME/IP Protocol
    """

    def __init__(self) -> None:
        """
        Initialize a packet
        """
        self._header = Header()

        # Payload [Variable size is up to 3K]
        self._payload: bytearray = None

        # length = Header(16 bytes) + payload
        # the length info is located in Header
        self._length: int = None

    def get_header(self) -> Header:
        return self._header

    def set_header(self) -> None:
        pass

    def get_payload(self) -> int:
        return self._payload

    def set_payload(self, payload) -> None:
        self._payload = payload
