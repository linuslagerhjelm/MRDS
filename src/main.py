import sys
import os
from src.mrdsapi import Mrdsapi
from src.path import Path
from src.lowcontrol import LowControl


# Input argument address, port, lookahead, path to path file
def main():
    if len(sys.argv) != 5:
        print "This program requires exactly 5 input parameters. Got: " + str(len(sys.argv))
        sys.exit(0)

    ADDRESS = sys.argv[1]
    PORT = sys.argv[2]
    LOOKAHEAD = sys.argv[3]
    path = Path(os.path.abspath(sys.argv[4]))
    robot = Robot(Mrdsapi(ADDRESS, PORT))

if __name__ == "__main__":
    main()



