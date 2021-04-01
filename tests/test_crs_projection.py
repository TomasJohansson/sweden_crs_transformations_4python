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
            self._wgs84Projections = {CrsProjection.wgs84}

            self._sweref99Projections = {
                CrsProjection.sweref_99_12_00, CrsProjection.sweref_99_13_30, CrsProjection.sweref_99_14_15,
                CrsProjection.sweref_99_15_00, CrsProjection.sweref_99_15_45, CrsProjection.sweref_99_16_30,
                CrsProjection.sweref_99_17_15, CrsProjection.sweref_99_18_00, CrsProjection.sweref_99_18_45,
                CrsProjection.sweref_99_20_15, CrsProjection.sweref_99_21_45, CrsProjection.sweref_99_23_15,
                CrsProjection.sweref_99_tm
            }

            self._rt90Projections = {
                CrsProjection.rt90_0_0_gon_v, CrsProjection.rt90_2_5_gon_o, CrsProjection.rt90_2_5_gon_v,
                CrsProjection.rt90_5_0_gon_o, CrsProjection.rt90_5_0_gon_v, CrsProjection.rt90_7_5_gon_v
            }


        def test_getEpsgNumber(self):
            self.assertEqual(
                CrsProjectionTest.epsgNumberForSweref99tm,
                CrsProjection.sweref_99_tm.GetEpsgNumber()
            )

            self.assertEqual(
                CrsProjectionTest.epsgNumberForWgs84,
                CrsProjection.wgs84.GetEpsgNumber()
            )


        def test_isWgs84(self):
            self.assertEquals(
                CrsProjectionTest.numberOfWgs84Projections,
                len(self._wgs84Projections)
            )

            for crsProjection in self._wgs84Projections: #type: CrsProjection
                self.assertTrue(crsProjection.IsWgs84())

            for crsProjection in self._sweref99Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsWgs84())

            for crsProjection in self._rt90Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsWgs84())


        def test_isSweRef99(self):
            self.assertEquals(
                CrsProjectionTest.numberOfSweref99projections,
                len(self._sweref99Projections)
            )

            for crsProjection in self._wgs84Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsSweref())

            for crsProjection in self._sweref99Projections: #type: CrsProjection
                self.assertTrue(crsProjection.IsSweref())

            for crsProjection in self._rt90Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsSweref())


        def test_isRT90(self):
            self.assertEquals(
                CrsProjectionTest.numberOfRT90projections,
                len(self._rt90Projections)
            )

            for crsProjection in self._wgs84Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsRT90())

            for crsProjection in self._sweref99Projections: #type: CrsProjection
                self.assertFalse(crsProjection.IsRT90())

            for crsProjection in self._rt90Projections: #type: CrsProjection
                self.assertTrue(crsProjection.IsRT90())

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
