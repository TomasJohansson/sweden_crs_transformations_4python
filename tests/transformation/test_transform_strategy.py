import unittest
from sweden_crs_transformations.crs_projection import CrsProjection


class TransformStrategyTest(unittest.TestCase):

    # private CrsCoordinate coordinateWgs84, coordinateSweref99, coordinateRT90;

    def setUp(self):
        pass
        # self.coordinateWgs84 = CrsProjection.WGS84.createCoordinate(60.0, 20.0)
        # self.coordinateSweref99 = CrsProjection.SWEREF_99_TM.createCoordinate(6484098.0, 333538.0)
        # self.coordinateRT90 = CrsProjection.RT90_2_5_GON_V.createCoordinate(6797357.0, 1500627.0)


    def _assertIllegalArgumentException(
        # transformStrategy: TransformStrategy,
        # sourceCoordinate: CrsCoordinate,
        targetProjection: CrsProjection
    ):
        pass
        """
        Assert.assertThrows(
            IllegalArgumentException.class,
            new ThrowingRunnable() {
                @Override
                public void run() throws Throwable {
                    transformStrategy.transform(sourceCoordinate, targetProjection);
                }
            }
        )
        """

    def test_assertException__ForStrategy__From_Sweref99OrRT90__to_Sweref99OrRT90(self):
        pass
        """
        final TransformStrategy transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90 =
            TransFormStrategy_From_Sweref99orRT90_to_WGS84_andThenToSweref99orRT90_asFinalTarget.getInstance();

        assertIllegalArgumentException(
            transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90,
            this.coordinateSweref99,
            this.coordinateWgs84.getCrsProjection()
        );

        assertIllegalArgumentException(
            transformStrategy_From_Sweref99OrRT90__to_Sweref99OrRT90,
            this.coordinateWgs84,
            this.coordinateSweref99.getCrsProjection()
        );
        """

    def test_assertException__ForStrategy__From_SWEREF99_or_RT90_to_WGS84(self):
        pass
        """
        final TransformStrategy transformStrategy_From_SWEREF99_or_RT90_to_WGS84 =
            TransformStrategy_from_SWEREF99_or_RT90_to_WGS84.getInstance();

        assertIllegalArgumentException(
            transformStrategy_From_SWEREF99_or_RT90_to_WGS84,
            this.coordinateSweref99,
            this.coordinateRT90.getCrsProjection()
        );

        assertIllegalArgumentException(
            transformStrategy_From_SWEREF99_or_RT90_to_WGS84,
            this.coordinateWgs84,
            this.coordinateSweref99.getCrsProjection()
        );
        """



    def test_assertException__ForStrategy__From_WGS84_to_SWEREF99_or_RT90(self):
        pass
        """
        final TransformStrategy transformStrategy_From_WGS84_to_SWEREF99_or_RT90 =
            TransformStrategy_from_WGS84_to_SWEREF99_or_RT90.getInstance();

        assertIllegalArgumentException(
            transformStrategy_From_WGS84_to_SWEREF99_or_RT90,
            this.coordinateSweref99,
            this.coordinateRT90.getCrsProjection()
        );

        assertIllegalArgumentException(
            transformStrategy_From_WGS84_to_SWEREF99_or_RT90,
            this.coordinateSweref99,
            this.coordinateWgs84.getCrsProjection()
        );
        """
