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

namespace SwedenCrsTransformations {

    /// <summary>
    /// Extension methods for the enum CrsProjection.
    /// See also <see cref="CrsProjection"/>
    /// </summary>
    public static class CrsProjectionExtensions {

        private const int epsgForSweref99tm = 3006;

        //private const int epsgLowerValueForSwerefLocal = 3007; // the NATIONAL sweref99TM has value 3006 as in the above constant
        //private const int epsgUpperValueForSwerefLocal = 3018;
        private const int epsgLowerValueForSweref = epsgForSweref99tm;
        private const int epsgUpperValueForSweref = 3018;

        private const int epsgLowerValueForRT90 = 3019;
        private const int epsgUpperValueForRT90 = 3024;

        /// <summary>
        /// The EPSG number for the enum instance representing a coordinate reference system.
        /// The implementation is trivial but it is a convenience method that provides semantic 
        /// through the method name i.e. what the enum value represents 
        /// and it also lets the client code avoid to do the casting.
        /// </summary>
        /// <returns>
        /// An EPSG number.
        /// https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
        /// </returns>
        public static int GetEpsgNumber(this CrsProjection crsProjection) { 
            // the EPSG numbers have been used as the values in this enum
            return (int)crsProjection;
        }

        /// <summary>
        /// True if the coordinate reference system is WGS84.
        /// </summary>
        public static bool IsWgs84(this CrsProjection crsProjection) {
            return crsProjection == CrsProjection.wgs84;
        }

        /// <summary>
        /// True if the coordinate reference system is a version of SWEREF99.
        /// </summary>
        public static bool IsSweref(this CrsProjection crsProjection) {
            int epsgNumber = crsProjection.GetEpsgNumber();
            return epsgLowerValueForSweref <= epsgNumber && epsgNumber <= epsgUpperValueForSweref;
        }

        /// <summary>
        /// True if the coordinate reference system is a version of RT90.
        /// </summary>
        public static bool IsRT90(this CrsProjection crsProjection) {
            int epsgNumber = crsProjection.GetEpsgNumber();
            return epsgLowerValueForRT90 <= epsgNumber && epsgNumber <= epsgUpperValueForRT90;
        }

        public static CrsCoordinate CreateCoordinate(
            this CrsProjection crsProjection,
            double yLatitude,
            double xLongitude
        ) {
            return CrsCoordinate.CreateCoordinate(crsProjection, yLatitude, xLongitude);
        }
    }
}