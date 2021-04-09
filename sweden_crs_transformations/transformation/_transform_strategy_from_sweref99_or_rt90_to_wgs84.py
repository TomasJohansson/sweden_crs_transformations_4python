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
        sourceCoordinate: CrsCoordinate,
        targetCrsProjection: CrsProjection
    ) -> CrsCoordinate:
        sourceCoordinateProjection = sourceCoordinate.get_crs_projection()
        if(not(
            (sourceCoordinateProjection.is_sweref99() or sourceCoordinateProjection.is_rt90())
            and
            targetCrsProjection.is_wgs84()
        )):
            from sweden_crs_transformations.transformation._transformer import _Transformer
            _Transformer._throwExceptionMessage(sourceCoordinate.get_crs_projection(), targetCrsProjection)

        gaussKreugerParameterObject = _GaussKreugerParameterObject(sourceCoordinateProjection)
        gaussKreuger = _GaussKreuger(gaussKreugerParameterObject)
        latLon: _LatLon = gaussKreuger.grid_to_geodetic(sourceCoordinate.get_latitude_y(), sourceCoordinate.get_longitude_x())
        return CrsCoordinate.create_coordinate(targetCrsProjection, latLon.latitudeY, latLon.longitudeX)
