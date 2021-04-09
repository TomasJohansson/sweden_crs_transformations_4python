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
from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger import _GaussKreuger
from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger_parameter_object import _GaussKreugerParameterObject
from sweden_crs_transformations.mighty_little_geodesy._lat_lon import _LatLon
from sweden_crs_transformations.transformation._transform_strategy import _TransformStrategy


class _TransformStrategy_from_SWEREF99_or_RT90_to_WGS84(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS SWEREF99 or RT90 , and the target must be WGS84
    def transform(self,
                  source_coordinate: CrsCoordinate,
                  target_crs_projection: CrsProjection
                  ) -> CrsCoordinate:
        source_coordinate_projection = source_coordinate.get_crs_projection()
        if(not(
            (source_coordinate_projection.is_sweref99() or source_coordinate_projection.is_rt90())
            and
            target_crs_projection.is_wgs84()
        )):
            from sweden_crs_transformations.transformation._transformer import _Transformer
            _Transformer._throwExceptionMessage(source_coordinate.get_crs_projection(), target_crs_projection)

        gaussKreugerParameterObject = _GaussKreugerParameterObject(source_coordinate_projection)
        gaussKreuger = _GaussKreuger(gaussKreugerParameterObject)
        lat_lon: _LatLon = gaussKreuger.grid_to_geodetic(source_coordinate.get_latitude_y(), source_coordinate.get_longitude_x())
        return CrsCoordinate.create_coordinate(target_crs_projection, lat_lon.latitude_y, lat_lon.longitude_x)
