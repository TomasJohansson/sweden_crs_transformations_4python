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

// This project is based on the library [MightyLittleGeodesy](https://github.com/bjornsallarp/MightyLittleGeodesy/)
// It started as a fork, but then most of the original code is gone.
// The main part that is still used is this file with the mathematical calculations i.e. the file "GaussKreuger.cs"
// Although there has been some modifications of this file too, as mentioned below.

// https://github.com/bjornsallarp/MightyLittleGeodesy/blob/83491fc6e7454f5d90d792610b317eca7a332334/MightyLittleGeodesy/Classes/GaussKreuger.cs
// The original version of the below class 'GaussKreuger' is located at the above URL.
// That original version has been modified below in this file below but not in a significant way (e.g. the mathematical calculations has not been modified).
// The modifications:
//      - changed the class from public to internal i.e. "public class GaussKreuger" ==> "internal class GaussKreuger"
//      - a new 'LatLon' class is used as return type from two methods instead of returning an array "double[]"
//              i.e. the two method signatures have changed as below:
//              "public double[] geodetic_to_grid(double latitude, double longitude)"  ==> "public LatLon geodetic_to_grid(double latitude, double longitude)"
//              "public double[] grid_to_geodetic(double x, double y)" ==> "public LatLon grid_to_geodetic(double yLatitude, double xLongitude)"
//      - renamed and changed order of the parameters for the method "grid_to_geodetic" (see the above line)
//      - changed the method "swedish_params" to use an enum as parameter instead of string, i.e. the method signature changed as below:
//              "public void swedish_params(string projection)" ==> "public void swedish_params(CrsProjection projection)"
//      - now the if/else statements in the implementation of the above method "swedish_params" compares with the enum values for CrsProjection instead of comparing with string literals
//      - removed the if/else statements in the above method "swedish_params" which used the projection strings beginning with "bessel_rt90"
//      - updated the GaussKreuger class to be immutable with readonly fields, and the methods (e.g. the above mentioned method "swedish_params") that 
//          previously initialized (mutated) the fields have instead been moved to another class and is provided as a 
//          parameter object to the constructor which copies the values into the readonly fields.   
// 
// For more details about exactly what has changed in this GaussKreuger class, you can also use a git client with "compare" or "blame" features to see the changes)

// ------------------------------------------------------------------------------------------
// The below comment block is kept from the original source file (see the above github URL)
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
// ------------------------------------------------------------------------------------------

using System;

namespace MightyLittleGeodesy {
    /*
     * .NET-implementation of "Gauss Conformal Projection 
     * (Transverse Mercator), Krügers Formulas".
     * - Parameters for SWEREF99 lat-long to/from RT90 and SWEREF99 
     * coordinates (RT90 and SWEREF99 are used in Swedish maps).
     * 
     * The calculations are based entirely on the excellent
     * javscript library by Arnold Andreassons.
     * Source: http://www.lantmateriet.se/geodesi/
     * Source: Arnold Andreasson, 2007. http://mellifica.se/konsult
     * Author: Björn Sållarp. 2009. http://blog.sallarp.com
     * 
     * Some modifications in this file were made 2021 by Tomas Johansson.
     * For details about changes, you should be able to use the github repository to see the git history where you found this source code file.
     */

    internal class GaussKreuger
    {
        // Immutable class with all fields 'readonly'
        private readonly double axis; // Semi-major axis of the ellipsoid.
        private readonly double flattening; // Flattening of the ellipsoid.
        private readonly double central_meridian; // Central meridian for the projection.    
        private readonly double scale; // Scale on central meridian.
        private readonly double false_northing; // Offset for origo.
        private readonly double false_easting; // Offset for origo.
        private GaussKreuger(GaussKreugerParameterObject gaussKreugerParameterObject) {
            this.axis = gaussKreugerParameterObject.axis;
            this.flattening = gaussKreugerParameterObject.flattening;
            this.central_meridian = gaussKreugerParameterObject.central_meridian;
            this.scale = gaussKreugerParameterObject.scale;
            this.false_northing = gaussKreugerParameterObject.false_northing;
            this.false_easting = gaussKreugerParameterObject.false_easting;
        }
        public static GaussKreuger create(GaussKreugerParameterObject gaussKreugerParameterObject) {
            GaussKreuger gaussKreuger = new GaussKreuger(gaussKreugerParameterObject);
            return gaussKreuger;
        }

