#!/usr/bin/python3
"""Script that reads stdin
   line by line and computes metrics."""

import sys


def log_parse():
    """Function that reads stdin line by line and computes metrics.

    Args:
        None

    Returns:
        None
    """
    status_dict = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0}

    total_size = 0

    while True:
        for line in sys.stdin:
            line = line.strip()
            line = line.split()

            if len(line) > 2:
                try:
                    status = line[-2]
                    size = line[-1]

                    for k, v in status_dict.items():
                        if status == k:
                            status_dict[k] += 1
                            total_size += int(size)
                    print('File size: {}'.format(total_size))
                    for key in sorted(status_dict):
                        print('{}: {}'.format(key, status_dict[key]))

                except KeyboardInterrupt:
                    print('File size: {}'.format(total_size))
                    for key in sorted(status_dict):
                        print('{}: {}'.format(key, status_dict[key]))


if __name__ == '__main__':
    log_parse()
