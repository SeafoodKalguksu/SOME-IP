# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

"""
Client
"""
from typing import List, Tuple
import random
import socket
import time

from packet import Packet
from header_fields.message_type import MessageType
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

    def packet_to_bytes(self, packet: Packet) -> bytes:
        length = packet.get_header().get_length()
        payoad = packet.get_payload()

        # Message ID
        service_id = packet.get_header().get_message_id().get_service_id()
        method_id = packet.get_header().get_message_id().get_method_id()
        packet_bytes = int(service_id).to_bytes(2, "big")
        packet_bytes += int(method_id).to_bytes(2, "big")

        # Length
        packet_bytes += length.to_bytes(4, "big")

        # Request ID
        client_id = packet.get_header().get_request_id().get_client_id()
        session_id = packet.get_header().get_request_id().get_session_id()
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
        packet_bytes = self.packet_to_bytes(packet)
        sent_size = self.sender_socket.send(packet_bytes)
        print(f"sent_size: {sent_size}")
        # self.save_in_file(packet_bytes)

    def receive(self) -> bool:
        header_bytes = self.sender_socket.recv(16)
        if not header_bytes:
            return False

        header = int.from_bytes(header_bytes, "big")
        service_id = header >> 14 * 8 & 0xFFFF
        method_id = header >> 12 * 8 & 0xFFFF
        length = header >> 8 * 8 & 0xFFFFFFFF
        client_id = header >> 6 * 8 & 0xFFFF
        session_id = header >> 4 * 8 & 0xFFFF
        protocol_version = header >> 3 * 8 & 0xFF
        interface_version = header >> 2 * 8 & 0xFF
        message_type = header >> 1 * 8 & 0xFF
        return_code = header & 0xFF

        print(f"received, service_id: {service_id}")
        print(f"received, method_id: {method_id}")
        print(f"received, length: {length}")
        print(f"received, client_id: {client_id}")
        print(f"received, session_id: {session_id}")
        print(f"received, protocol: {protocol_version}")
        print(f"received, interface: {interface_version}")
        print(f"received, msg type: {message_type}")
        print(f"received, return code: {return_code}")

        # Payload
        payload = self.sender_socket.recv(length - LengthInfo.HEADER_SIZE)

        self.header = header
        self.payload = payload

        return True


def make_random_data_for_payload(payload_length: int) -> bytearray:
    """
    Generate random data for payload
    """
    payload = bytearray(payload_length)

    for index in range(payload_length):
        data = random.randint(1, LengthInfo.ONE_BYTE)  # 1 byte for data
        payload[index] = data

    return payload


def get_random_payload_size() -> int:
    """
    Generate a random number for the size of the payload
    """
    return random.randint(0, LengthInfo.MAX_PAYLOAD_SIZE)


def settings_for_sending_packet(packet: Packet) -> None:
    """
    sending from sender to receiver
    """
    header = packet.get_header()

    # 1. Length
    payload_length: int = get_random_payload_size()
    header.set_length(LengthInfo.HEADER_SIZE + payload_length)

    # 2. Message Type
    header.set_message_type(MessageType.RESPONSE)

    # 3. Payload
    packet.set_payload(make_random_data_for_payload(payload_length))


def main():
    packet = Packet()
    sender = Sender()

    # for _ in range(2):
    while True:
        settings_for_sending_packet(packet)
        sender.send(packet)
        print("#################################################")
        sender.receive()
        print("#################################################")
        time.sleep(1)

    sender.close()


if __name__ == "__main__":
    main()
