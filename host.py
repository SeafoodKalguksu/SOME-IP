# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import socket
import random
from typing import Tuple, Any

from length_info import LengthInfo
from packet import Packet


class Host:
    def __init__(self) -> None:
        self.socket: socket | None = None
        self.host_address: str | int | None = None
        self.host_port: int | None = None
        self.the_other_hosts_address: Tuple[str | int] | None = None
        self.connection: socket | None = None

    def send(self, packet: Packet) -> bool:
        if self.socket is None or self.connection is None or packet is None:
            return False

        return True

    def get_random_payload_size(self) -> int:
        """
        Generate a random number for the size of the payload
        """
        return random.randint(1, LengthInfo.MAX_PAYLOAD_SIZE)
