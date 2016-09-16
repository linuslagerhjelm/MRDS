import sys, os, time
from mrdsapi import Mrdsapi
from path import Path
from lowcontrol import LowControl
from highcontrol import HighControl

# Input argument address, port, lookahead, path to path file, speed
def main():
    # validate input args
    if len(sys.argv) < 3:
        print "This program requires at least 2 input parameters. Got: " + str(len(sys.argv) - 1)
        sys.exit(0)

    # initialize everything
    address = "localhost"
    port = 50000
    if len(sys.argv) == 5:
        address = sys.argv[3]
        port = sys.argv[4]

    lookahead = float(sys.argv[2])
    path = Path(os.path.abspath(sys.argv[1]))
    speed = 1
    lc = LowControl(Mrdsapi(address, port))
    hc = HighControl(lc, lookahead, speed)

    # start program
    t1 = time.time()
    hc.start(path)
    print "Robot finished path in: %s seconds" % (time.time() - t1)


if __name__ == "__main__":
    main()



