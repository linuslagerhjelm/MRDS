import unittest
from src import mrdsapi


ADDRESS = "192.168.1.12"
PORT = 50000


class MrdsapiTest(unittest.TestCase):
    def test_get_localization(self):
        mrds = mrdsapi.mrdsapi(ADDRESS, PORT)
        mrds.get_localization()

    def test_get_laser_echoes(self):
        mrds = mrdsapi.mrdsapi(ADDRESS, PORT)
        mrds.get_laser_echoes()

    def test_get_laser_properties(self):
        mrds = mrdsapi.mrdsapi(ADDRESS, PORT)
        mrds.get_laser_properties()

    def test_post_speed_data(self):
        mrds = mrdsapi.mrdsapi(ADDRESS, PORT)
        mrds.post_speed(0, 0.1)
