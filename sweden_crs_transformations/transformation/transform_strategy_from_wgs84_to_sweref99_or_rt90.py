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

using MightyLittleGeodesy;

namespace SwedenCrsTransformations.Transformation {
    internal class TransformStrategy_from_WGS84_to_SWEREF99_or_RT90 : TransformStrategy {
        // Precondition: sourceCoordinate must be CRS WGS84
        public CrsCoordinate Transform(
            CrsCoordinate sourceCoordinate,
            CrsProjection targetCrsProjection
        ) {
            var gkProjection = GaussKreugerFactory.getInstance().getGaussKreuger(targetCrsProjection);
            LatLon latLon = gkProjection.geodetic_to_grid(sourceCoordinate.LatitudeY, sourceCoordinate.LongitudeX);
            return CrsCoordinate.CreateCoordinate(targetCrsProjection, latLon.LatitudeY, latLon.LongitudeX);
        }
    }

}