import unittest
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.crs_projection_factory import CrsProjectionFactory
from typing import Iterator


class CrsProjectionFactoryTest(unittest.TestCase):
    epsgNumberForWgs84 = 4326
    epsgNumberForSweref99tm = 3006 # https://epsg.org/crs_3006/SWEREF99-TM.html
    numberOfSweref99projections = 13 #  with EPSG numbers 3006-3018
    numberOfRT90projections = 6 # with EPSG numbers 3019-3024
    numberOfWgs84Projections = 1 # just to provide semantic instead of using a magic number 1 below
    totalNumberOfProjections = numberOfSweref99projections + numberOfRT90projections + numberOfWgs84Projections

    def setUp(self):
        self._allCrsProjections: list[CrsProjection] = CrsProjectionFactory.get_all_crs_projections()


    def test_get_crs_projection_by_epsg_number(self):
        self.assertEqual(
            CrsProjection.SWEREF_99_TM,
            CrsProjectionFactory.get_crs_projection_by_epsg_number(CrsProjectionFactoryTest.epsgNumberForSweref99tm)
        )

        self.assertEqual(
            CrsProjection.SWEREF_99_23_15,
            CrsProjectionFactory.get_crs_projection_by_epsg_number(3018)  # https://epsg.io/3018
        )

        self.assertEqual(
            CrsProjection.RT90_5_0_GON_O,
            CrsProjectionFactory.get_crs_projection_by_epsg_number(3024)  # https://epsg.io/3018
        )


    def test_verify_total_number_of_projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.totalNumberOfProjections,
            len(self._allCrsProjections)  # retrieved with 'get_all_crs_projections' in the SetUp method
        )

    def get_number_of_projections(self, mylambda):
        res: Iterator = filter(mylambda, self._allCrsProjections)
        lis = list(res)
        return len(lis)

    def test_verify_number_of_wgs84_projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfWgs84Projections,
            self.get_number_of_projections(lambda crs: crs.is_wgs84())
        )


    def test_verify_number_of_sweref99_projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfSweref99projections,
            self.get_number_of_projections(lambda crs: crs.is_sweref99())
        )

    def test_verify_number_of_rt90_projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfRT90projections,
            self.get_number_of_projections(lambda crs: crs.is_rt90())
        )

    def test_verify_that_all_projections_can_be_retrieved_by_its_epsg_number(self):
        for crsProjection in self._allCrsProjections:
            crsProj: CrsProjection = CrsProjectionFactory.get_crs_projection_by_epsg_number(crsProjection.get_epsg_number())
            self.assertEqual(crsProjection, crsProj)
