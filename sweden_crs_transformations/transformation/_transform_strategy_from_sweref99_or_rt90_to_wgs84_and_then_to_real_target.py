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
from sweden_crs_transformations.transformation._transform_strategy import _TransformStrategy


class _TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS SWEREF99 or RT90, and the target too
    def transform(self,
                  source_coordinate: CrsCoordinate,
                  final_target_crs_projection: CrsProjection
                  ) -> CrsCoordinate:
        from sweden_crs_transformations.transformation._transformer import _Transformer
        source_coordinate_projection: CrsProjection = source_coordinate.get_crs_projection()
        if (not (
            (source_coordinate_projection.is_sweref99() or source_coordinate_projection.is_rt90())
            and
            (final_target_crs_projection.is_sweref99() or final_target_crs_projection.is_rt90())
        )):
            _Transformer._throwExceptionMessage(source_coordinate.get_crs_projection(), final_target_crs_projection)

        intermediate_crs_projection = CrsProjection.WGS84
        intermediate_wgs84_coordinate = _Transformer.transform(source_coordinate, intermediate_crs_projection)
        return _Transformer.transform(intermediate_wgs84_coordinate, final_target_crs_projection)
