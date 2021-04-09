"""
| Copyright (c) Tomas Johansson , http://www.programmerare.com
| The code in this library is licensed with MIT.
| The library is based on the C#.NET library 'sweden_crs_transformations_4net' (https://github.com/TomasJohansson/sweden_crs_transformations_4net)
| which in turn is based on 'MightyLittleGeodesy' (https://github.com/bjornsallarp/MightyLittleGeodesy/)
| which is also released with MIT.
| License information about 'sweden_crs_transformations_4python' and 'MightyLittleGeodesy':
| https://github.com/TomasJohansson/sweden_crs_transformations_4python/blob/python_SwedenCrsTransformations/LICENSE
| For more information see the webpage below.
| https://github.com/TomasJohansson/sweden_crs_transformations_4python
"""
from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy


class TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS SWEREF99 or RT90, and the target too
    def transform(self,
        sourceCoordinate: CrsCoordinate,
        finalTargetCrsProjection: CrsProjection
    ) -> CrsCoordinate:
        from sweden_crs_transformations.transformation.transformer import Transformer
        sourceCoordinateProjection: CrsProjection = sourceCoordinate.get_crs_projection()
        if(not(
            (sourceCoordinateProjection.is_sweref99() or sourceCoordinateProjection.is_rt90())
            and
            (finalTargetCrsProjection.is_sweref99() or finalTargetCrsProjection.is_rt90())
        )):
            Transformer._throwExceptionMessage(sourceCoordinate.get_crs_projection(), finalTargetCrsProjection)

        intermediateCrsProjection = CrsProjection.WGS84
        intermediateWgs84coordinate = Transformer.transform(sourceCoordinate, intermediateCrsProjection)
        return Transformer.transform(intermediateWgs84coordinate, finalTargetCrsProjection)
