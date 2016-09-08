import sys
import os
from src.mrdsapi import Mrdsapi
from src.path import Path
from src.lowcontrol import LowControl
from src.highcontrol import HighControl


# Input argument address, port, lookahead, path to path file
def main():
    if len(sys.argv) != 6:
        print "This program requires exactly 6 input parameters. Got: " + str(len(sys.argv))
        sys.exit(0)

    address = sys.argv[1]
    port = sys.argv[2]
    lookahead = float(sys.argv[3])
    path = Path(os.path.abspath(sys.argv[4]))
    speed = float(sys.argv[5])
    lc = LowControl(Mrdsapi(address, port))
    hc = HighControl(lc, lookahead, speed)
    hc.start(path)


if __name__ == "__main__":
    main()



