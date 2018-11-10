#!/usr/bin/python3

import sys, time

def main(argv):
    if (len(argv) < 1):
        print("Input file is missing!")
    else:
        # TODO: Add header line

        # Read all lines of the file
        for line in open(argv[0]):
            # FIXME: And add one line for each character
            for c in line:
                print(c)
                time.sleep(1)

if __name__ == "__main__":
   main(sys.argv[1:])
