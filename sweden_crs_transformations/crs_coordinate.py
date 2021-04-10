from __future__ import annotations
from typing import Final  # https://www.python.org/dev/peps/pep-0591/

# without the above "from __future__ import annotations" a method in the class CrsCoordinate
# can not define (with type hinting)  a method to return a CrsCoordinate i.e. an instance from the same class

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
                 crs_projection: CrsProjection,
                 y_latitude: float,
                 x_longitude: float
                 ):
        """
        | Client code can instead use the factory class methods.
        """
        self._crsProjection: Final[CrsProjection] = crs_projection
        self._y_latitude: Final[float] = y_latitude
        self._x_longitude: Final[float] = x_longitude

    @classmethod
    def create_coordinate(cls,
                          crs_projection: CrsProjection,
                          y_latitude: float,
                          x_longitude: float
                          ) -> CrsCoordinate:
        """
        | Factory method for creating an instance.
        :param crs_projection: represents the coordinate reference system that defines the location together with the other two parameters
        :param y_latitude: the coordinate position value representing the latitude or Y or Northing
        :param x_longitude: the coordinate position value representing the longitude or X or Easting
        :return: a coordinate (CrsCoordinate)
        """
        return cls(crs_projection, y_latitude, x_longitude)

    @classmethod
    def create_coordinate_by_epsg_number(cls,
                                         epsg_number: int,
                                         y_latitude: float,
                                         x_longitude: float
                                         ) -> CrsCoordinate:
        """
        | Factory method for creating an instance.
        :param epsg_number: represents the coordinate reference system that defines the location together with the other two parameters
        :param y_latitude: the coordinate position value representing the latitude or Y or Northing
        :param x_longitude: the coordinate position value representing the longitude or X or Easting
        :return: a coordinate (CrsCoordinate)
        """
        crs_projection: CrsProjection = CrsProjection.get_crs_projection_by_epsg_number(epsg_number)
        return cls.create_coordinate(crs_projection, y_latitude, x_longitude)

    def get_crs_projection(self) -> CrsProjection:
        """
        | The coordinate reference system that defines the location together with the other two properties (LongitudeX and LatitudeY).
        """
        return self._crsProjection

    def get_longitude_x(self) -> float:
        """
        | The coordinate value representing the longitude or X or Easting.
        """
        return self._x_longitude

    def get_latitude_y(self) -> float:
        """
        | The coordinate value representing the latitude or Y or Northing.
        """
        return self._y_latitude

    def transform(self, target_crs_projection: CrsProjection) -> CrsCoordinate:
        """
        | Transforms the coordinate to another coordinate reference system
        :param target_crs_projection: the coordinate reference system that you want to transform to
        :return: a coordinate (CrsCoordinate)
        """
        from sweden_crs_transformations.transformation._transformer import _Transformer
        return _Transformer.transform(self, target_crs_projection)

    def transform_by_epsg_number(self, target_epsg_number: int) -> CrsCoordinate:
        """
        | Transforms the coordinate to another coordinate reference system
        :param target_epsg_number: the coordinate reference system that you want to transform to
        :return: a coordinate (CrsCoordinate)
        """
        target_crs_projection: CrsProjection = CrsProjection.get_crs_projection_by_epsg_number(target_epsg_number)
        return self.transform(target_crs_projection)

    def __str__(self):
        """
        | Two examples of the string that can be returned:
        | "CrsCoordinate [ X: 153369.673 , Y: 6579457.649 , CRS: SWEREF_99_18_00 ]"
        | "CrsCoordinate [ Longitude: 18.059196 , Latitude: 59.330231 , CRS: WGS84 ]"
        """
        crs: str = str(self.get_crs_projection()).upper()
        is_wgs84: bool = self.get_crs_projection().is_wgs84()
        y_or_latitude: str = "Y"
        x_or_longitude: str = "X"
        if is_wgs84:
            y_or_latitude = "Latitude"
            x_or_longitude = "Longitude"

        # Python 3.6+
        # return f"CrsCoordinate [ {y_or_latitude}: {self.get_latitude_y()} , {x_or_longitude}: {self.get_longitude_x()} , CRS: {crs} ]"
        # The below works with older Python versions e.g. 2.7
        return "CrsCoordinate [ " + str(y_or_latitude)+ ": " + str(self.get_latitude_y())+ " , " + str(x_or_longitude) + ": " + str(self.get_longitude_x()) + " , CRS: " + str(crs) + " ]"


    def __hash__(self):
        return hash((self.get_longitude_x(), self.get_latitude_y(), self.get_crs_projection()))

    def __eq__(self, other):
        if (type(self) != type(other)):
            return False
        return self.get_longitude_x() == other.get_longitude_x() and self.get_latitude_y() == other.get_latitude_y() and self.get_crs_projection() == other.get_crs_projection()
