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
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy

class TransformStrategy_from_WGS84_to_SWEREF99_or_RT90(_TransformStrategy):
    # Precondition: sourceCoordinate must be CRS WGS84
    def transform(
        # CrsCoordinate sourceCoordinate,
        targetCrsProjection: CrsProjection
    #) -> CrsCoordinate:
    ):
        pass
        # var gkProjection = GaussKreugerFactory.getInstance().getGaussKreuger(targetCrsProjection);
        # LatLon latLon = gkProjection.geodetic_to_grid(sourceCoordinate.LatitudeY, sourceCoordinate.LongitudeX);
        # return CrsCoordinate.CreateCoordinate(targetCrsProjection, latLon.LatitudeY, latLon.LongitudeX);
