#!/usr/bin/python3

import sys, random

def main(argv):
    if (len(argv) < 1):
        print("Input file is missing!")
    else:
        # Add header line
        # TODO: Make width and height parameterizable!
        print('{"timestamp": 1541886839, "width": 144, "version": 2, "env": {"TERM": "xterm-256color", "SHELL": "/bin/bash"}, "height": 62}')

        # Read all lines of the file
        t=0
        for line in open(argv[0]):
            # And add one line for each character
            for c in line:
                t = t + random.uniform(0.1, 1.0)
                sys.stdout.write('[')
                sys.stdout.write(str(t))
                sys.stdout.write(', "o", "')
                if(c == '\n'):
                    # Used by the file format this way!!!
                    sys.stdout.write('\\r\\n')
                else:
                    sys.stdout.write(str(c))
                print('"]')

if __name__ == "__main__":
   main(sys.argv[1:])
