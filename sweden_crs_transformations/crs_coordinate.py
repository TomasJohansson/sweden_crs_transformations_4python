from __future__ import annotations
# without the above "from __future__ import annotations" a method in the class CrsCoordinate
# can not define (with type hinting)  a method to return a CrsCoordinate i.e. an instance from the same class
from sweden_crs_transformations.crs_projection_factory import CrsProjectionFactory

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

"""
    /// <summary>
    /// Coordinate, defined by the three parameters for the factory methods.
    /// </summary>
"""
class CrsCoordinate:

        """
        /// <summary>
        /// The coordinate reference system that defines the location together with the other two properties (LongitudeX and LatitudeY).
        /// </summary>
        """
        # public CrsProjection CrsProjection { get; private set; }
        def get_crs_projection(self) -> CrsProjection:
            return self.crsProjection

        """
        /// <summary>
        /// The coordinate value representing the longitude or X or Easting.
        /// </summary>
        """
        # public double LongitudeX { get; private set; }
        def get_longitude_x(self) -> float:
            return self.xLongitude


        """
        /// <summary>
        /// The coordinate value representing the latitude or Y or Northing.
        /// </summary>
        """
        # public double LatitudeY { get; private set; }
        def get_latitude_y(self) -> float:
            return self.yLatitude

        """
        /// <summary>
        /// Private constructor. Client code must instead use the public factory methods.
        /// </summary>
        """
        def __init__(self, crsProjection: CrsProjection, yLatitude: float, xLongitude: float):
            self.crsProjection = crsProjection
            self.yLatitude = yLatitude
            self.xLongitude = xLongitude


        """
        /// <summary>
        /// Transforms the coordinate to another coordinate reference system
        /// </summary>
        /// <param name="targetCrsProjection">the coordinate reference system that you want to transform to</param>
        """
        def transform(self, targetCrsProjection: CrsProjection) -> CrsCoordinate:
            from sweden_crs_transformations.transformation.transformer import Transformer
            return Transformer.transform(self, targetCrsProjection)

        """
        /// <summary>
        /// Transforms the coordinate to another coordinate reference system
        /// </summary>
        /// <param name="targetEpsgNumber">the coordinate reference system that you want to transform to</param>
        """
        def transform_by_epsg_number(self, targetEpsgNumber: int) -> CrsCoordinate:
            targetCrsProjection: CrsProjection = CrsProjectionFactory.get_crs_projection_by_epsg_number(targetEpsgNumber)
            return self.transform(targetCrsProjection)


        """
        /// <summary>
        /// Factory method for creating an instance.
        /// </summary>
        /// <param name="epsgNumber">represents the coordinate reference system that defines the location together with the other two parameters</param>
        /// <param name="xLongitude">the coordinate position value representing the longitude or X or Easting</param>
        /// <param name="yLatitude">the coordinate position value representing the latitude or Y or Northing</param>
        """

        @classmethod
        def create_coordinate_by_epsg_number(cls,
            epsgNumber: int,
            yLatitude: float,
            xLongitude: float
        ) -> CrsCoordinate:
            crsProjection: CrsProjection = CrsProjectionFactory.get_crs_projection_by_epsg_number(epsgNumber)
            return cls.create_coordinate(crsProjection, yLatitude, xLongitude)

        """
        /// <summary>
        /// Factory method for creating an instance.
        /// See also <see cref="CrsProjection"/>
        /// </summary>
        /// <param name="crsProjection">represents the coordinate reference system that defines the location together with the other two parameters</param>
        /// <param name="xLongitude">the coordinate position value representing the longitude or X or Easting</param>
        /// <param name="yLatitude">the coordinate position value representing the latitude or Y or Northing</param>
        """

        @classmethod
        def create_coordinate(cls,
            crsProjection: CrsProjection,
            yLatitude: float,
            xLongitude: float
        ) -> CrsCoordinate:
            return CrsCoordinate(crsProjection, yLatitude, xLongitude)

        """
        # // ----------------------------------------------------------------------------------------------------------------------
        # // These five methods below was generated with Visual Studio 2019
        """

        """
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
        """
        #// These five methods above was generated with Visual Studio 2019
        # // ----------------------------------------------------------------------------------------------------------------------

        """
        /// <summary>
        /// Two examples of the string that can be returned:
        /// "CrsCoordinate [ X: 153369.673 , Y: 6579457.649 , CRS: SWEREF_99_18_00 ]"
        /// "CrsCoordinate [ Longitude: 18.059196 , Latitude: 59.330231 , CRS: WGS84 ]"
        /// </summary>
        """
        def __str__(self):
            crs: str = str(self.get_crs_projection()).upper()
            isWgs84: bool = self.get_crs_projection().is_wgs84()
            yOrLatitude: str = "Y"
            xOrLongitude: str = "X"
            if (isWgs84):
                yOrLatitude = "Latitude"
                xOrLongitude = "Longitude"
            return f"CrsCoordinate [ {yOrLatitude}: {self.get_latitude_y()} , {xOrLongitude}: {self.get_longitude_x()} , CRS: {crs} ]"
