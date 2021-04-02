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
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation.transform_strategy import _TransformStrategy


class Transformer:
    pass
    """

    # Implementations of transformations from WGS84:
    private static readonly TransformStrategy _transformStrategy_from_WGS84_to_SWEREF99_or_RT90 = new TransformStrategy_from_WGS84_to_SWEREF99_or_RT90();

    # Implementations of transformations to WGS84:
    private static readonly TransformStrategy _transformStrategy_from_SWEREF99_or_RT90_to_WGS84 = new TransformStrategy_from_SWEREF99_or_RT90_to_WGS84();

    # Implementation first transforming to WGS84 and then to the real target:
    private static readonly TransformStrategy _transFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget  = new TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget();

    @staticmethod
    transform(sourceCoordinate: CrsCoordinate, targetCrsProjection: CrsProjection) -> CrsCoordinate:
        if(sourceCoordinate.CrsProjection == targetCrsProjection):
            return sourceCoordinate

        _transFormStrategy: _TransformStrategy = null

        # Transform FROM wgs84:
        if(
            sourceCoordinate.CrsProjection.is_wgs84()
            and
            ( targetCrsProjection.is_sweref99() || targetCrsProjection.is_rt90() )
        ):
            _transFormStrategy = _transformStrategy_from_WGS84_to_SWEREF99_or_RT90

        # Transform TO wgs84:
        elif(
            targetCrsProjection.is_wgs84()
            and
            ( sourceCoordinate.CrsProjection.is_sweref99() || sourceCoordinate.CrsProjection.is_rt90() )
        ):
            _transFormStrategy = _transformStrategy_from_SWEREF99_or_RT90_to_WGS84

        # Transform between two non-wgs84:
        elif(
            ( sourceCoordinate.CrsProjection.is_sweref99() || sourceCoordinate.CrsProjection.is_rt90() )
            and
            ( targetCrsProjection.is_sweref99() || targetCrsProjection.is_rt90() )
        ):
            # the only direct transform supported is to/from WGS84, so therefore first transform to wgs84
            _transFormStrategy = _transFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget

        if(_transFormStrategy != null):
            return _transFormStrategy.transform(sourceCoordinate, targetCrsProjection)

        raise ValueError(f"Unhandled source/target projection transformation: {sourceProjection} ==> {targetCrsProjection}")
    """
