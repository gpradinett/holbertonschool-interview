#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys

# Dictionary to store the number of lines for each status code
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

# Variable to store the total file size
total_size = 0

# Counter to keep track of the number of lines read
line_counter = 0

# Read lines from stdin one by one
for line in sys.stdin:
    # Parse the line to extract the status code and file size
    parts = line.split()
    try:
        status_code = int(parts[3])
        file_size = int(parts[4])
    except (ValueError, IndexError):
        """
        Skip the line if it is
        not in the expected format
        """
        continue

    # Update the statistics
    status_codes[status_code] += 1
    total_size += file_size
    line_counter += 1

    """
    Print the statistics every 10 lines
    or when a keyboard interruption occurs
    """
    if line_counter % 10 == 0 or line_counter == 0:
        print("Total file size:", total_size)
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f"{code}: {status_codes[code]}")

# Print the final statistics after all lines have been read
print("Total file size:", total_size)
for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
        print(f"{code}: {status_codes[code]}")