        // Conversion from geodetic coordinates to grid coordinates.
        public LatLon geodetic_to_grid(double latitude, double longitude) // public double[] geodetic_to_grid(double latitude, double longitude)
        {
            double[] x_y = new double[2];

            // Prepare ellipsoid-based stuff.
            double e2 = flattening * (2.0 - flattening);
            double n = flattening / (2.0 - flattening);
            double a_roof = axis / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0);
            double A = e2;
            double B = (5.0 * e2 * e2 - e2 * e2 * e2) / 6.0;
            double C = (104.0 * e2 * e2 * e2 - 45.0 * e2 * e2 * e2 * e2) / 120.0;
            double D = (1237.0 * e2 * e2 * e2 * e2) / 1260.0;
            double beta1 = n / 2.0 - 2.0 * n * n / 3.0 + 5.0 * n * n * n / 16.0 + 41.0 * n * n * n * n / 180.0;
            double beta2 = 13.0 * n * n / 48.0 - 3.0 * n * n * n / 5.0 + 557.0 * n * n * n * n / 1440.0;
            double beta3 = 61.0 * n * n * n / 240.0 - 103.0 * n * n * n * n / 140.0;
            double beta4 = 49561.0 * n * n * n * n / 161280.0;

            // Convert.
            double deg_to_rad = Math.PI / 180.0;
            double phi = latitude * deg_to_rad;
            double lambda = longitude * deg_to_rad;
            double lambda_zero = central_meridian * deg_to_rad;

            double phi_star = phi - Math.Sin(phi) * Math.Cos(phi) * (A +
                            B * Math.Pow(Math.Sin(phi), 2) +
                            C * Math.Pow(Math.Sin(phi), 4) +
                            D * Math.Pow(Math.Sin(phi), 6));
            double delta_lambda = lambda - lambda_zero;
            double xi_prim = Math.Atan(Math.Tan(phi_star) / Math.Cos(delta_lambda));
            double eta_prim = math_atanh(Math.Cos(phi_star) * Math.Sin(delta_lambda));
            double x = scale * a_roof * (xi_prim +
                            beta1 * Math.Sin(2.0 * xi_prim) * math_cosh(2.0 * eta_prim) +
                            beta2 * Math.Sin(4.0 * xi_prim) * math_cosh(4.0 * eta_prim) +
                            beta3 * Math.Sin(6.0 * xi_prim) * math_cosh(6.0 * eta_prim) +
                            beta4 * Math.Sin(8.0 * xi_prim) * math_cosh(8.0 * eta_prim)) +
                            false_northing;
            double y = scale * a_roof * (eta_prim +
                            beta1 * Math.Cos(2.0 * xi_prim) * math_sinh(2.0 * eta_prim) +
                            beta2 * Math.Cos(4.0 * xi_prim) * math_sinh(4.0 * eta_prim) +
                            beta3 * Math.Cos(6.0 * xi_prim) * math_sinh(6.0 * eta_prim) +
                            beta4 * Math.Cos(8.0 * xi_prim) * math_sinh(8.0 * eta_prim)) +
                            false_easting;
            x_y[0] = Math.Round(x * 1000.0) / 1000.0;
            x_y[1] = Math.Round(y * 1000.0) / 1000.0;
            var latLon = new LatLon(x_y[0], x_y[1]);
            return latLon;
        }

        // Conversion from grid coordinates to geodetic coordinates.
        
