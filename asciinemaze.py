#!/usr/bin/python3

import sys, random, shutil

lospeed = 0.03
hispeed = 0.4

def main(argv):
    if (len(argv) < 1):
        print("Input file is missing!")
    else:
        # Create header line
        # Use the width and height as the terminal is now!
        col, row = shutil.get_terminal_size()
        sys.stdout.write('{"timestamp": 1541886839, "width":')
        sys.stdout.write(str(col))
        sys.stdout.write(', "version": 2, "env": {"TERM": "xterm-256color", "SHELL": "/bin/bash"}, "height": ')
        sys.stdout.write(str(row))
        print('}')

        # Read all lines of the file
        t=0
        for line in open(argv[0]):
            # And add one line for each character
            for c in line:
                t = t + random.uniform(lospeed, hispeed)
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
