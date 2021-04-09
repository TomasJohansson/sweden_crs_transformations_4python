from __future__ import annotations # without this the type hint (method annotation) '-> CrsCoordinate:' causes error:  NameError: name 'CrsCoordinate' is not defined
# from sweden_crs_transformations.crs_coordinate import CrsCoordinate # ImportError ... circular import
import enum

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


class CrsProjection(enum.Enum):
    """
    | Crs = Coordinate reference system.
    |
    | The integer values for these enums are the EPSG numbers for the corresponding coordinate reference systems.
    | There are three kind of coordinate systems supported and defined in this enum type below:
    |     WGS84
    |     SWEREF99 (the new Swedish grid, 13 versions, one national grid and 12 local projection zones)
    |     RT90 (the old Swedish grid, 6 local projection zones)
    | There are methods for the enum which can be used to determine one of the above three types.
    |
    | Regarding the mentioned EPSG numbers (the enum values), at the links below you may find some more information about "EPSG".
    | https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
    | https://epsg.org
    | https://epsg.io
    """

    WGS84 = 4326
    """
    | https://epsg.org/crs_4326/WGS-84.html
    | https://epsg.io/4326
    | https://spatialreference.org/ref/epsg/4326/
    | https://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS_84
    """

    SWEREF_99_TM = 3006  # national sweref99 CRS
    """
    | "SWEREF 99 TM" (with EPSG code 3006) is the new national projection.
    | https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/referenssystem/tvadimensionella-system/sweref-99-projektioner/
    | https://epsg.org/crs_3006/SWEREF99-TM.html
    | https://epsg.io/3006
    | https://spatialreference.org/ref/epsg/3006/
    """

    # local sweref99 systems (the new swedish national system):
    SWEREF_99_12_00 = 3007
    SWEREF_99_13_30 = 3008
    SWEREF_99_15_00 = 3009
    SWEREF_99_16_30 = 3010
    SWEREF_99_18_00 = 3011
    SWEREF_99_14_15 = 3012
    SWEREF_99_15_45 = 3013
    SWEREF_99_17_15 = 3014
    SWEREF_99_18_45 = 3015
    SWEREF_99_20_15 = 3016
    SWEREF_99_21_45 = 3017
    SWEREF_99_23_15 = 3018

    # local RT90 systems (the old swedish national system):
    RT90_7_5_GON_V = 3019
    RT90_5_0_GON_V = 3020

    RT90_2_5_GON_V = 3021
    """
    | https://epsg.org/crs_3021/RT90-2-5-gon-V.html
    | https://epsg.io/3021
    | https://spatialreference.org/ref/epsg/3021/
    """

    RT90_0_0_GON_V = 3022
    RT90_2_5_GON_O = 3023
    RT90_5_0_GON_O = 3024

    def get_epsg_number(self) -> int:
        # // the EPSG numbers have been used as the values in this enum
        return self.value

    def is_wgs84(self) -> bool:
        return self.value == CrsProjection.WGS84.value

    def is_sweref99(self) -> bool:
        epsg_number: int = self.get_epsg_number()
        return _EpsgConstant._epsgLowerValueForSweref <= epsg_number <= _EpsgConstant._epsgUpperValueForSweref

    def is_rt90(self) -> bool:
        epsg_number: int = self.get_epsg_number()
        return _EpsgConstant._epsgLowerValueForRT90 <= epsg_number <= _EpsgConstant._epsgUpperValueForRT90

    def create_coordinate(self,
                          y_latitude: float,
                          x_longitude: float
                          ) -> CrsCoordinate:  # requires 'from __future__ import annotations' at the top of the file
        """
        :param y_latitude: the coordinate position value representing the latitude or Y or Northing
        :param x_longitude: the coordinate position value representing the longitude or X or Easting
        :return: a coordinate (CrsCoordinate)
        """
        # the below 'from ... import' statement can not be at the top of the file since it causes error with circular import
        from sweden_crs_transformations.crs_coordinate import CrsCoordinate
        return CrsCoordinate.create_coordinate(self, y_latitude, x_longitude)

    def __str__(self):
        return f"{self.name}(EPSG:{self.get_epsg_number()})"

    @staticmethod
    def get_crs_projection_by_epsg_number(epsg_number: int) -> CrsProjection:
        """
        | Factory method creating an enum 'CrsProjection' by its number (EPSG) value.
        | https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
        | https://epsg.org
        | https://epsg.io
        :param epsg_number: an EPSG number.
        :return: a projection (CrsProjection) corresponding to the EPSG number
        """
        # TODO implement with a hashmap maybe ...
        for crs in CrsProjection:
            if crs.value == epsg_number:
                return crs
        raise ValueError(f"Could not find CrsProjection for EPSG {epsg_number}")

    @staticmethod
    def get_all_crs_projections() -> list[CrsProjection]:
        """
        | Convenience method for retrieving all the projections in a List.
        """
        crs_projections = []
        for crs in CrsProjection:
            crs_projections.append(crs)
        return crs_projections


# The class below is only intended for internal usage i.e. only used by the above class CrsProjection
class _EpsgConstant:
    _epsgLowerValueForSweref = 3006
    _epsgUpperValueForSweref = 3018
    _epsgLowerValueForRT90 = 3019
    _epsgUpperValueForRT90 = 3024
