import unittest
from sweden_crs_transformations.crs_projection import CrsProjection

# using SwedenCrsTransformations;
# using System.Collections.Generic;
# using static SwedenCrsTransformationsTests.CrsProjectionFactoryTest; // to be able to use constants such as epsgNumberForSweref99tm and epsgNumberForWgs84
# using static SwedenCrsTransformations.CrsProjection;


class CrsProjectionTest(unittest.TestCase):
    # TODO maybe define these below constants instead in 'CrsProjectionFactoryTest' as in C#.NET library being ported to this Python library
    epsgNumberForWgs84: int = 4326
    epsgNumberForSweref99tm: int = 3006
    numberOfSweref99projections: int = 13  # ; // with EPSG numbers 3006-3018
    numberOfRT90projections: int = 6  # ; // with EPSG numbers 3019-3024
    numberOfWgs84Projections: int = 1  # ; // just to provide semantic instead of using a magic number 1 below
    totalNumberOfProjections = numberOfSweref99projections + numberOfRT90projections + numberOfWgs84Projections

    def setUp(self):
        self._wgs84Projections = {CrsProjection.WGS84}

        self._sweref99Projections = {
            CrsProjection.SWEREF_99_12_00, CrsProjection.SWEREF_99_13_30, CrsProjection.SWEREF_99_14_15,
            CrsProjection.SWEREF_99_15_00, CrsProjection.SWEREF_99_15_45, CrsProjection.SWEREF_99_16_30,
            CrsProjection.SWEREF_99_17_15, CrsProjection.SWEREF_99_18_00, CrsProjection.SWEREF_99_18_45,
            CrsProjection.SWEREF_99_20_15, CrsProjection.SWEREF_99_21_45, CrsProjection.SWEREF_99_23_15,
            CrsProjection.SWEREF_99_TM
        }

        self._rt90Projections = {
            CrsProjection.RT90_0_0_GON_V, CrsProjection.RT90_2_5_GON_O, CrsProjection.RT90_2_5_GON_V,
            CrsProjection.RT90_5_0_GON_O, CrsProjection.RT90_5_0_GON_V, CrsProjection.RT90_7_5_GON_V
        }


    def test_get_epsg_number(self):
        self.assertEqual(
            CrsProjectionTest.epsgNumberForSweref99tm,
            CrsProjection.SWEREF_99_TM.get_epsg_number()
        )

        self.assertEqual(
            CrsProjectionTest.epsgNumberForWgs84,
            CrsProjection.WGS84.get_epsg_number()
        )


    def test_is_wgs84(self):
        self.assertEqual(
            CrsProjectionTest.numberOfWgs84Projections,
            len(self._wgs84Projections)
        )

        for crsProjection in self._wgs84Projections: #type: CrsProjection
            self.assertTrue(crsProjection.is_wgs84())

        for crsProjection in self._sweref99Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_wgs84())

        for crsProjection in self._rt90Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_wgs84())


    def test_is_sweref99(self):
        self.assertEqual(
            CrsProjectionTest.numberOfSweref99projections,
            len(self._sweref99Projections)
        )

        for crsProjection in self._wgs84Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_sweref99())

        for crsProjection in self._sweref99Projections: #type: CrsProjection
            self.assertTrue(crsProjection.is_sweref99())

        for crsProjection in self._rt90Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_sweref99())


    def test_is_rt90(self):
        self.assertEqual(
            CrsProjectionTest.numberOfRT90projections,
            len(self._rt90Projections)
        )

        for crsProjection in self._wgs84Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_rt90())

        for crsProjection in self._sweref99Projections: #type: CrsProjection
            self.assertFalse(crsProjection.is_rt90())

        for crsProjection in self._rt90Projections: #type: CrsProjection
            self.assertTrue(crsProjection.is_rt90())

    def test_string(self):
        self.assertEqual(
            "WGS84(EPSG:4326)",
            str(CrsProjection.WGS84)
        )

        self.assertEqual(
            "SWEREF_99_TM(EPSG:3006)",
            str(CrsProjection.SWEREF_99_TM)
        );

        self.assertEqual(
            "SWEREF_99_14_15(EPSG:3012)",
            str(CrsProjection.SWEREF_99_14_15)
        )

        self.assertEqual(
            "RT90_0_0_GON_V(EPSG:3022)",
            str(CrsProjection.RT90_0_0_GON_V)
        )


    '''
    [Test]
    public void CreateCoordinate() {
        const double x = 22.5;
        const double y = 62.5;
        CrsCoordinate crsCoordinate = CrsProjection.sweref_99_tm.CreateCoordinate(y, x);
        Assert.AreEqual(epsgNumberForSweref99tm, crsCoordinate.CrsProjection.GetEpsgNumber());
        Assert.AreEqual(CrsProjection.sweref_99_tm, crsCoordinate.CrsProjection);
        const double delta = 0.000001;
        Assert.AreEqual(x, crsCoordinate.LongitudeX, delta);
        Assert.AreEqual(y, crsCoordinate.LatitudeY, delta);
    '''
