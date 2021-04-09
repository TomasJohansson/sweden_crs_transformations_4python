from abc import ABC, abstractmethod
from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection
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

class _TransformStrategy(ABC):
    @abstractmethod
    def transform(self,
        sourceCoordinate : CrsCoordinate,
        targetCrsProjection : CrsProjection
    ) -> CrsCoordinate:
        pass
