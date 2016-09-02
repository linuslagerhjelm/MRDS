import sys
import mrdsapi

#Input argument address, port, lookahead, path to path file
def main():
    ADDRESS = sys.argv[1]
    PORT = sys.argv[2]
    LOOKAHEAD = sys.argv[3]
    mrds = Mrdsapi(ADDRESS, PORT)
    path_file = Path(path)
    rob = Robot(mrds)

if __name__ == "__main__":
    main()



