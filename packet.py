# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
AUTOSAR Protocol 'Scalable service-Oriented MiddlewarE over IP(SOME/IP)'
"""

from header import Header


class Packet:
    """
    SOME/IP Protocol
    """

    def __init__(self) -> None:
        """
        Initialize a packet
        """
        self.header = Header()

        # Payload [Variable size is up to 3K]
        self.payload: bytearray = None

        # length = Header(16 bytes) + payload
        # the length info is located in Header
        self._length: int = None

    def get_header(self) -> Header:
        return self.header

    def set_header(self, header: Header) -> None:
        self.header = header

    def get_payload(self) -> bytearray:
        return self.payload

    def set_payload(self, payload: bytearray) -> None:
        self.payload = payload
