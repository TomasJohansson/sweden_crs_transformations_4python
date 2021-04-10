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


class _LatLon:
    """
    | This class was not part of the original 'MightyLittleGeodesy'
    | but the class 'GaussKreuger' has later been changed to return this 'LatLon' instead of array 'double[]'
    """

    def __init__(self, latitude_y, longitude_x):
        self.latitude_y = latitude_y
        self.longitude_x = longitude_x
