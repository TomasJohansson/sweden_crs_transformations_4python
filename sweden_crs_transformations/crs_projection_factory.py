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

using System;
using System.Collections.Generic;
using System.Linq;

namespace SwedenCrsTransformations {

    /// <summary>
    /// Class with methods for getting all projections, and for getting one projection by its EPSG number.
    /// (since such custom methods can not be located within the CrsProjection enum type itself)
    /// </summary>
    /// See also <see cref="CrsProjection"/>
    public static class CrsProjectionFactory {
    
        private readonly static IDictionary<int, CrsProjection>
            mapWithAllCrsProjections = new Dictionary<int, CrsProjection>();
        static CrsProjectionFactory() {
            IList<CrsProjection> crsProjections = GetAllCrsProjections();
            foreach(CrsProjection crsProjection in crsProjections) {
                mapWithAllCrsProjections.Add(crsProjection.GetEpsgNumber(), crsProjection);
            }  
        }

        /// <summary>
        /// Factory method creating an enum 'CrsProjection' by its number (EPSG) value.
        /// </summary>
        /// <param name="epsg">
        /// An EPSG number.
        /// https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
        /// https://epsg.org
        /// https://epsg.io
        /// </param>
        /// See also <see cref="CrsProjection"/>        
        public static CrsProjection GetCrsProjectionByEpsgNumber(int epsg) {
            if(mapWithAllCrsProjections.ContainsKey(epsg)) {
                return mapWithAllCrsProjections[epsg];
            }
            throw new ArgumentException("Could not find CrsProjection for EPSG " + epsg);
        }

        /// <summary>
        /// Convenience method for retrieving all the projections in a List.
        /// </summary>
        public static IList<CrsProjection> GetAllCrsProjections() {
            return ((CrsProjection[])Enum.GetValues(typeof(CrsProjection))).ToList();
        }
    }
}