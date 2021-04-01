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

using SwedenCrsTransformations.Transformation;
using System;
using System.Collections.Generic;

namespace SwedenCrsTransformations {

    /// <summary>
    /// Coordinate, defined by the three parameters for the factory methods.
    /// </summary>
    public class CrsCoordinate : IEquatable<CrsCoordinate> {

        /// <summary>
        /// The coordinate reference system that defines the location together with the other two properties (LongitudeX and LatitudeY).
        /// </summary>
        public CrsProjection CrsProjection { get; private set; }
        
        /// <summary>
        /// The coordinate value representing the longitude or X or Easting.
        /// </summary>    
        public double LongitudeX { get; private set; }

        /// <summary>
        /// The coordinate value representing the latitude or Y or Northing.
        /// </summary>
        public double LatitudeY { get; private set; }

        /// <summary>
        /// Private constructor. Client code must instead use the public factory methods.
        /// </summary>
        private CrsCoordinate(
            CrsProjection crsProjection,
            double yLatitude,
            double xLongitude
        ) {
            this.CrsProjection = crsProjection;
            this.LatitudeY = yLatitude;
            this.LongitudeX = xLongitude;
        }

        /// <summary>
        /// Transforms the coordinate to another coordinate reference system
        /// </summary>
        /// <param name="targetCrsProjection">the coordinate reference system that you want to transform to</param>        
        public CrsCoordinate Transform(CrsProjection targetCrsProjection) {
            return Transformer.Transform(this, targetCrsProjection);
        }

        /// <summary>
        /// Transforms the coordinate to another coordinate reference system
        /// </summary>
        /// <param name="targetEpsgNumber">the coordinate reference system that you want to transform to</param>        
        public CrsCoordinate Transform(int targetEpsgNumber) {
            CrsProjection targetCrsProjection = CrsProjectionFactory.GetCrsProjectionByEpsgNumber(targetEpsgNumber);
            return this.Transform(targetCrsProjection);
        }

        /// <summary>
        /// Factory method for creating an instance.
        /// </summary>
        /// <param name="epsgNumber">represents the coordinate reference system that defines the location together with the other two parameters</param>
        /// <param name="xLongitude">the coordinate position value representing the longitude or X or Easting</param>
        /// <param name="yLatitude">the coordinate position value representing the latitude or Y or Northing</param>
        public static CrsCoordinate CreateCoordinate(
            int epsgNumber,
            double yLatitude,
            double xLongitude
        ) {
            CrsProjection crsProjection = CrsProjectionFactory.GetCrsProjectionByEpsgNumber(epsgNumber);
            return CreateCoordinate(crsProjection, yLatitude, xLongitude);
        }

        /// <summary>
        /// Factory method for creating an instance.
        /// See also <see cref="CrsProjection"/>
        /// </summary>
        /// <param name="crsProjection">represents the coordinate reference system that defines the location together with the other two parameters</param>
        /// <param name="xLongitude">the coordinate position value representing the longitude or X or Easting</param>
        /// <param name="yLatitude">the coordinate position value representing the latitude or Y or Northing</param>
        public static CrsCoordinate CreateCoordinate(
            CrsProjection crsProjection,
            double yLatitude,
            double xLongitude
        ) {
            return new CrsCoordinate(crsProjection, yLatitude, xLongitude);
        }

        // ----------------------------------------------------------------------------------------------------------------------
        // These five methods below was generated with Visual Studio 2019
        public override bool Equals(object obj) {
            return Equals(obj as CrsCoordinate);
        }

        public bool Equals(CrsCoordinate other) {
            return other != null &&
                   CrsProjection == other.CrsProjection &&
                   LongitudeX == other.LongitudeX &&
                   LatitudeY == other.LatitudeY;
        }

        public override int GetHashCode() {
            int hashCode = 1147467376;
            hashCode = hashCode * -1521134295 + CrsProjection.GetHashCode();
            hashCode = hashCode * -1521134295 + LongitudeX.GetHashCode();
            hashCode = hashCode * -1521134295 + LatitudeY.GetHashCode();
            return hashCode;
        }

        public static bool operator ==(CrsCoordinate left, CrsCoordinate right) {
            return EqualityComparer<CrsCoordinate>.Default.Equals(left, right);
        }

        public static bool operator !=(CrsCoordinate left, CrsCoordinate right) {
            return !(left == right);
        }

        // These five methods above was generated with Visual Studio 2019
        // ----------------------------------------------------------------------------------------------------------------------

        /// <summary>
        /// Two examples of the string that can be returned:
        /// "CrsCoordinate [ X: 153369.673 , Y: 6579457.649 , CRS: SWEREF_99_18_00 ]"
        /// "CrsCoordinate [ Longitude: 18.059196 , Latitude: 59.330231 , CRS: WGS84 ]"
        /// </summary>
        public override string ToString() {
            return _toStringImplementation(this);
        }

        private static Func<CrsCoordinate, string> _toStringImplementation = defaultToStringImplementation;
        
        private static string defaultToStringImplementation(CrsCoordinate coordinate) {
            string crs = coordinate.CrsProjection.ToString().ToUpper();
            bool isWgs84 =  coordinate.CrsProjection.IsWgs84();
            string yOrLatitude = isWgs84 ? "Latitude" : "Y";
            string xOrLongitude = isWgs84 ? "Longitude" : "X";
            return string.Format(
                "{0} [ {1}: {2} , {3}: {4} , CRS: {5} ]",
                    nameof(CrsCoordinate),  // 0
                    yOrLatitude,            // 1
                    coordinate.LatitudeY,   // 2
                    xOrLongitude,           // 3
                    coordinate.LongitudeX,  // 4
                    crs                     // 5
            );
        }

        /// <summary>
        /// Sets a custom method to be used for rendering an instance when the 'ToString' method is used.
        /// </summary>
        public static void SetToStringImplementation(Func<CrsCoordinate, string> toStringImplementation) {
            _toStringImplementation = toStringImplementation;
        }

        /// <summary>
        /// Sets the default method to be used for rendering an instance when the 'ToString' method is used.
        /// </summary>
        public static void SetToStringImplementationDefault() { 
            _toStringImplementation = defaultToStringImplementation;
        }
    }
}