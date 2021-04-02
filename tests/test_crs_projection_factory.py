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
        self._allCrsProjections: list[CrsProjection] = CrsProjectionFactory.GetAllCrsProjections()


    def test_GetCrsProjectionByEpsgNumber(self):
        self.assertEqual(
            CrsProjection.SWEREF_99_TM,
            CrsProjectionFactory.GetCrsProjectionByEpsgNumber(CrsProjectionFactoryTest.epsgNumberForSweref99tm)
        )

        self.assertEqual(
            CrsProjection.SWEREF_99_23_15,
            CrsProjectionFactory.GetCrsProjectionByEpsgNumber(3018) # https://epsg.io/3018
        )

        self.assertEqual(
            CrsProjection.RT90_5_0_GON_O,
            CrsProjectionFactory.GetCrsProjectionByEpsgNumber(3024)  # https://epsg.io/3018
        )


    def test_VerifyTotalNumberOfProjections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.totalNumberOfProjections,
            len(self._allCrsProjections) # retrieved with 'GetAllCrsProjections' in the SetUp method
        )

    def getNumberOfProjections(self, mylambda):
        res: Iterator = filter(mylambda, self._allCrsProjections)
        lis = list(res)
        return len(lis)

    def test_VerifyNumberOfWgs84Projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfWgs84Projections,
        self.getNumberOfProjections(lambda crs: crs.is_wgs84())
        )


    def test_VerifyNumberOfSweref99Projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfSweref99projections,
            self.getNumberOfProjections(lambda crs: crs.is_sweref99())
        )

    def test_VerifyNumberOfRT90Projections(self):
        self.assertEqual(
            CrsProjectionFactoryTest.numberOfRT90projections,
            self.getNumberOfProjections(lambda crs: crs.is_rt90())
        )

    def test_VerifyThatAllProjectionsCanBeRetrievedByItsEpsgNumber(self):
        for crsProjection in self._allCrsProjections:
            crsProj: CrsProjection = CrsProjectionFactory.GetCrsProjectionByEpsgNumber(crsProjection.get_epsg_number())
            self.assertEqual(crsProjection, crsProj)
