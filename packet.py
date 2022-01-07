# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
AUTOSAR Protocol 'Scalable service-Oriented MiddlewarE over IP(SOME/IP)'
"""

import random

from header import Header
from header_fields.message_id.service_id import ServiceID
from header_fields.message_id.method_id import MethodID
from header_fields.request_id.client_id import ClientID
from header_fields.request_id.session_id import SessionID
from header_fields.interface_version import InterfaceVersion
from header_fields.protocol_version import ProtocolVersion
from header_fields.message_type import MessageType
from header_fields.return_code import ReturnCode

from length_info import LengthInfo


class PacketDirection:
    """
    Direction between a sender and a receiver
    """

    SENDER_TO_RECEIVER = 1
    RECEIVER_TO_SENDER = 2


class Packet:
    """
    SOME/IP Protocol
    """

    def __init__(self) -> None:
        """
        Initialize a packet
        """
        self.header = Header()

        self.payload: bytearray = None

    def get_header(self) -> Header:
        return self.header

    def set_header(self, header: Header) -> None:
        self.header = header

    def get_payload(self) -> bytearray:
        return self.payload

    def set_payload(self, payload: bytearray) -> None:
        self.payload = payload

    def make_payload_data(self, payload_length: int) -> bytes:
        """
        Generate random data for payload
        """
        payload = bytearray(payload_length)

        for index in range(payload_length):
            data = random.randint(1, LengthInfo.ONE_BYTE - 1)
            payload[index] = data

        return payload

    def settings_for_packet(
        self,
        payload_size: int,
        direction: PacketDirection = PacketDirection.SENDER_TO_RECEIVER,
    ) -> None:
        """
        Settings for a Packet instance
        """
        header = self.get_header()

        # Make random data for payload
        self.set_payload(self.make_payload_data(payload_size))

        # 1. Message ID
        header.set_message_id((ServiceID.DEFAULT, MethodID.DEFAULT))

        # 2. Length
        header.set_length(LengthInfo.HEADER_SIZE + payload_size)

        # 3. Request ID
        header.set_request_id((ClientID.DEFAULT, SessionID.DEFAULT))

        # 4. Protocol version
        header.set_protocol_version(ProtocolVersion.DEFAULT)

        # 5. Interface version
        header.set_interface_version(InterfaceVersion.DEFAULT)

        # 6. Message Type
        if direction == PacketDirection.SENDER_TO_RECEIVER:
            header.set_message_type(MessageType.RESPONSE)
        elif direction == PacketDirection.RECEIVER_TO_SENDER:
            header.set_message_type(MessageType.REQUEST)

        # 7. Return code
        header.set_return_code(ReturnCode.DEFAULT)

    def convert_packet_instance_to_bytes(self) -> bytes:
        """
        Convert a packet instance to bytesarray for sending
        """
        length = self.get_header().get_length()

        # Message ID
        service_id, method_id = self.get_header().get_message_id()
        packet_bytes = int(service_id).to_bytes(2, "big")
        packet_bytes += int(method_id).to_bytes(2, "big")

        # Length
        packet_bytes += length.to_bytes(4, "big")

        # Request ID
        client_id, session_id = self.get_header().get_request_id()
        packet_bytes += int(client_id).to_bytes(2, "big")
        packet_bytes += int(session_id).to_bytes(2, "big")

        # Protocol version
        protocol_version = self.get_header().get_protocol_version()
        packet_bytes += int(protocol_version).to_bytes(1, "big")

        # Interface version
        interface_version = self.get_header().get_interface_version()
        packet_bytes += int(interface_version).to_bytes(1, "big")

        # Message type
        message_type = self.get_header().get_message_type()
        packet_bytes += int(message_type).to_bytes(1, "big")

        # Return code
        return_code = self.get_header().get_return_code()
        packet_bytes += int(return_code).to_bytes(1, "big")

        # Payload
        packet_bytes += self.payload

        return packet_bytes

    def debug_info(self, packet_bytes: bytes, direction: str) -> None:
        print(f"-{direction}: start ------------------------------------")
        header_bytes = packet_bytes[: LengthInfo.HEADER_SIZE]

        # Header
        header = int.from_bytes(header_bytes, "big")
        service_id = header >> (LengthInfo.HEADER_SIZE - 2) * 8 & 0xFFFF
        method_id = header >> (LengthInfo.HEADER_SIZE - 4) * 8 & 0xFFFF
        length = header >> (LengthInfo.HEADER_SIZE - 8) * 8 & 0xFFFFFFFF
        client_id = header >> (LengthInfo.HEADER_SIZE - 10) * 8 & 0xFFFF
        session_id = header >> (LengthInfo.HEADER_SIZE - 12) * 8 & 0xFFFF
        protocol_version = header >> (LengthInfo.HEADER_SIZE - 13) * 8 & 0xFF
        interface_version = header >> (LengthInfo.HEADER_SIZE - 14) * 8 & 0xFF
        message_type = header >> (LengthInfo.HEADER_SIZE - 15) * 8 & 0xFF
        return_code = header & 0xFF

        # Payload
        payload = packet_bytes[LengthInfo.HEADER_SIZE :]

        print(f"service_id: {service_id}")
        print(f"method_id: {method_id}")
        print(f"length: {length}")
        print(f"client_id: {client_id}")
        print(f"session_id: {session_id}")
        print(f"protocol: {protocol_version}")
        print(f"interface: {interface_version}")
        print(f"msg type: {message_type}")
        print(f"return code: {return_code}")
        # print(f"payload: {payload}")
        print(f"-{direction}: end --------------------------------------")
