import sys
import os
from time import sleep
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
    lc = LowControl(Mrdsapi(ADDRESS, PORT))
    for i in range(0, len(path.data_points)):
        lc.steer_to_point(path.data_points[i], 1)
        sleep(.1)

if __name__ == "__main__":
    main()