        public LatLon grid_to_geodetic(double yLatitude, double xLongitude) // public double[] grid_to_geodetic(double yLatitude, double xLongitude)
        {
            double[] lat_lon = new double[2];
            if (central_meridian == double.MinValue)
            {
                return new LatLon(lat_lon[1], lat_lon[0]);
            }
            // Prepare ellipsoid-based stuff.
            double e2 = flattening * (2.0 - flattening);
            double n = flattening / (2.0 - flattening);
            double a_roof = axis / (1.0 + n) * (1.0 + n * n / 4.0 + n * n * n * n / 64.0);
            double delta1 = n / 2.0 - 2.0 * n * n / 3.0 + 37.0 * n * n * n / 96.0 - n * n * n * n / 360.0;
            double delta2 = n * n / 48.0 + n * n * n / 15.0 - 437.0 * n * n * n * n / 1440.0;
            double delta3 = 17.0 * n * n * n / 480.0 - 37 * n * n * n * n / 840.0;
            double delta4 = 4397.0 * n * n * n * n / 161280.0;

            double Astar = e2 + e2 * e2 + e2 * e2 * e2 + e2 * e2 * e2 * e2;
            double Bstar = -(7.0 * e2 * e2 + 17.0 * e2 * e2 * e2 + 30.0 * e2 * e2 * e2 * e2) / 6.0;
            double Cstar = (224.0 * e2 * e2 * e2 + 889.0 * e2 * e2 * e2 * e2) / 120.0;
            double Dstar = -(4279.0 * e2 * e2 * e2 * e2) / 1260.0;

            // Convert.
            double deg_to_rad = Math.PI / 180;
            double lambda_zero = central_meridian * deg_to_rad;
            double xi = (yLatitude - false_northing) / (scale * a_roof);
            double eta = (xLongitude - false_easting) / (scale * a_roof);
            double xi_prim = xi -
                            delta1 * Math.Sin(2.0 * xi) * math_cosh(2.0 * eta) -
                            delta2 * Math.Sin(4.0 * xi) * math_cosh(4.0 * eta) -
                            delta3 * Math.Sin(6.0 * xi) * math_cosh(6.0 * eta) -
                            delta4 * Math.Sin(8.0 * xi) * math_cosh(8.0 * eta);
            double eta_prim = eta -
                            delta1 * Math.Cos(2.0 * xi) * math_sinh(2.0 * eta) -
                            delta2 * Math.Cos(4.0 * xi) * math_sinh(4.0 * eta) -
                            delta3 * Math.Cos(6.0 * xi) * math_sinh(6.0 * eta) -
                            delta4 * Math.Cos(8.0 * xi) * math_sinh(8.0 * eta);
            double phi_star = Math.Asin(Math.Sin(xi_prim) / math_cosh(eta_prim));
            double delta_lambda = Math.Atan(math_sinh(eta_prim) / Math.Cos(xi_prim));
            double lon_radian = lambda_zero + delta_lambda;
            double lat_radian = phi_star + Math.Sin(phi_star) * Math.Cos(phi_star) *
                            (Astar +
                             Bstar * Math.Pow(Math.Sin(phi_star), 2) +
                             Cstar * Math.Pow(Math.Sin(phi_star), 4) +
                             Dstar * Math.Pow(Math.Sin(phi_star), 6));
            lat_lon[0] = lat_radian * 180.0 / Math.PI;
            lat_lon[1] = lon_radian * 180.0 / Math.PI;
            var latLon = new LatLon(lat_lon[0], lat_lon[1]);
            return latLon;
        }


        private double math_sinh(double value) {
            return 0.5 * (Math.Exp(value) - Math.Exp(-value));
        }
        private double math_cosh(double value) {
            return 0.5 * (Math.Exp(value) + Math.Exp(-value));
        }
        private double math_atanh(double value) {
            return 0.5 * Math.Log((1.0 + value) / (1.0 - value));
        }

    }
}

