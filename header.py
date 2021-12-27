from header_fields.message_id.message_id import MessageID
from header_fields.request_id.request_id import RequestID
from header_fields.protocol_version import ProtocolVersion
from header_fields.interface_version import InterfaceVersion
from header_fields.message_type import MessageType
from header_fields.request_id.session_id import SessionID
from header_fields.return_code import ReturnCode


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

    HEADER_SIZE = 16
    MAX_PAYLOAD_SIZE = 3 * (2 ** 10)  # 3KB
    MAX_PACKET_LENGTH: int = HEADER_SIZE + MAX_PAYLOAD_SIZE

    def __init__(self) -> None:
        """
        Initialize a header
        """
        # 1. MessageID [32 bit]f
        self.msg_id: MessageID = None

        # 2. Length [32 bit]
        # Header size is 16 bytes
        # Max size for Payload is 3K bytes
        self.length: int = None

        # 3. RequestID [32 bit]
        self.request_id: RequestID = None

        # 4. Protocol Version [8 bit]
        self.protocol_version: ProtocolVersion = None

        # 5. Interface Version [8 bit]
        self.interface_version: InterfaceVersion = None

        # 6. Message Type [8] bit]
        self.message_type: MessageType = None

        # 7. Return Code [8 bit]
        self.return_code: ReturnCode = None

    def get_message_id(self) -> MessageID:
        pass

    def set_message_id(self, id: MessageID) -> None:
        pass

    def get_length(self) -> int:
        """
        get length of packet
        """
        return self.length

    def set_length(self, packet_length: int = 0):
        """
        set length of packet
        """
        try:
            if packet_length > self.MAX_PACKET_LENGTH:
                raise Exception(
                    "length should not be greater than {self.MAX_PACKET_LENGTH} bytes."
                )
            elif packet_length < self.HEADER_SIZE:
                raise Exception("length should be less than HEADER_SIZE.")
        except Exception as e:
            print(e)
        else:
            self.length = packet_length

    def get_request_id(self) -> RequestID:
        pass

    def set_request_id(self, id: RequestID) -> None:
        pass

    def get_session_id(self) -> SessionID:
        pass

    def set_session_id(self, id: SessionID) -> None:
        pass

    def get_interface_version(self) -> InterfaceVersion:
        pass

    def set_interface_version(self, version: InterfaceVersion) -> None:
        pass

    def set_message_type(self, type: MessageType):
        self.message_type = type

    def get_message_type(self) -> MessageType:
        return self.message_type

    def set_return_code(self, code: ReturnCode) -> None:
        self.return_code = code

    def get_return_code(self) -> ReturnCode:
        return self.return_code

    def get_header_size(self) -> int:
        return self.HEADER_SIZE

    def get_max_payload_size(self) -> int:
        return self.MAX_PAYLOAD_SIZE
