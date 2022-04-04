# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import socket
import random
import time


from packet import Packet, Direction
from length_info import LengthInfo


class Sender:
    def __init__(self, address: str | int = "localhost", port: int = 5004) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))

    def send(self, packet: Packet) -> bool:
        if not packet:
            return False

        packet_bytes = packet.convert_packet_instance_to_bytes()
        sent_size = self.socket.send(packet_bytes)

        if sent_size == packet.header.length:
            print(f"[Sender] The packet was sent successfully, sent_size: {sent_size}")
            packet.debug_info(packet_bytes, "S: send")
            return True
        else:
            print(
                f"[Sender] Failed to send a packet, sent size: {sent_size}, length: {packet.header.length}"
            )
            return False

    def get_payload_size(self) -> int:
        """
        Generate a random number for the size of the payload
        """
        return random.randint(1, LengthInfo.MAX_PAYLOAD_SIZE)


def main():
    packet = Packet()
    sender = Sender()

    while True:
        # Make a packet to send
        payload_size = sender.get_payload_size()
        payload = packet.make_payload_data(payload_size)
        packet.setting(
            payload, payload_size, Direction.SENDER_TO_RECEIVER
        )

        if not sender.send(packet):
            break

        # Receive a packet
        packet_bytes = sender.socket.recv(LengthInfo.MAX_PACKET_LENGTH)
        if not packet_bytes:
            break
        else:
            Packet().debug_info(packet_bytes, "S: recv")
            
        time.sleep(1)

    sender.socket.close()


if __name__ == "__main__":
    main()
