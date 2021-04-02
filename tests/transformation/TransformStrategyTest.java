package com.programmerare.sweden_crs_transformations_4jvm.transformation;

import com.programmerare.sweden_crs_transformations_4jvm.CrsCoordinate;
import com.programmerare.sweden_crs_transformations_4jvm.CrsProjection;
import org.junit.*;
import org.junit.function.ThrowingRunnable;

public class TransformStrategyTest  {
    
    private CrsCoordinate coordinateWgs84, coordinateSweref99, coordinateRT90;
    
    @Before
    public void setUp() throws Exception {
        coordinateWgs84 = CrsProjection.WGS84.createCoordinate(60.0, 20.0);
        coordinateSweref99 = CrsProjection.SWEREF_99_TM.createCoordinate(6484098.0, 333538.0);
        coordinateRT90 = CrsProjection.RT90_2_5_GON_V.createCoordinate(6797357.0, 1500627.0);
    }

    private void assertIllegalArgumentException(
        final TransformStrategy transformStrategy,
        final CrsCoordinate sourceCoordinate,
        final CrsProjection targetProjection
    ) {
        Assert.assertThrows(
            IllegalArgumentException.class,
            new ThrowingRunnable() {
                @Override
                public void run() throws Throwable {
                    transformStrategy.transform(sourceCoordinate, targetProjection);
                }
            }
        );        
    }
    
    @Test
    public void assertException__ForStrategy__From_Sweref99OrRT90__to_Sweref99OrRT90() {
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
    }

    @Test
    public void assertException__ForStrategy__From_SWEREF99_or_RT90_to_WGS84() {
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
    }


    @Test
    public void assertException__ForStrategy__From_WGS84_to_SWEREF99_or_RT90() {
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
    }
    
}
