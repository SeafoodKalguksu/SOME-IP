# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
Server
"""
import socket
import random
import time
import sys
import keyboard  # pip install keyboard

from header_fields.message_id.service_id import ServiceID
from header_fields.message_id.method_id import MethodID
from header_fields.request_id.client_id import ClientID
from header_fields.request_id.session_id import SessionID
from header_fields.interface_version import InterfaceVersion
from header_fields.protocol_version import ProtocolVersion
from header_fields.message_type import MessageType
from header_fields.return_code import ReturnCode

from packet import Packet
from length_info import LengthInfo


class Sender:
    def __init__(self) -> None:
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender_socket.connect(("localhost", 5004))
        # self.file = open("sent_packet.txt", "ab")

    def close(self) -> None:
        # self.file.close()
        self.sender_socket.close()

    # def save_in_file(self, packet_bytes: bytes) -> None:
    #     self.file.write(packet_bytes)

    def settings_for_sending_bytes(self, packet: Packet) -> bytes:
        length = packet.get_header().get_length()
        payoad = packet.get_payload()

        # Message ID
        service_id, method_id = packet.get_header().get_message_id()
        packet_bytes = int(service_id).to_bytes(2, "big")
        packet_bytes += int(method_id).to_bytes(2, "big")

        # Length
        packet_bytes += length.to_bytes(4, "big")

        # Request ID
        client_id, session_id = packet.get_header().get_request_id()
        packet_bytes += int(client_id).to_bytes(2, "big")
        packet_bytes += int(session_id).to_bytes(2, "big")

        # Protocol version
        protocol_version = packet.get_header().get_protocol_version()
        packet_bytes += int(protocol_version).to_bytes(1, "big")

        # Interface version
        interface_version = packet.get_header().get_interface_version()
        packet_bytes += int(interface_version).to_bytes(1, "big")

        # Message type
        message_type = packet.get_header().get_message_type()
        packet_bytes += int(message_type).to_bytes(1, "big")

        # Return code
        return_code = packet.get_header().get_return_code()
        packet_bytes += int(return_code).to_bytes(1, "big")

        # Payload
        packet_bytes += payoad

        print(f"will send, service_id: {service_id}")
        print(f"will send, method_id: {method_id}")
        print(f"will send, length: {length}")
        print(f"will send, client_id: {client_id}")
        print(f"will send, session_id: {session_id}")
        print(f"will send, protocol: {protocol_version}")
        print(f"will send, interface: {interface_version}")
        print(f"will send, msg type: {message_type}")
        print(f"will send, return code: {return_code}")

        return packet_bytes

    def send(self, packet: Packet) -> None:
        packet_bytes = self.settings_for_sending_bytes(packet)
        sent_size = self.sender_socket.send(packet_bytes)
        print(f"sent_size: {sent_size}")
        # self.save_in_file(packet_bytes)

    def receive(self) -> bool:
        message = self.sender_socket.recv(1024)
        if not message:
            return False

        print(message)
        return True

        return True


def get_random_data_for_payload(payload_length: int) -> bytearray:
    """
    Generate random data for payload
    """
    payload = bytearray(payload_length)

    for index in range(payload_length):
        data = random.randint(1, LengthInfo.ONE_BYTE - 1)  # 1 byte for data
        payload[index] = data

    return payload


def get_random_payload_size() -> int:
    """
    Generate a random number for the size of the payload
    """
    return random.randint(0, LengthInfo.MAX_PAYLOAD_SIZE)


def settings_for_sending_packet(packet: Packet) -> None:
    """
    From sender to receiver
    """
    header = packet.get_header()

    # 1. Make Payload
    payload_length: int = get_random_payload_size()
    packet.set_payload(get_random_data_for_payload(payload_length))

    # 1. Message ID
    header.set_message_id((ServiceID.DEFAULT, MethodID.DEFAULT))

    # 2. Length
    header.set_length(LengthInfo.HEADER_SIZE + payload_length)

    # 3. Request ID
    header.set_request_id((ClientID.DEFAULT, SessionID.DEFAULT))

    # 4. Protocol version
    header.set_protocol_version(ProtocolVersion.DEFAULT)

    # 5. Interface version
    header.set_interface_version(InterfaceVersion.DEFAULT)

    # 6. Message Type
    # Server(Sender) to Client(Receiver)
    header.set_message_type(MessageType.RESPONSE)

    # 7. Return code
    header.set_return_code(ReturnCode.DEFAULT)


def main():
    packet = Packet()
    sender = Sender()

    while True:
        settings_for_sending_packet(packet)
        print("send: #################################################")
        sender.send(packet)
        print("receive: #################################################")
        if not sender.receive():
            break

        time.sleep(1)

    sender.close()


if __name__ == "__main__":
    main()
