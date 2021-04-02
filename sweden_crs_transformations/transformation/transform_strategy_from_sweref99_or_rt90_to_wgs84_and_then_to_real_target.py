"""
/*
* Copyright (c) Tomas Johansson , http://www.programmerare.com
* The code in this library is licensed with MIT.
* The library is based on the library 'MightyLittleGeodesy' (https://github.com/bjornsallarp/MightyLittleGeodesy/)
* which is also released with MIT.
* License information about 'sweden_crs_transformations_4net' and 'MightyLittleGeodesy':
* https://github.com/TomasJohansson/sweden_crs_transformations_4net/blob/csharpe_SwedenCrsTransformations/LICENSE
* For more information see the webpage below.
* https://github.com/TomasJohansson/sweden_crs_transformations_4net
*/
"""
from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy


class TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS SWEREF99 or RT90
    def transform(self,
        sourceCoordinate: CrsCoordinate,
        finalTargetCrsProjection: CrsProjection
    ) -> CrsCoordinate:
        from sweden_crs_transformations.transformation.transformer import Transformer
        # sourceCoordinateProjection: CrsProjection = sourceCoordinate.getCrsProjection()
        # var wgs84coordinate = Transformer.Transform(sourceCoordinate, CrsProjection.wgs84);
        # return Transformer.Transform(wgs84coordinate, targetCrsProjection);
        intermediateCrsProjection = CrsProjection.WGS84
        intermediateWgs84coordinate = Transformer.transform(sourceCoordinate, intermediateCrsProjection)
        return Transformer.transform(intermediateWgs84coordinate, finalTargetCrsProjection)
