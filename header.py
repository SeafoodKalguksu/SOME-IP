from header_fields.message_id.message_id import MessageID
from header_fields.request_id.request_id import RequestID
from header_fields.protocol_version import ProtocolVersion
from header_fields.interface_version import InterfaceVersion
from header_fields.message_type import MessageType
from header_fields.return_code import ReturnCode


class HeaderForSOMEoverIP:
    """
    <<--------------------------------32 bit---------------------------------->>
    |--------------------------------------------------------------------------|
    |       Message ID (Service ID [16 bit] / Method ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    |                        Length [32 bit]                                   |
    |--------------------------------------------------------------------------|
    |       Request ID (Client ID [16 bit] / Session ID [16 bit]) [32 bit]     |
    |--------------------------------------------------------------------------|
    | Protocol Ver.[8 bit] IF. Ver.[8 bit] Msg. Type[8 bit] Return Code [8 bit]|
    |--------------------------------------------------------------------------|
    |                           Payload [variable size]                        |
    |--------------------------------------------------------------------------|
    """

    HEADER_SIZE = 16
    MAX_PAYLOAD_SIZE = 3 * (2 ** 10)

    def __init__(self) -> None:
        """
        Initialize a header
        """
        # 1. MessageID [32 bit]
        msg_id = MessageID()
        self._msg_id = msg_id.get_msg_id()

        # 2. Length [32 bit]
        # Header size is 16 bytes
        # Max size for Payload is 3K bytes
        self._length: int = 0

        self.MAX_PACKET_LENGTH: int = self.HEADER_SIZE + self.MAX_PAYLOAD_SIZE

        # 3. RequestID [32 bit]
        request_id = RequestID()
        self._request_id = request_id.get_request_id()

        # 4. Protocol Version [8 bit]
        self._protocol_version: int = ProtocolVersion.DEFAULT

        # 5. Interface Version [8 bit]
        self._protocol_version: int = InterfaceVersion.DEFAULT

        # 6. Message Type [8] bit]
        self._message_type: int = None

        # 7. Return Code [8 bit]
        self._return_code: int = None

    def set_message_type(self, type: MessageType):
        self._message_type = type

    def get_message_type(self) -> MessageType:
        return self._message_type

    def set_return_code(self, code: ReturnCode) -> None:
        self._return_code = code

    def get_return_code(self) -> ReturnCode:
        return self._return_code

    def set_packet_length(self, packet_length: int = 0):
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
            self._length = packet_length

    def get_length(self) -> int:
        return self._length
