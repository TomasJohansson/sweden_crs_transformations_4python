import unittest
from sweden_crs_transformations.crs_projection import CrsProjection

class CrsProjectionTest(unittest.TestCase):
    epsgNumberForWgs84 = 4326
    epsgNumberForSweref99tm = 3006 # https://epsg.org/crs_3006/SWEREF99-TM.html
    numberOfSweref99projections = 13 #  with EPSG numbers 3006-3018
    numberOfRT90projections = 6 # with EPSG numbers 3019-3024
    numberOfWgs84Projections = 1 # just to provide semantic instead of using a magic number 1 below
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

        self._allCrsProjections = CrsProjection.get_all_crs_projections()


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


    def test_CreateCoordinate(self):
        x = 22.5
        y = 62.5
        crsCoordinate = CrsProjection.SWEREF_99_TM.create_coordinate(y, x)
        self.assertEqual(CrsProjectionTest.epsgNumberForSweref99tm, crsCoordinate.get_crs_projection().get_epsg_number())
        self.assertEqual(CrsProjection.SWEREF_99_TM, crsCoordinate.get_crs_projection())
        delta = 0.000001
        self.assertEqual(x, crsCoordinate.get_longitude_x(), delta)
        self.assertEqual(y, crsCoordinate.get_latitude_y(), delta)


    def test_get_crs_projection_by_epsg_number(self):
        self.assertEqual(
            CrsProjection.SWEREF_99_TM,
            CrsProjection.get_crs_projection_by_epsg_number(CrsProjectionTest.epsgNumberForSweref99tm)
        )

        self.assertEqual(
            CrsProjection.SWEREF_99_23_15,
            CrsProjection.get_crs_projection_by_epsg_number(3018)  # https://epsg.io/3018
        )

        self.assertEqual(
            CrsProjection.RT90_5_0_GON_O,
            CrsProjection.get_crs_projection_by_epsg_number(3024)  # https://epsg.io/3018
        )


    def test_verify_total_number_of_projections(self):
        self.assertEqual(
            CrsProjectionTest.totalNumberOfProjections,
            len(self._allCrsProjections)  # retrieved with 'get_all_crs_projections' in the SetUp method
        )

    def get_number_of_projections(self, mylambda):
        res = filter(mylambda, self._allCrsProjections) # from typing import Iterator
        lis = list(res)
        return len(lis)

    def test_verify_number_of_wgs84_projections(self):
        self.assertEqual(
            CrsProjectionTest.numberOfWgs84Projections,
            self.get_number_of_projections(lambda crs: crs.is_wgs84())
        )


    def test_verify_number_of_sweref99_projections(self):
        self.assertEqual(
            CrsProjectionTest.numberOfSweref99projections,
            self.get_number_of_projections(lambda crs: crs.is_sweref99())
        )

    def test_verify_number_of_rt90_projections(self):
        self.assertEqual(
            CrsProjectionTest.numberOfRT90projections,
            self.get_number_of_projections(lambda crs: crs.is_rt90())
        )

    def test_verify_that_all_projections_can_be_retrieved_by_its_epsg_number(self):
        for crsProjection in self._allCrsProjections:
            crsProj = CrsProjection.get_crs_projection_by_epsg_number(crsProjection.get_epsg_number())
            self.assertEqual(crsProjection, crsProj)
