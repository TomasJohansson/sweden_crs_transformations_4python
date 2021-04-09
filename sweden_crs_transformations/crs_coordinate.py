from __future__ import annotations
# without the above "from __future__ import annotations" a method in the class CrsCoordinate
# can not define (with type hinting)  a method to return a CrsCoordinate i.e. an instance from the same class
from sweden_crs_transformations.crs_projection_factory import CrsProjectionFactory

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
from sweden_crs_transformations.crs_projection import CrsProjection

class CrsCoordinate:
    """
    | Coordinate, defined by the three parameters for the factory methods.
    """

    def __init__(self,
        crsProjection: CrsProjection,
        yLatitude: float,
        xLongitude: float
    ):
        """
        | Client code can instead use the factory class methods.
        """
        self._crsProjection = crsProjection
        self._yLatitude = yLatitude
        self._xLongitude = xLongitude

    @classmethod
    def create_coordinate(cls,
        crsProjection: CrsProjection,
        yLatitude: float,
        xLongitude: float
    ) -> CrsCoordinate:
        """
        | Factory method for creating an instance.
        | :param crsProjection: represents the coordinate reference system that defines the location together with the other two parameters
        | :param yLatitude: the coordinate position value representing the latitude or Y or Northing
        | :param xLongitude: the coordinate position value representing the longitude or X or Easting
        """
        return cls(crsProjection, yLatitude, xLongitude)

    @classmethod
    def create_coordinate_by_epsg_number(cls,
        epsgNumber: int,
        yLatitude: float,
        xLongitude: float
    ) -> CrsCoordinate:
        """
        | Factory method for creating an instance.
        | :param epsgNumber: represents the coordinate reference system that defines the location together with the other two parameters
        | :param yLatitude: the coordinate position value representing the latitude or Y or Northing
        | :param xLongitude: the coordinate position value representing the longitude or X or Easting
        """
        crsProjection: CrsProjection = CrsProjectionFactory.get_crs_projection_by_epsg_number(epsgNumber)
        return cls.create_coordinate(crsProjection, yLatitude, xLongitude)

    def get_crs_projection(self) -> CrsProjection:
        """
        | The coordinate reference system that defines the location together with the other two properties (LongitudeX and LatitudeY).
        """
        return self._crsProjection

    def get_longitude_x(self) -> float:
        """
        | The coordinate value representing the longitude or X or Easting.
        """
        return self._xLongitude

    def get_latitude_y(self) -> float:
        """
        | The coordinate value representing the latitude or Y or Northing.
        """
        return self._yLatitude

    def transform(self, targetCrsProjection: CrsProjection) -> CrsCoordinate:
        """
        | Transforms the coordinate to another coordinate reference system
        | :param targetCrsProjection: the coordinate reference system that you want to transform to
        """
        from sweden_crs_transformations.transformation.transformer import Transformer
        return Transformer.transform(self, targetCrsProjection)

    def transform_by_epsg_number(self, targetEpsgNumber: int) -> CrsCoordinate:
        """
        | Transforms the coordinate to another coordinate reference system
        | :param targetEpsgNumber: the coordinate reference system that you want to transform to
        """
        targetCrsProjection: CrsProjection = CrsProjectionFactory.get_crs_projection_by_epsg_number(targetEpsgNumber)
        return self.transform(targetCrsProjection)


    def __str__(self):
        """
        | Two examples of the string that can be returned:
        | "CrsCoordinate [ X: 153369.673 , Y: 6579457.649 , CRS: SWEREF_99_18_00 ]"
        | "CrsCoordinate [ Longitude: 18.059196 , Latitude: 59.330231 , CRS: WGS84 ]"
        """
        crs: str = str(self.get_crs_projection()).upper()
        isWgs84: bool = self.get_crs_projection().is_wgs84()
        yOrLatitude: str = "Y"
        xOrLongitude: str = "X"
        if (isWgs84):
            yOrLatitude = "Latitude"
            xOrLongitude = "Longitude"
        return f"CrsCoordinate [ {yOrLatitude}: {self.get_latitude_y()} , {xOrLongitude}: {self.get_longitude_x()} , CRS: {crs} ]"


    """
    # // ----------------------------------------------------------------------------------------------------------------------
    # C#.NET code:

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

