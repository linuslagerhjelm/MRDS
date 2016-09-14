import sys, os, time
from src.mrdsapi import Mrdsapi
from src.path import Path
from src.lowcontrol import LowControl
from src.highcontrol import HighControl


# Input argument address, port, lookahead, path to path file, speed
def main():
    # validate input arga
    if len(sys.argv) != 6:
        print "This program requires exactly 5 input parameters. Got: " + str(len(sys.argv) - 1)
        sys.exit(0)

    # initialize everything
    address = sys.argv[1]
    port = sys.argv[2]
    lookahead = float(sys.argv[3])
    path = Path(os.path.abspath(sys.argv[4]))
    speed = float(sys.argv[5])
    lc = LowControl(Mrdsapi(address, port))
    hc = HighControl(lc, lookahead, speed)

    # start program
    t1 = time.time()
    hc.start(path)
    print "Robot finished path in: %s seconds" % (time.time() - t1)


if __name__ == "__main__":
    main()



