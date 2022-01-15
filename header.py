"""
Header for SOME/IP
"""

from header_fields.message_id import MessageID
from header_fields.request_id import RequestID
from header_fields.protocol_version import ProtocolVersion
from header_fields.interface_version import InterfaceVersion
from header_fields.message_type import MessageType
from header_fields.return_code import ReturnCode

from length_info import LengthInfo


class Header:
    """
    <<--------------------------------32 bit---------------------------------->>
    |--------------------------------------------------------------------------|
    |       Message ID (Service ID [16 bit] / Method ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    |              Length(= Header size + Payload size) [32bit]                |
    |--------------------------------------------------------------------------|
    |       Request ID (Client ID [16 bit] / Session ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    | Protocol Ver.[8 bit] IF. Ver.[8 bit] Msg. Type[8 bit] Return Code [8 bit]|
    |--------------------------------------------------------------------------|
    |                   Payload [variable size: up to 3KB]                     |
    |--------------------------------------------------------------------------|
    """

    def __init__(self) -> None:
        """
        Initialize a header
        """
        # 1. MessageID [32 bit]f
        self.message_id: MessageID = MessageID()

        # 2. Length [32 bit]
        # Header size is 16 bytes
        # Payload size is up to 3KB
        # 'length' means the size of the packet
        self.length: int | None = None

        # 3. RequestID [32 bit]
        self.request_id: RequestID = RequestID()

        # 4. Protocol Version [8 bit]
        self.protocol_version: ProtocolVersion | None = None

        # 5. Interface Version [8 bit]
        self.interface_version: InterfaceVersion | None = None

        # 6. Message Type [8 bit]
        self.message_type: MessageType | None = None

        # 7. Return Code [8 bit]
        self.return_code: ReturnCode | None = None

    def get_message_id(self) -> MessageID:
        return self.message_id

    def set_message_id(self, message_id: MessageID) -> None:
        self.message_id = message_id

    def get_length(self) -> int | None:
        """
        get length of packet
        """
        return self.length

    def set_length(self, packet_length: int):
        """
        set length of packet
        """
        try:
            if packet_length > LengthInfo.MAX_PACKET_LENGTH:
                raise Exception(
                    "length should not be greater than {self.MAX_PACKET_LENGTH} bytes."
                )
            elif packet_length <= LengthInfo.HEADER_SIZE:
                raise Exception("length should be greater than HEADER_SIZE.")
        except Exception as e:
            print(e)
        else:
            self.length = packet_length

    def get_request_id(self) -> RequestID:
        return self.request_id

    def set_request_id(self, request_id: RequestID) -> None:
        self.request_id = request_id

    def get_protocol_version(self) -> ProtocolVersion:
        return self.protocol_version

    def set_protocol_version(self, version: ProtocolVersion) -> None:
        self.protocol_version = version

    def get_interface_version(self) -> InterfaceVersion:
        return self.interface_version

    def set_interface_version(self, version: InterfaceVersion) -> None:
        self.interface_version = version

    def get_message_type(self) -> MessageType:
        return self.message_type

    def set_message_type(self, type: MessageType):
        self.message_type = type

    def get_return_code(self) -> ReturnCode:
        return self.return_code

    def set_return_code(self, code: ReturnCode) -> None:
        self.return_code = code
