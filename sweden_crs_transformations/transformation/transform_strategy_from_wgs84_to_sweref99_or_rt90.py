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
from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger import _GaussKreuger
from sweden_crs_transformations.mighty_little_geodesy._gauss_kreuger_parameter_object import _GaussKreugerParameterObject
from sweden_crs_transformations.mighty_little_geodesy._lat_lon import _LatLon
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy


class TransformStrategy_from_WGS84_to_SWEREF99_or_RT90(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS WGS84, and the target must be CRS SWEREF99 or RT90
    def transform(self,
        sourceCoordinate: CrsCoordinate,
        targetCrsProjection: CrsProjection
    ) -> CrsCoordinate:
        sourceCoordinateProjection: CrsProjection = sourceCoordinate.get_crs_projection()
        if(not(
            (sourceCoordinateProjection.is_wgs84())
            and
            (targetCrsProjection.is_sweref99() or targetCrsProjection.is_rt90())
        )):
            from sweden_crs_transformations.transformation.transformer import Transformer
            Transformer._throwExceptionMessage(sourceCoordinate.get_crs_projection(), targetCrsProjection)

        gaussKreugerParameterObject = _GaussKreugerParameterObject(targetCrsProjection)
        gaussKreuger = _GaussKreuger(gaussKreugerParameterObject)
        latLon: _LatLon = gaussKreuger.geodetic_to_grid(sourceCoordinate.get_latitude_y(), sourceCoordinate.get_longitude_x())
        return CrsCoordinate.create_coordinate(targetCrsProjection, latLon.latitudeY, latLon.longitudeX)
