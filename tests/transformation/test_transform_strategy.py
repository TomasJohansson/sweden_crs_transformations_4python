import unittest

from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy
from sweden_crs_transformations.transformation.transform_strategy_from_sweref99_or_rt90_to_wgs84 import _TransformStrategy_from_SWEREF99_or_RT90_to_WGS84
from sweden_crs_transformations.transformation.transform_strategy_from_sweref99_or_rt90_to_wgs84_and_then_to_real_target import _TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget
from sweden_crs_transformations.transformation.transform_strategy_from_wgs84_to_sweref99_or_rt90 import _TransformStrategy_from_WGS84_to_SWEREF99_or_RT90
from sweden_crs_transformations.transformation.transformer import _Transformer


class TransformStrategyTest(unittest.TestCase):

    def setUp(self):
        self.coordinateWgs84: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.WGS84, 60.0, 20.0)
        self.coordinateSweref99 = CrsCoordinate.create_coordinate(CrsProjection.SWEREF_99_TM, 6484098.0, 333538.0)
        self.coordinateRT90 = CrsCoordinate.create_coordinate(CrsProjection.RT90_2_5_GON_V, 6797357.0, 1500627.0)


    def _assertValueError(self,
        transformStrategy: _TransformStrategy,
        sourceCoordinate: CrsCoordinate,
        targetProjection: CrsProjection
    ):
        with self.assertRaises(ValueError):
            _Transformer._transform_with_explicit_strategy(transformStrategy, sourceCoordinate, targetProjection)


    def test_assertException__ForStrategy__From_Sweref99OrRT90__to_Sweref99OrRT90(self):
        transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90 = _TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget()

        self._assertValueError(
            transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90,
            self.coordinateSweref99,
            self.coordinateWgs84.get_crs_projection()
        )

        self._assertValueError(
            transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90,
            self.coordinateWgs84,
            self.coordinateSweref99.get_crs_projection()
        )

    def test_assertException__ForStrategy__From_SWEREF99_or_RT90_to_WGS84(self):
        transformStrategy_From_SWEREF99_or_RT90_to_WGS84 = _TransformStrategy_from_SWEREF99_or_RT90_to_WGS84()

        self._assertValueError(
            transformStrategy_From_SWEREF99_or_RT90_to_WGS84,
            self.coordinateSweref99,
            self.coordinateRT90.get_crs_projection()
        )

        self._assertValueError(
            transformStrategy_From_SWEREF99_or_RT90_to_WGS84,
            self.coordinateWgs84,
            self.coordinateSweref99.get_crs_projection()
        )



    def test_assertException__ForStrategy__From_WGS84_to_SWEREF99_or_RT90(self):
        transformStrategy_From_WGS84_to_SWEREF99_or_RT90 = _TransformStrategy_from_WGS84_to_SWEREF99_or_RT90()

        self._assertValueError(
            transformStrategy_From_WGS84_to_SWEREF99_or_RT90,
            self.coordinateSweref99,
            self.coordinateRT90.get_crs_projection()
        )

        self._assertValueError(
            transformStrategy_From_WGS84_to_SWEREF99_or_RT90,
            self.coordinateSweref99,
            self.coordinateWgs84.get_crs_projection()
        )

    # successfully transformed coordinate values will be tested through the transform method of 'CrsCoordinate'
    # i.e. from the test file 'test_crs_coordinate.py'
