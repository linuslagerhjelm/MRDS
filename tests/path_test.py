import json
import unittest
from src.path import Path
from src.utils import Utils

PATH_TO_EXAMPLE = 'examples/Path-to-bed.json'


class PathTest(unittest.TestCase):
    def test_readfile(self):
        Path(PATH_TO_EXAMPLE)

    def test_get_closest_point(self):
        p1 = json.load(open(PATH_TO_EXAMPLE, 'r'))[0]
        path = Path(PATH_TO_EXAMPLE)
        self.assertTrue(Utils.position_equals(p1, path.get_closest_pos()))
