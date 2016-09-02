import sys
import mrdsapi

#Input argument address, port, lookahead
def main():
    ADDRESS = sys.argv[1]
    PORT = sys.argv[2]
    LOOKAHEAD = sys.argv[3]
    mrds = Mrdsapi(ADDRESS, PORT)
    rob = Robot(mrds)

if __name__ == "__main__":
    main()



