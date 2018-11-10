#!/usr/bin/python3

import sys, random, shutil

lospeed = 0.03
hispeed = 0.4
thinkscaler = 5
tabtime = 0.0001

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
            prev=' ' # Rem.: For leading tabulation spaces!
            # And add one line for each character
            for c in line:
                sys.stdout.write('[')
                if ((c == '\t') or (c == ' ')):
                    # When char is tab or space it might be a source code!
                    # That means we must skip tabulation spaces and also
                    # we should wait a bit after end of words (thinking time)
                    if ((prev == '\t') or (prev == ' ')):
                        t = t + tabtime # fast tabulation!
                    else:
                        t = t + random.uniform(lospeed*thinkscaler, hispeed*thinkscaler) # thinking time
                else:
                    t = t + random.uniform(lospeed, hispeed) # usual writin' time

                sys.stdout.write(str(t))
                sys.stdout.write(', "o", "')
                if (c == '\n'):
                    # Rem.: Endl is used by the file format this way!!!
                    sys.stdout.write('\\r\\n')
                elif (c == '"'):
                    sys.stdout.write('\\"')
                else:
                    sys.stdout.write(str(c))
                print('"]')
                prev = c # update prev char

if __name__ == "__main__":
   main(sys.argv[1:])
