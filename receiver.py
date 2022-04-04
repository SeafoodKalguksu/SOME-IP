# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import socket
import random
from typing import Tuple

from length_info import LengthInfo
from packet import Packet, Direction


class Receiver:
    def __init__(self, address: str | int = "localhost", port: int = 5004) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(Tuple(address, port))
        self.socket.listen(1)

        self.connection, self.sender_addr = self.socket.accept()
        print("Connected by", self.sender_addr)

    def send(self, packet: Packet) -> bool:
        if packet is not None:
            return False

        packet_bytes = packet.convert_packet_instance_to_bytes()
        sent_size = self.connection.send(packet_bytes)

        if sent_size == packet.header.length:
            print(
                f"[Receiver] the packet was sent successfully, sent_size: {sent_size}"
            )
            packet.debug_info(packet_bytes, "R: send")
            return True
        else:
            print(
                f"[Receiver] Failed to send a packet, sent size: {sent_size}, length: {packet.header.length}"
            )
            return False

    def get_payload_size(self) -> int:
        """
        Generate a random number for the size of the payload
        """
        return random.randint(1, LengthInfo.MAX_PAYLOAD_SIZE)


def main():
    packet = Packet()
    receiver = Receiver()

    while True:
        # Receive a packet
        packet_bytes = receiver.connection.recv(LengthInfo.MAX_PACKET_LENGTH)
        if not packet_bytes:
            break
        else:
            Packet().debug_info(packet_bytes, "R: recv")

        # Make a packet to send
        payload_size = receiver.get_payload_size()
        payload = packet.make_payload_data(payload_size)
        packet.setting(
            payload, payload_size, Direction.RECEIVER_TO_SENDER
        )

        if not receiver.send(packet):
            break

    receiver.connection.close()


if __name__ == "__main__":
    main()
