#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_sizes = 0

line_counter = 1


def printStats():
    """
    Print the final statistics after
    all lines have been read
    """
    print("File size:", total_sizes)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        try:
            line = line[:-1]
            parts = line.split(' ')
            total_sizes += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            continue

        if line_counter % 10 == 0 or line_counter == 0:
            printStats()
        line_counter += 1

except KeyboardInterrupt:
    printStats()
    raise
printStats()
