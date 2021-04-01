from sweden_crs_transformations.crs_projection import CrsProjection

# this file was initially ported from C# extension methods to use Python monkey patching in this file
# but most of these functions/methods have now been moved directly into the Python 'class CrsProjection(enum.Enum)'

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
    /// Extension methods for the enum CrsProjection.
    /// See also <see cref="CrsProjection"/>
    /// </summary>
"""
# class CrsProjectionExtensions:

# private const int epsgForSweref99tm = 3006;
# epsgForSweref99tm: int = 3006

# //private const int epsgLowerValueForSwerefLocal = 3007; // the NATIONAL sweref99TM has value 3006 as in the above constant
# //private const int epsgUpperValueForSwerefLocal = 3018;
# private const int epsgLowerValueForSweref = epsgForSweref99tm;
# private const int epsgUpperValueForSweref = 3018;
# epsgLowerValueForSweref: int = epsgForSweref99tm
# epsgUpperValueForSweref: int = 3018


# private const int epsgLowerValueForRT90 = 3019;
# private const int epsgUpperValueForRT90 = 3024;
# epsgLowerValueForRT90: int = 3019
# epsgUpperValueForRT90: int = 3024

"""
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
"""

'''
this method below has now been moved directly into the file 'crs_projection.py'
def GetEpsgNumber(self) -> int :
    # // the EPSG numbers have been used as the values in this enum
    return self.value
CrsProjection.GetEpsgNumber = GetEpsgNumber
'''

"""
/// <summary>
/// True if the coordinate reference system is WGS84.
/// </summary>
"""
'''
this method below has now been moved directly into the file 'crs_projection.py'
def isWgs84(self) -> bool :
    return self.value == CrsProjection.wgs84.value
CrsProjection.IsWgs84 = isWgs84
'''

"""
/// <summary>
/// True if the coordinate reference system is a version of SWEREF99.
/// </summary>
"""
'''
this method below has now been moved directly into the file 'crs_projection.py'
def isSweref(self) -> bool :
    epsgNumber: int = self.GetEpsgNumber()
    return epsgLowerValueForSweref <= epsgNumber and epsgNumber <= epsgUpperValueForSweref
CrsProjection.IsSweref = isSweref
'''

"""
/// <summary>
/// True if the coordinate reference system is a version of RT90.
/// </summary>
"""
'''
this method below has now been moved directly into the file 'crs_projection.py'
def isRT90(self) -> bool :
    epsgNumber: int = self.GetEpsgNumber()
    return epsgLowerValueForRT90 <= epsgNumber and epsgNumber <= epsgUpperValueForRT90
CrsProjection.IsRT90 = isRT90
'''



'''
# TODO move this file driectly into the file 'crs_projection.py' and then this file 'crs_projection_extensions.py' can be deleted
public static CrsCoordinate CreateCoordinate(
    this CrsProjection crsProjection,
    double yLatitude,
    double xLongitude
) {
    return CrsCoordinate.CreateCoordinate(crsProjection, yLatitude, xLongitude);
'''
