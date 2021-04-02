﻿"""
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
// This class was not part of the original 'MightyLittleGeodesy'
// but the class 'GaussKreuger' has later been changed to return this 'LatLon' instead of array 'double[]'
"""
class _LatLon:
    def __init__(self,latitudeY: float, longitudeX: float):
        self.latitudeY = latitudeY
        self.longitudeX = longitudeX
