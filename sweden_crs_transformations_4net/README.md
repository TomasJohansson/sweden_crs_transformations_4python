# sweden_crs_transformations_4net
'sweden_crs_transformations_4net' is a C#.NET library for transforming geographic coordinates between the following three kind of CRS (Coordinate Reference Systems): WGS84, SWEREF99 and RT90.
(13 versions of SWEREF99, and 6 versions of RT90)

The library is based on [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/) which in turn is based on a [javascript library by Arnold Andreasson](http://latlong.mellifica.se/).

The main part of 'MightyLittleGeodesy' which has been kept is the mathematical calculations in the class 'GaussKreuger.cs'.
(although some modifications have been done in the class [GaussKreuger](https://github.com/TomasJohansson/sweden_crs_transformations_4net/blob/csharpe_SwedenCrsTransformations/SwedenCrsTransformations/MightyLittleGeodesy/Classes/GaussKreuger.cs))

# NuGet release

No.  
I have currently not released it anywhere except from here at this github repository, and currently I have no plans of releasing it at NuGet neither.  
If you are looking for a NuGet library for transformation of coordinates, I can instead suggest that you try using my .NET library [crsTransformations-dotnet](https://github.com/TomasJohansson/crsTransformations-dotnet) with adapters for (currently) three implementation libraries (and one of those is 'MightyLittleGeodesy').  
That adapter library is implemented with F# but you can use it from C# too if you want.

Of course, if you are only interested in Swedish coordinate systems then you can also choose to use 
[MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy) (which is also [released to NuGet](https://www.nuget.org/packages/MightyLittleGeodesy/)) directly.  
The disadvantage (IMHO) with using 'MightyLittleGeodesy' directly is that the client API is not consistent in the sense that you need to use different classes (for WGS84, RT90, SWEREF99) 
and you can only directly transform to/from WGS84.  
For example if you want to transform between two SWEREF99 systems, then you have to (in your own client code) do it through an intermediate WGS84 transformation.  
See a code example further down below which compares the API for 'MightyLittleGeodesy' with this library 'sweden_crs_transformations_4net'.  

# Ports to other programming languages
Currently I have ported this C#.NET library to the following programming languages and github repositories:   
Dart: [sweden_crs_transformations_4dart](https://github.com/TomasJohansson/sweden_crs_transformations_4dart)   
TypeScript: [sweden_crs_transformations_4typescript](https://github.com/TomasJohansson/sweden_crs_transformations_4typescript)   
Java : [sweden_crs_transformations_4jvm](https://github.com/TomasJohansson/sweden_crs_transformations_4jvm)   

# Code example
Please note that the API is very different from the originally forked library.  
(the only significant part that remains from the forked library is the *internal implementation* using the GaussKreuger class).  
See a code example further down below which compares the API for 'MightyLittleGeodesy' vs this library 'sweden_crs_transformations_4net'.
```C#
using SwedenCrsTransformations;
using System;
using System.Collections.Generic;

...

const double stockholmCentralStation_WGS84_latitude = 59.330231; // https://kartor.eniro.se/m/XRCfh
const double stockholmCentralStation_WGS84_longitude = 18.059196;

CrsCoordinate stockholmWGS84 = CrsCoordinate.CreateCoordinate(
    CrsProjection.wgs84,
    stockholmCentralStation_WGS84_latitude,
    stockholmCentralStation_WGS84_longitude
);

CrsCoordinate stockholmSweref99tm = stockholmWGS84.Transform(CrsProjection.sweref_99_tm);
Console.WriteLine("stockholmSweref99tm X: " + stockholmSweref99tm.LongitudeX);
Console.WriteLine("stockholmSweref99tm Y: " + stockholmSweref99tm.LatitudeY);
Console.WriteLine("stockholmSweref99tm 'ToString': " + stockholmSweref99tm.ToString());
// Output from the above:
//stockholmSweref99tm X: 674032.357
//stockholmSweref99tm Y: 6580821.991
//stockholmSweref99tm 'ToString': CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM ]

IList<CrsProjection> allProjections = CrsProjectionFactory.GetAllCrsProjections();
foreach(var crsProjection in allProjections) {
    Console.WriteLine(stockholmWGS84.Transform(crsProjection));
}
// Output from the above loop:
//CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM ]
//CrsCoordinate [ Y: 6595151.116 , X: 494604.69 , CRS: SWEREF_99_12_00 ]
//CrsCoordinate [ Y: 6588340.147 , X: 409396.217 , CRS: SWEREF_99_13_30 ]
//CrsCoordinate [ Y: 6583455.373 , X: 324101.998 , CRS: SWEREF_99_15_00 ]
//CrsCoordinate [ Y: 6580494.921 , X: 238750.424 , CRS: SWEREF_99_16_30 ]
//CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00 ]
//CrsCoordinate [ Y: 6585657.12 , X: 366758.045 , CRS: SWEREF_99_14_15 ]
//CrsCoordinate [ Y: 6581734.696 , X: 281431.616 , CRS: SWEREF_99_15_45 ]
//CrsCoordinate [ Y: 6579735.93 , X: 196061.94 , CRS: SWEREF_99_17_15 ]
//CrsCoordinate [ Y: 6579660.051 , X: 110677.129 , CRS: SWEREF_99_18_45 ]
//CrsCoordinate [ Y: 6581507.028 , X: 25305.238 , CRS: SWEREF_99_20_15 ]
//CrsCoordinate [ Y: 6585277.577 , X: -60025.629 , CRS: SWEREF_99_21_45 ]
//CrsCoordinate [ Y: 6590973.148 , X: -145287.219 , CRS: SWEREF_99_23_15 ]
//CrsCoordinate [ Y: 6598325.639 , X: 1884004.1 , CRS: RT90_7_5_GON_V ]
//CrsCoordinate [ Y: 6587493.237 , X: 1756244.287 , CRS: RT90_5_0_GON_V ]
//CrsCoordinate [ Y: 6580994.18 , X: 1628293.886 , CRS: RT90_2_5_GON_V ]
//CrsCoordinate [ Y: 6578822.84 , X: 1500248.374 , CRS: RT90_0_0_GON_V ]
//CrsCoordinate [ Y: 6580977.349 , X: 1372202.721 , CRS: RT90_2_5_GON_O ]
//CrsCoordinate [ Y: 6587459.595 , X: 1244251.702 , CRS: RT90_5_0_GON_O ]
//CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84 ]
```

# API difference between the forked library 'MightyLittleGeodesy' and this library 'sweden_crs_transformations_4net'

The example below shows how to transform from a RT90 coordinate ('RT90 2.5 gon v' is the default in the below 'RT90Position' constructor) to SWEREF99 TM.

Code example from the homepage of [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/):
```C#
RT90Position rt90Pos = new RT90Position(6583052, 1627548);
SWEREF99Position sweRef = new SWEREF99Position(rt90Pos.ToWGS84(), SWEREF99Position.SWEREFProjection.sweref_99_tm);
```
Code example for doing the same transformation with this library 'sweden_crs_transformations_4net':
```C#
CrsCoordinate rt90Pos = CrsCoordinate.CreateCoordinate(CrsProjection.rt90_2_5_gon_v, 6583052, 1627548);
CrsCoordinate sweRef = rt90Pos.Transform(CrsProjection.sweref_99_tm);
```
The RT90 (2,5 gon V) coordinate used in the above example:
```Text
https://kartor.eniro.se/m/3w33L
WGS84 decimal (lat, lon)        59.348915, 18.047319
RT90 (northing, easting)        6583052, 1627548
SWEREF99 TM (northing, easting) 6582870, 673262
```

# Accuracy of the transformations

The transformations have been verified by using coordinates from a test file "swedish_crs_coordinates.csv".  
That test file were copied from another project of mine which had created it by using six different Java implementations of transformations.  
See these URL's below for that file and the Java code that created it:  
[https://github.com/TomasJohansson/crsTransformations/ ... /swedish_crs_coordinates.csv](https://github.com/TomasJohansson/crsTransformations/blob/a1da6c74daf040a521beb32f9f395124ffe76aa6/crs-transformation-adapter-test/src/test/resources/generated/swedish_crs_coordinates.csv  )   
[https://github.com/TomasJohansson/crsTransformations/ ...  /CoordinateTestDataGeneratedFromEpsgDatabaseTest.java (method createFileWithTransformationResultsForCoordinatesInSweden())](https://github.com/TomasJohansson/crsTransformations/blob/173ba6c35f045ac906da5b28dfa8bbff97d037fb/crs-transformation-adapter-test/src/test/java/com/programmerare/com/programmerare/testData/CoordinateTestDataGeneratedFromEpsgDatabaseTest.java#L671)

When I had forked 'MightyLittleGeodesy' I created a test method which asserted 108 transformations from the 18 data rows in that file.  
See the the test class 'TransformingCoordinatesFromFileTest.cs' and the class 'Transformer' (which uses the original MightyLittleGeodesy classes 'SWEREF99Position', RT90Position', and 'WGS84Position' for the transformations, in [git commit 135e54](https://github.com/TomasJohansson/sweden_crs_transformations_4net/commit/135e543dc8ae7fd7b8c7be9fc0f034896daea7b4).  
Later versions of [Transformer](https://github.com/TomasJohansson/sweden_crs_transformations_4net/blob/csharpe_SwedenCrsTransformations/SwedenCrsTransformations/Transformation/Transformer.cs) does **not** use those three 'Position' subclasses at all but they are instead using the class 'GaussKreuger' (from 'MightyLittleGeodesy') from within two [implementations of a 'TransformStrategy' interface](https://github.com/TomasJohansson/sweden_crs_transformations_4net/tree/csharpe_SwedenCrsTransformations/SwedenCrsTransformations/Transformation).    
Regression testing have been done continously by using the above mentioned 'TransformingCoordinatesFromFileTest.cs'.  


# License

MIT.   
'SwedenCrsTransformations' started as a fork of 'MightyLittleGeodesy' and it is licensed with the MIT license just like 'MightyLittleGeodesy' (see below).  
[License text for 'sweden_crs_transformations_4net'](https://github.com/TomasJohansson/sweden_crs_transformations_4net/blob/csharpe_SwedenCrsTransformations/LICENSE)

# License for the forked repository [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/)

The text below has been copied from the above webpage (the forked repository):
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