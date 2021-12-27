# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import socket
import time
from some_over_ip import PacketForSOMEoverIP

"""
Server
"""


class Receiver:
    def __init__(self) -> None:
        self.header: bytearray = None
        self.payload: bytearray = None

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("localhost", 5004)
        self.socket.bind(self.address)
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        # self.file = open("received_packet.txt", "ab")
        print("Connected by", self.addr)

    def close(self) -> None:
        # self.file.close()
        self.conn.close()

    def send(self) -> None:
        # Header
        header = int.from_bytes(self.header, "big")
        service_id = header >> 14 * 8 & 0xFFFF
        method_id = header >> 12 * 8 & 0xFFFF
        length = header >> 8 * 8 & 0xFFFFFFFF
        client_id = header >> 6 * 8 & 0xFFFF
        session_id = header >> 4 * 8 & 0xFFFF
        protocol_version = header >> 3 * 8 & 0xFF
        interface_version = header >> 2 * 8 & 0xFF
        message_type = header >> 1 * 8 & 0xFF
        return_code = header & 0xFF

        print(f"will send, service_id: {service_id}")
        print(f"will send, method_id: {method_id}")
        print(f"will send, length: {length}")
        print(f"will send, client_id: {client_id}")
        print(f"will send, session_id: {session_id}")
        print(f"will send, protocol: {protocol_version}")
        print(f"will send, interface: {interface_version}")
        print(f"will send, msg type: {message_type}")
        print(f"will send, return code: {return_code}")

        self.conn.send(self.header + self.payload)

    def receive(self, conn: socket) -> bool:
        """
        1. Receive header(16 bytes)
        2. Get 'length' from the header
        3. Receive payload
        """
        header_bytes = conn.recv(16)
        if not header_bytes:
            return False

        # Header
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
        print("#################################################")

        # Update message type in header to MessageType.REQUEST
        message_type = 0x00
        header = header & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF00FF

        # Payload
        payload = conn.recv(length - 16)

        self.header = header.to_bytes(16, "big")
        self.payload = payload

        # self.save_packet_in_file(
        #     service_id,
        #     method_id,
        #     length,
        #     client_id,
        #     session_id,
        #     protocol_version,
        #     interface_version,
        #     message_type,
        #     return_code,
        #     payload,
        #     file,
        # )
        return True

    def save_packet_in_file(
        self,
        service_id,
        method_id,
        length,
        client_id,
        session_id,
        protocol_version,
        interface_version,
        message_type,
        return_code,
        payload,
        file,
    ) -> None:
        file.write(
            service_id
            + method_id
            + length
            + client_id
            + service_id
            + protocol_version
            + interface_version
            + message_type
            + return_code
            + payload
        )


def main():
    receiver = Receiver()

    while True:
        if False == receiver.receive(receiver.conn):
            break
        else:
            receiver.send()
            print("#################################################")

    receiver.close()


if __name__ == "__main__":
    main()
