import unittest
from sweden_crs_transformations.mighty_little_geodesy._lat_lon import _LatLon


class LatLonTest(unittest.TestCase):

    def test_latLon(self):
        latLon = _LatLon(12.34, 56.78)
        self.assertEqual(latLon.latitudeY, 12.34)
        self.assertEqual(latLon.longitudeX, 56.78)
