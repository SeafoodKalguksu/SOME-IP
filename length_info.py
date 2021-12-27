class LengthInfo:
    HEADER_SIZE: int = 16
    MAX_PAYLOAD_SIZE: int = 3 * (2 ** 10)  # 3KB
    MAX_PACKET_LENGTH: int = HEADER_SIZE + MAX_PAYLOAD_SIZE
    ONE_BYTE: int = 256
