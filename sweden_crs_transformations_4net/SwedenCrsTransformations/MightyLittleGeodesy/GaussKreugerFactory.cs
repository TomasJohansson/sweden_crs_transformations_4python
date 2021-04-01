using SwedenCrsTransformations;
using System;
using System.Collections.Generic;

namespace MightyLittleGeodesy {
    internal class GaussKreugerFactory {

        private static readonly GaussKreugerFactory _gaussKreugerFactory = new GaussKreugerFactory();
    
        internal static GaussKreugerFactory getInstance() {
            return _gaussKreugerFactory;
        }

        private readonly IDictionary<CrsProjection, GaussKreuger>
            mapWithAllGaussKreugers = new Dictionary<CrsProjection, GaussKreuger>();

        private GaussKreugerFactory() {
            IList<CrsProjection> crsProjections = CrsProjectionFactory.GetAllCrsProjections();
            foreach(CrsProjection crsProjection in crsProjections) {
                GaussKreugerParameterObject gaussKreugerParameterObject = new GaussKreugerParameterObject(crsProjection);
                GaussKreuger gaussKreuger = GaussKreuger.create(gaussKreugerParameterObject);
                mapWithAllGaussKreugers.Add(crsProjection, gaussKreuger);
            }        
        }
    
        internal GaussKreuger getGaussKreuger(CrsProjection crsProjection) {
            if(mapWithAllGaussKreugers.ContainsKey(crsProjection)) {
                return mapWithAllGaussKreugers[crsProjection];
            }
            throw new ArgumentException("Could not find GaussKreuger for crsProjection " + crsProjection);
        }

    }
}