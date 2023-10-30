#!/usr/bin/python3
"""0-validate_utf8 module."""


def validUTF8(data):
    # type: (List[int]) -> bool
    """
    validUTF8: determines if a given data set represents a valid \
        UTF-8 encoding.

    Args:
        data: list of integers.

    Returns:
        True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0
    for num in data:
        if num_bytes == 0:
            if (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            elif (num >> 7) == 0b0:
                num_bytes = 0
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
