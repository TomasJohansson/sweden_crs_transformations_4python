import sys
from sweden_crs_transformations.crs_projection import CrsProjection

class _GaussKreugerParameterObject:

        def __init__(self, crsProjection: CrsProjection):
            self._axis = 0                  # Semi-major axis of the ellipsoid.
            self._flattening = 0            # Flattening of the ellipsoid.
            self._central_meridian = 0      # Central meridian for the projection.
            self._scale = 0                 # Scale on central meridian.
            self._false_northing = 0        # Offset for origo.
            self._false_easting = 0         # Offset for origo.
            self._swedish_params(crsProjection)

        """
        // Parameters for RT90 and SWEREF99TM.
        // Note: Parameters for RT90 are choosen to eliminate the
        // differences between Bessel and GRS80-ellipsoides.
        // Bessel-variants should only be used if lat/long are given as
        // RT90-lat/long based on the Bessel ellipsoide (from old maps).
        // Parameter: projection (string). Must match if-statement.
        """
        def _swedish_params(self, projection: CrsProjection):
            # // RT90 parameters, GRS 80 ellipsoid.
            if (projection == CrsProjection.RT90_7_5_GON_V):
                self._grs80_params()
                self._central_meridian = 11.0 + 18.375 / 60.0
                self._scale = 1.000006000000
                self._false_northing = -667.282
                self._false_easting = 1500025.141
            elif (projection == CrsProjection.RT90_5_0_GON_V):
                self._grs80_params()
                self._central_meridian = 13.0 + 33.376 / 60.0
                self._scale = 1.000005800000
                self._false_northing = -667.130
                self._false_easting = 1500044.695
            elif (projection == CrsProjection.RT90_2_5_GON_V):
                self._grs80_params()
                self._central_meridian = 15.0 + 48.0 / 60.0 + 22.624306 / 3600.0
                self._scale = 1.00000561024
                self._false_northing = -667.711
                self._false_easting = 1500064.274
            elif (projection == CrsProjection.RT90_0_0_GON_V):
                self._grs80_params()
                self._central_meridian = 18.0 + 3.378 / 60.0
                self._scale = 1.000005400000
                self._false_northing = -668.844
                self._false_easting = 1500083.521
            elif (projection == CrsProjection.RT90_2_5_GON_O):
                self._grs80_params()
                self._central_meridian = 20.0 + 18.379 / 60.0
                self._scale = 1.000005200000;
                self._false_northing = -670.706;
                self._false_easting = 1500102.765;
            elif (projection == CrsProjection.RT90_5_0_GON_O):
                self._grs80_params()
                self._central_meridian = 22.0 + 33.380 / 60.0
                self._scale = 1.000004900000
                self._false_northing = -672.557
                self._false_easting = 1500121.846
            # // SWEREF99TM and SWEREF99ddmm  parameters.
            elif (projection == CrsProjection.SWEREF_99_TM):
                self._sweref99_params()
                self._central_meridian = 15.00
                self._scale = 0.9996
                self._false_northing = 0.0
                self._false_easting = 500000.0
            elif (projection == CrsProjection.SWEREF_99_12_00):
                self._sweref99_params()
                self._central_meridian = 12.00
            elif (projection == CrsProjection.SWEREF_99_13_30):
                self._sweref99_params()
                self._central_meridian = 13.50
            elif (projection == CrsProjection.SWEREF_99_15_00):
                self._sweref99_params();
                self._central_meridian = 15.00;
            elif (projection == CrsProjection.SWEREF_99_16_30):
                self._sweref99_params();
                self._central_meridian = 16.50;
            elif (projection == CrsProjection.SWEREF_99_18_00):
                self._sweref99_params()
                self._central_meridian = 18.00
            elif (projection == CrsProjection.SWEREF_99_14_15):
                self._sweref99_params()
                self._central_meridian = 14.25
            elif (projection == CrsProjection.SWEREF_99_15_45):
                self._sweref99_params()
                self._central_meridian = 15.75
            elif (projection == CrsProjection.SWEREF_99_17_15):
                self._sweref99_params()
                self.central_meridian = 17.25
            elif (projection == CrsProjection.SWEREF_99_18_45):
                self._sweref99_params()
                self._central_meridian = 18.75
            elif (projection == CrsProjection.SWEREF_99_20_15):
                self._sweref99_params()
                self._central_meridian = 20.25
            elif (projection == CrsProjection.SWEREF_99_21_45):
                self._sweref99_params()
                self._central_meridian = 21.75
            elif (projection == CrsProjection.SWEREF_99_23_15):
                self._sweref99_params()
                self._central_meridian = 23.25
            else:
                self._central_meridian = sys.float_info.min # double.MinValue

        # // Sets of default parameters.
        def _grs80_params(self):
            self._axis = 6378137.0# ; // GRS 80.
            self._flattening = 1.0 / 298.257222101 #  // GRS 80.
            self._central_meridian = sys.float_info.min # double.MinValue
        def _bessel_params(self):
            self._axis = 6377397.155 # // Bessel 1841.
            self._flattening = 1.0 / 299.1528128 # // Bessel 1841.
            self._central_meridian = sys.float_info.min # double.MinValue
            self._scale = 1.0
            self._false_northing = 0.0
            self._false_easting = 1500000.0

        def _sweref99_params(self):
            self._axis = 6378137.0 # ; // GRS 80.
            self._flattening = 1.0 / 298.257222101 #  // GRS 80.
            self._central_meridian =  sys.float_info.min # double.MinValue
            self._scale = 1.0
            self._false_northing = 0.0
            self._false_easting = 150000.0
