#!/usr/bin/env python3
import os
import sys

from FormatBytes import format_bytes

def raw_size(fullpath):
    """
    Returns the size of the input directory, in bytes
    """
    try:
        return sum([os.stat(os.path.join(path, file)).st_size
                    for path, _, files in os.walk(fullpath)
                    for file in files])

    except Exception:
        total = 0
        for path, _, files in os.walk(fullpath):
            try:
                for file in files:
                    total += os.stat(os.path.join(path, file)).st_size
            except Exception:
                print('-', end=' ')
        return total

def formatted_size(fullpath):
    """
    Returns the string format of size of the input directory,
    with metric prefixes like Kilo, Mega, Giga, etc.
    """
    return format_bytes(raw_size(fullpath))

def main():
    """
    Main function for displaying size of drectories
    """
    if len(sys.argv) > 1: # Command Line Input
        print(raw_size(sys.argv[1]))
        print(formatted_size(sys.argv[1]))
    else:   # Default Path: Desktop
        print(raw_size(f"C:\\Users\\{os.getlogin()}\\Desktop"))
        print(formatted_size(f"C:\\Users\\{os.getlogin()}\\Desktop"))

if __name__ == "__main__":
    main()
