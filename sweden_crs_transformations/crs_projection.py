import enum
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

"""
/// <summary>
/// Crs = Coordinate reference system.
///
/// The integer values for these enums are the EPSG numbers for the corresponding coordinate reference systems.
/// There are three kind of coordinate systems supported and defined in this enum type below:
///     WGS84
///     SWEREF99 (the new Swedish grid, 13 versions, one national grid and 12 local projection zones)
///     RT90 (the old Swedish grid, 6 local projection zones)
/// There are extensions methods for the enum which can be used to determine one of the above three types.
/// See also <see cref="CrsProjectionExtensions"/>
///
/// Regarding the mentioned EPSG numbers (the enum values), at the links below you may find some more information about "EPSG".
/// https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
/// https://epsg.org
/// https://epsg.io
/// </summary>
"""


class CrsProjection(enum.Enum):
    """
    /// <summary>
    /// https://epsg.org/crs_4326/WGS-84.html
    /// https://epsg.io/4326
    /// https://spatialreference.org/ref/epsg/4326/
    /// https://en.wikipedia.org/wiki/World_Geodetic_System#A_new_World_Geodetic_System:_WGS_84
    /// </summary>
    """
    WGS84 = 4326

    """
    /// <summary>
    /// "SWEREF 99 TM" (with EPSG code 3006) is the new national projection.
    /// https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/referenssystem/tvadimensionella-system/sweref-99-projektioner/
    /// https://epsg.org/crs_3006/SWEREF99-TM.html
    /// https://epsg.io/3006
    /// https://spatialreference.org/ref/epsg/3006/
    /// </summary>
    """
    SWEREF_99_TM = 3006 # national sweref99 CRS

    """
    // local sweref99 systems (the new swedish national system):
    """
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

    """
    // local RT90 systems (the old swedish national system):
    """
    RT90_7_5_GON_V = 3019
    RT90_5_0_GON_V = 3020

    """
    /// <summary>
    /// https://epsg.org/crs_3021/RT90-2-5-gon-V.html
    /// https://epsg.io/3021
    /// https://spatialreference.org/ref/epsg/3021/
    /// </summary>
    """
    RT90_2_5_GON_V = 3021

    RT90_0_0_GON_V = 3022
    RT90_2_5_GON_O = 3023
    RT90_5_0_GON_O = 3024

    def get_epsg_number(self) -> int:
        # // the EPSG numbers have been used as the values in this enum
        return self.value

    def is_wgs84(self) -> bool:
        return self.value == CrsProjection.WGS84.value

    def is_sweref99(self) -> bool:
        epsgNumber: int = self.get_epsg_number()
        return _EpsgConstant._epsgLowerValueForSweref <= epsgNumber <= _EpsgConstant._epsgUpperValueForSweref

    def is_rt90(self) -> bool:
        epsgNumber: int = self.get_epsg_number()
        return _EpsgConstant._epsgLowerValueForRT90 <= epsgNumber <= _EpsgConstant._epsgUpperValueForRT90

    def __str__(self):
        return f"{self.name}(EPSG:{self.get_epsg_number()})"


# The class below is only intended for internal usage i.e. only used by the above class CrsProjection
class _EpsgConstant:
    _epsgLowerValueForSweref = 3006
    _epsgUpperValueForSweref = 3018
    _epsgLowerValueForRT90 = 3019
    _epsgUpperValueForRT90 = 3024

