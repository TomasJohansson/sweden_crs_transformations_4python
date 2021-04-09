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
from sweden_crs_transformations.crs_projection import CrsProjection

class CrsProjectionFactory:
    """
    | Class with methods for getting all projections, and for getting one projection by its EPSG number.
    | (since such custom methods can not be located within the CrsProjection enum type itself)
    """


    """
    private readonly static IDictionary<int, CrsProjection>
        mapWithAllCrsProjections = new Dictionary<int, CrsProjection>();
    static CrsProjectionFactory() {
        IList<CrsProjection> crsProjections = GetAllCrsProjections();
        foreach(CrsProjection crsProjection in crsProjections) {
            mapWithAllCrsProjections.Add(crsProjection.GetEpsgNumber(), crsProjection);
    """


    @staticmethod
    def get_crs_projection_by_epsg_number(epsg: int) -> CrsProjection:
        """
        | Factory method creating an enum 'CrsProjection' by its number (EPSG) value.
        | :param epsg: an EPSG number.
        | https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset
        | https://epsg.org
        | https://epsg.io
        """
        # TODO implement with a hashmap maybe ...
        for crs in CrsProjection:
            if crs.value == epsg:
                return crs
        raise ValueError(f"Could not find CrsProjection for EPSG {epsg}")

    @staticmethod
    def get_all_crs_projections() -> list[CrsProjection]:
        """
        | Convenience method for retrieving all the projections in a List.
        """
        crsProjections = []
        for crs in CrsProjection:
            crsProjections.append(crs)
        return crsProjections
