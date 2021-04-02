import unittest

from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger import _GaussKreuger
from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger_parameter_object import _GaussKreugerParameterObject
from sweden_crs_transformations.mighty_little_geodesy._lat_lon import _LatLon
from sweden_crs_transformations.crs_projection import CrsProjection


class GaussKreugerTest(unittest.TestCase):
        # https://kartor.eniro.se/m/XRCfh
        # WGS84 decimal (lat, lon)      59.330231, 18.059196
        # SWEREF99 TM (nord, öst)       6580822, 674032
        stockholmCentralStation_WGS84_latitude = 59.330231
        stockholmCentralStation_WGS84_longitude = 18.059196
        stockholmCentralStation_SWEREF99TM_northing = 6580822
        stockholmCentralStation_SWEREF99TM_easting = 674032

        def setUp(self):
            gaussKreugerParameterObject = _GaussKreugerParameterObject(CrsProjection.SWEREF_99_TM)
            self.gaussKreuger = _GaussKreuger(gaussKreugerParameterObject)

        def test_geodetic_to_grid_transforming_from_WGS84_to_SWEREF99TM(self):
            resultSweref99: _LatLon = self.gaussKreuger.geodetic_to_grid(
                GaussKreugerTest.stockholmCentralStation_WGS84_latitude,
                GaussKreugerTest.stockholmCentralStation_WGS84_longitude
            )
            # self.assertEqual(GaussKreugerTest.stockholmCentralStation_SWEREF99TM_northing, resultSweref99.latitudeY)
            # failure for the above if using 'assertEqual' as above:
            # Expected: 6580822
            # Actual: 6580821.991
            # self.assertEqual(GaussKreugerTest.stockholmCentralStation_SWEREF99TM_easting, resultSweref99.longitudeX)
            # failure for the above if using 'assertEqual' as above:
            # Expected: 674032
            # Actual: 674032.357
            delta: float = 0.36 # max diff is around 0.357
            self.assertAlmostEqual(GaussKreugerTest.stockholmCentralStation_SWEREF99TM_northing, resultSweref99.latitudeY, delta=delta)
            self.assertAlmostEqual(GaussKreugerTest.stockholmCentralStation_SWEREF99TM_easting, resultSweref99.longitudeX, delta=delta)

        def test_grid_to_geodetic_transforming_from_SWEREF99TM_to_WGS84(self):
            resultWGS84: _LatLon = self.gaussKreuger.grid_to_geodetic(
                GaussKreugerTest.stockholmCentralStation_SWEREF99TM_northing,
                GaussKreugerTest.stockholmCentralStation_SWEREF99TM_easting
            )
            # self.assertEqual(GaussKreugerTest.stockholmCentralStation_WGS84_latitude, resultWGS84.latitudeY)
            # failure for the above if using 'assertEqual' as above
            # Expected: 59.330231
            # Actual: 59.33023122691265
            # self.assertEqual(GaussKreugerTest.stockholmCentralStation_WGS84_longitude, resultWGS84.longitudeX)
            # failure for the above if using 'assertEqual' as above
            # Expected: 18.059196
            # Actual: 18.059189736354668
            delta: float = 0.000007 # max diff is around 6.26E-6
            self.assertAlmostEqual(GaussKreugerTest.stockholmCentralStation_WGS84_latitude, resultWGS84.latitudeY, delta=delta)
            self.assertAlmostEqual(GaussKreugerTest.stockholmCentralStation_WGS84_longitude, resultWGS84.longitudeX, delta=delta)
