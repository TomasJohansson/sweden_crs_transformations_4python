# sweden_crs_transformations_4python
'sweden_crs_transformations_4python' is a Python library ported from the
[C#.NET library 'sweden_crs_transformations_4net'](https://github.com/TomasJohansson/sweden_crs_transformations_4net/) and it is used for transforming geographic coordinates between the following three kind of CRS (Coordinate Reference Systems):  
WGS84, SWEREF99 and RT90.  
(13 versions of SWEREF99, and 6 versions of RT90)

# Code example
```python
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.crs_coordinate import CrsCoordinate

stockholmCentralStation_WGS84_latitude = 59.330231
stockholmCentralStation_WGS84_longitude = 18.059196

stockholmWGS84: CrsCoordinate = CrsCoordinate.create_coordinate(
    CrsProjection.WGS84,
    stockholmCentralStation_WGS84_latitude,
    stockholmCentralStation_WGS84_longitude
)

stockholmSweref99tm: CrsCoordinate = stockholmWGS84.transform(CrsProjection.SWEREF_99_TM)
print(f"stockholmSweref99tm X: {stockholmSweref99tm.get_longitude_x()}")  # Python 3.6+
print(f"stockholmSweref99tm Y: {stockholmSweref99tm.get_latitude_y()}")
print(f"stockholmSweref99tm as string: {str(stockholmSweref99tm)}")
'''
Output from the above:
stockholmSweref99tm X: 674032.357
stockholmSweref99tm Y: 6580821.991
stockholmSweref99tm as string: CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM(EPSG:3006) ]
'''

all_projections = CrsProjection.get_all_crs_projections()
for crs_projection in all_projections:
    print(stockholmWGS84.transform(crs_projection))
'''
Output from the above loop:
CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84(EPSG:4326) ]
CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM(EPSG:3006) ]
CrsCoordinate [ Y: 6595151.116 , X: 494604.69 , CRS: SWEREF_99_12_00(EPSG:3007) ]
CrsCoordinate [ Y: 6588340.147 , X: 409396.217 , CRS: SWEREF_99_13_30(EPSG:3008) ]
CrsCoordinate [ Y: 6583455.373 , X: 324101.998 , CRS: SWEREF_99_15_00(EPSG:3009) ]
CrsCoordinate [ Y: 6580494.921 , X: 238750.424 , CRS: SWEREF_99_16_30(EPSG:3010) ]
CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00(EPSG:3011) ]
CrsCoordinate [ Y: 6585657.12 , X: 366758.045 , CRS: SWEREF_99_14_15(EPSG:3012) ]
CrsCoordinate [ Y: 6581734.696 , X: 281431.616 , CRS: SWEREF_99_15_45(EPSG:3013) ]
CrsCoordinate [ Y: 6579735.93 , X: 196061.94 , CRS: SWEREF_99_17_15(EPSG:3014) ]
CrsCoordinate [ Y: 6579660.051 , X: 110677.129 , CRS: SWEREF_99_18_45(EPSG:3015) ]
CrsCoordinate [ Y: 6581507.028 , X: 25305.238 , CRS: SWEREF_99_20_15(EPSG:3016) ]
CrsCoordinate [ Y: 6585277.577 , X: -60025.629 , CRS: SWEREF_99_21_45(EPSG:3017) ]
CrsCoordinate [ Y: 6590973.148 , X: -145287.219 , CRS: SWEREF_99_23_15(EPSG:3018) ]
CrsCoordinate [ Y: 6598325.639 , X: 1884004.1 , CRS: RT90_7_5_GON_V(EPSG:3019) ]
CrsCoordinate [ Y: 6587493.237 , X: 1756244.287 , CRS: RT90_5_0_GON_V(EPSG:3020) ]
CrsCoordinate [ Y: 6580994.18 , X: 1628293.886 , CRS: RT90_2_5_GON_V(EPSG:3021) ]
CrsCoordinate [ Y: 6578822.84 , X: 1500248.374 , CRS: RT90_0_0_GON_V(EPSG:3022) ]
CrsCoordinate [ Y: 6580977.349 , X: 1372202.721 , CRS: RT90_2_5_GON_O(EPSG:3023) ]
CrsCoordinate [ Y: 6587459.595 , X: 1244251.702 , CRS: RT90_5_0_GON_O(EPSG:3024) ]
'''
```

# Accuracy of the transformations

This Python library is a port of the [C#.NET library 'sweden_crs_transformations_4net'](https://github.com/TomasJohansson/sweden_crs_transformations_4net/) and therefore it is using the same file "swedish_crs_coordinates.csv" as the C# library, for the regression testing of the Python implementation.  
There are 18 rows with coordinates in that file, and it will lead to 108 transformations being done when executing all Python tests, e.g. with the command 'py -3.9 -m unittest tests/coordinate_files/test_transforming_coordinates_from_file.py'.  
The coordinate values in the file have been created as median values from six different Java implementations of CRS transformations.  
For more information about the origin of the data file being used, please see the webpage linked above for the C# library 'sweden_crs_transformations_4net'.

# Origin of the mathematics used in the library

This Python library is ported from the C#.NET library ('sweden_crs_transformations_4net') which is based on [C# library MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/) which in turn is based on a [javascript library by Arnold Andreasson](https://latlong.mellifica.se/).  
The main part of 'MightyLittleGeodesy' which has been kept (to the C# library 'sweden_crs_transformations_4net') is the mathematical calculations in the class 'GaussKreuger.cs'.  
Regarding the port to this Python version 'sweden_crs_transformations_4python' then of course there had to be more modifications since Python has differences in syntax compared with C#, although
the mathematical logic has still been kept from the original 'MightyLittleGeodesy' class 'GaussKreuger.cs'.


# License

MIT.
'sweden_crs_transformations_4python' is ported from the C# library 'sweden_crs_transformations_4net'
which is also licensed with MIT since it started as a fork of the C# library 'MightyLittleGeodesy' which is licensed with the MIT license. (see below).  
[License text for 'sweden_crs_transformations_4python'](https://github.com/TomasJohansson/sweden_crs_transformations_4python/blob/python_SwedenCrsTransformations/LICENSE)

# License for the original C# repository [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/)

The text below has been copied from the above linked webpage:
> The calculations in this library is based on the excellent javascript library by Arnold Andreasson which is published under the Creative Commons license. However, as agreed with mr Andreasson, MightyLittleGeodesy is now licensed under the MIT license.

The text below has been copied from [one of the source files for MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/blob/83491fc6e7454f5d90d792610b317eca7a332334/MightyLittleGeodesy/Classes/GaussKreuger.cs).
```C#
/*
 * MightyLittleGeodesy
 * RT90, SWEREF99 and WGS84 coordinate transformation library
 *
 * Read my blog @ http://blog.sallarp.com
 *
 *
 * Copyright (C) 2009 Björn Sållarp
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this
 * software and associated documentation files (the "Software"), to deal in the Software
 * without restriction, including without limitation the rights to use, copy, modify,
 * merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 * BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 * DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
 ```
# Swedish coordinate reference systems
There are two kind of national CRS being used in Sweden:
The old [RT90](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/Referenssystem/Tvadimensionella-system/RT-90/) (six versions for different local regions)
The new [SWEREF99](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/gps-geodesi-och-swepos/referenssystem/tvadimensionella-system/sweref-99-projektioner/) (thirteen versions, one for the national "TM" and twelve local regions)

The above links are for pages in Swedish at the website for [Lantmäteriet](https://en.wikipedia.org/wiki/Lantm%C3%A4teriet) which is a swedish authority for mapping.

[https://www.lantmateriet.se/en/about-lantmateriet/about-lantmateriet/](https://www.lantmateriet.se/en/about-lantmateriet/about-lantmateriet/)
Quote from the above URL:
```Text
We map the country, demarcate boundaries and help guarantee secure ownership of Sweden’s real property.
You can get more information and documentation on Sweden’s geography and real properties from us.
```
