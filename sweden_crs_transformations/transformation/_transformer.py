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
from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.transformation._transform_strategy import _TransformStrategy
from sweden_crs_transformations.transformation._transform_strategy_from_sweref99_or_rt90_to_wgs84 import _TransformStrategy_from_SWEREF99_or_RT90_to_WGS84
from sweden_crs_transformations.transformation._transform_strategy_from_sweref99_or_rt90_to_wgs84_and_then_to_real_target import _TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget
from sweden_crs_transformations.transformation._transform_strategy_from_wgs84_to_sweref99_or_rt90 import _TransformStrategy_from_WGS84_to_SWEREF99_or_RT90


class _Transformer:

    # Implementations of transformations from WGS84:
    transformStrategy_From_WGS84_to_SWEREF99_or_RT90 = _TransformStrategy_from_WGS84_to_SWEREF99_or_RT90()


    # Implementations of transformations to WGS84:
    transformStrategy_From_SWEREF99_or_RT90_to_WGS84 = _TransformStrategy_from_SWEREF99_or_RT90_to_WGS84()

    # Implementation first transforming to WGS84 and then to the real target:
    transFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget = _TransFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget()

    @staticmethod
    def transform(sourceCoordinate: CrsCoordinate, targetCrsProjection: CrsProjection) -> CrsCoordinate:
        if(sourceCoordinate.get_crs_projection() == targetCrsProjection):
            return sourceCoordinate

        _transFormStrategy: _TransformStrategy = None

        # Transform FROM wgs84:
        if(
            sourceCoordinate.get_crs_projection().is_wgs84()
            and
            ( targetCrsProjection.is_sweref99() or targetCrsProjection.is_rt90() )
        ):
            _transFormStrategy = _Transformer.transformStrategy_From_WGS84_to_SWEREF99_or_RT90

        # Transform TO wgs84:
        elif(
            targetCrsProjection.is_wgs84()
            and
            ( sourceCoordinate.get_crs_projection().is_sweref99() or sourceCoordinate.get_crs_projection().is_rt90() )
        ):
            _transFormStrategy = _Transformer.transformStrategy_From_SWEREF99_or_RT90_to_WGS84

        # Transform between two non-wgs84:
        elif(
            ( sourceCoordinate.get_crs_projection().is_sweref99() or sourceCoordinate.get_crs_projection().is_rt90() )
            and
            ( targetCrsProjection.is_sweref99() or targetCrsProjection.is_rt90() )
        ):
            # the only direct transform supported is to/from WGS84, so therefore first transform to wgs84
            _transFormStrategy = _Transformer.transFormStrategy_From_Sweref99OrRT90_to_WGS84_andThenToRealTarget

        return _Transformer._transform_with_explicit_strategy(_transFormStrategy, sourceCoordinate, targetCrsProjection)


    # this method is not intended for public usage
    @staticmethod
    def _transform_with_explicit_strategy(
        _transFormStrategy: _TransformStrategy,
        sourceCoordinate: CrsCoordinate,
        targetCrsProjection: CrsProjection
    ) -> CrsCoordinate:
        if(_transFormStrategy is None):
            _Transformer._throwExceptionMessage(sourceCoordinate.get_crs_projection(), targetCrsProjection)
        else:
            return _transFormStrategy.transform(sourceCoordinate, targetCrsProjection)


    @staticmethod
    def _throwExceptionMessage(
        sourceProjection: CrsCoordinate,
        targetCrsProjection: CrsCoordinate,
    ):
        raise ValueError(f"Unhandled source/target projection transformation: {sourceProjection} ==> {targetCrsProjection}")
