import unittest
from src import Path

PATH_TO_EXAMPLE = '../examples/Path-to-bed.json'

class PathTest(unittest.TestCase):
    def test_readfile(self):
        readf = Path(PATH_TO_EXAMPLE)

