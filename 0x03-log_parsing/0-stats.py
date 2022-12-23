#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys


"""
Dictionary to store the number of lines for each status code
"""
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

"""
Variable to store the total file size
"""
total_sizes = 0

"""
Counter to keep track of the number of lines read
"""
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
    """ Read lines from stdin one by one """
    for line in sys.stdin:
        """ Parse the line to extract the status code and file size """
        try:
            line = line[:-1]
            parts = line.split(' ')
            total_sizes += int(parts[-1])
            status_code = int(parts[-2])
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            """
            Skip the line if it is
            not in the expected format
            """
            continue

        """
        Print the statistics every 10 lines
        or when a keyboard interruption occurs
        """
        if line_counter % 10 == 0 or line_counter == 0:
            printStats()
        line_counter += 1

except KeyboardInterrupt:
    printStats()
    raise
printStats()
