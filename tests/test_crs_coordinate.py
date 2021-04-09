import unittest
from sweden_crs_transformations.crs_projection import CrsProjection
from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from tests.test_crs_projection import CrsProjectionTest


class CrsCoordinateTest(unittest.TestCase):

    # // https://kartor.eniro.se/m/XRCfh
    #    //WGS84 decimal (lat, lon)      59.330231, 18.059196
    #    //RT90 (nord, öst)              6580994, 1628294
    #    //SWEREF99 TM (nord, öst)       6580822, 674032
    stockholmCentralStation_WGS84_latitude = 59.330231
    stockholmCentralStation_WGS84_longitude = 18.059196
    stockholmCentralStation_RT90_northing = 6580994
    stockholmCentralStation_RT90_easting = 1628294
    stockholmCentralStation_SWEREF99TM_northing = 6580822
    stockholmCentralStation_SWEREF99TM_easting = 674032

    def test_transform(self):
        stockholmWGS84: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.WGS84,
            CrsCoordinateTest.stockholmCentralStation_WGS84_latitude,
            CrsCoordinateTest.stockholmCentralStation_WGS84_longitude
        )
        stockholmSWEREF99TM: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.SWEREF_99_TM,
            CrsCoordinateTest.stockholmCentralStation_SWEREF99TM_northing,
            CrsCoordinateTest.stockholmCentralStation_SWEREF99TM_easting
        )

        stockholmRT90: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.RT90_2_5_GON_V,
            CrsCoordinateTest.stockholmCentralStation_RT90_northing,
            CrsCoordinateTest.stockholmCentralStation_RT90_easting
        )
        self.assertIsNotNone(stockholmWGS84)
        self.assertIsNotNone(stockholmSWEREF99TM)
        self.assertIsNotNone(stockholmRT90)

        # Transformations to WGS84 (from SWEREF99TM and RT90):
        self.assertEqualCoordinate(
            stockholmWGS84,  # expected WGS84
            stockholmSWEREF99TM.transform(CrsProjection.WGS84)  # actual/transformed WGS84
        )

        self.assertEqualCoordinate(
            stockholmWGS84,  # expected WGS84
            stockholmRT90.transform(CrsProjection.WGS84)  # actual/transformed WGS84
        )

        # below is a similar test as one of the above tests but using the overloaded Transform method
        # which takes an integer as parameter instead of an instance of the enum CrsProjection
        epsgNumberForWgs84: int = CrsProjection.WGS84.get_epsg_number()
        self.assertEqualCoordinate(
            stockholmWGS84,
            stockholmRT90.transform_by_epsg_number(epsgNumberForWgs84)  # testing the overloaded Transform method with an integer parameter
        )

        # Transformations to SWEREF99TM (from WGS84 and RT90):
        self.assertEqualCoordinate(
            stockholmSWEREF99TM,  # expected SWEREF99TM
            stockholmWGS84.transform(CrsProjection.SWEREF_99_TM)  # actual/transformed SWEREF99TM
        )

        self.assertEqualCoordinate(
            stockholmSWEREF99TM,  # expected SWEREF99TM
            stockholmRT90.transform(CrsProjection.SWEREF_99_TM)  # actual/transformed SWEREF99TM
        )


        # Transformations to RT90 (from WGS84 and SWEREF99TM):
        self.assertEqualCoordinate(
            stockholmRT90,  # expected RT90
            stockholmWGS84.transform(CrsProjection.RT90_2_5_GON_V)  # actual/transformed RT90
        )

        self.assertEqualCoordinate(
            stockholmRT90,  # expected RT90
            stockholmSWEREF99TM.transform(CrsProjection.RT90_2_5_GON_V)  # actual/transformed RT90
        )

    def assertEqualCoordinate(self, crsCoordinate_1: CrsCoordinate, crsCoordinate_2: CrsCoordinate) :
        messageToDisplayIfAssertionFails = f"crsCoordinate_1: {crsCoordinate_1}  , crsCoordinate_2 : {crsCoordinate_2}"
        self.assertEqual(crsCoordinate_1.get_crs_projection(), crsCoordinate_2.get_crs_projection(), messageToDisplayIfAssertionFails)
        maxDifference = 0.000007 if crsCoordinate_1.get_crs_projection().is_wgs84() else 0.5  # the other (i.e. non-WGS84) value is using meter as unit, so 0.5 is just five decimeters difference
        self.assertAlmostEqual(crsCoordinate_1.get_longitude_x(), crsCoordinate_2.get_longitude_x(), msg=messageToDisplayIfAssertionFails, delta=maxDifference)
        self.assertAlmostEqual(crsCoordinate_1.get_latitude_y(), crsCoordinate_2.get_latitude_y(), msg=messageToDisplayIfAssertionFails, delta=maxDifference)


    def test_create_coordinate_by_epsg_number(self):
        x = 20.0
        y = 60.0
        crsCoordinate: CrsCoordinate = CrsCoordinate.create_coordinate_by_epsg_number(CrsProjectionTest.epsgNumberForSweref99tm, y, x)
        self.assertEqual(CrsProjectionTest.epsgNumberForSweref99tm, crsCoordinate.get_crs_projection().get_epsg_number())
        self.assertEqual(x, crsCoordinate.get_longitude_x())
        self.assertEqual(y, crsCoordinate.get_latitude_y())


    def test_create_coordinate(self):
        x = 22.5
        y = 62.5
        crsCoordinate: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.SWEREF_99_TM, y, x)
        self.assertEqual(CrsProjectionTest.epsgNumberForSweref99tm, crsCoordinate.get_crs_projection().get_epsg_number())
        self.assertEqual(CrsProjection.SWEREF_99_TM, crsCoordinate.get_crs_projection())
        self.assertEqual(x, crsCoordinate.get_longitude_x())
        self.assertEqual(y, crsCoordinate.get_latitude_y())


    def test_equality(self):
        coordinateInstance_1: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.WGS84, CrsCoordinateTest.stockholmCentralStation_WGS84_longitude, CrsCoordinateTest.stockholmCentralStation_WGS84_latitude)
        coordinateInstance_2: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.WGS84, CrsCoordinateTest.stockholmCentralStation_WGS84_longitude, CrsCoordinateTest.stockholmCentralStation_WGS84_latitude)
        self.assertEqual(coordinateInstance_1, coordinateInstance_2)
        self.assertEqual(hash(coordinateInstance_1), hash(coordinateInstance_2))
        self.assertTrue(coordinateInstance_1 == coordinateInstance_2)
        self.assertTrue(coordinateInstance_2 == coordinateInstance_1)

        delta = 0.000000000000001  # see comments further below regarding the value of "delta"
        coordinateInstance_3: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.WGS84,
            CrsCoordinateTest.stockholmCentralStation_WGS84_longitude + delta,
            CrsCoordinateTest.stockholmCentralStation_WGS84_latitude + delta
        )
        self.assertEqual(coordinateInstance_1, coordinateInstance_3)
        self.assertEqual(hash(coordinateInstance_1), hash(coordinateInstance_3))
        self.assertTrue(coordinateInstance_1 == coordinateInstance_3) # method "operator =="
        self.assertTrue(coordinateInstance_3 == coordinateInstance_1)

        '''
        // Regarding the chosen value for "delta" (which is added to the lon/lat values, to create a slightly different value) above and below,
        // it is because of experimentation this "breakpoint" value has been determined, i.e. the above value still resulted in equality
        // but when it was increased as below with one decimal then the above kind of assertions failed and therefore the other assertions below
        // are used instead e.g. testing the overloaded operator "!=".
        // You should generally be cautios when comparing floating point values but the above test indicate that values are considered equal even though
        // the difference is as 'big' as in the "delta" value above.
        '''

        delta = delta * 10  # moving the decimal one bit to get a somewhat larger values, and then the instances are not considered equal, as you can see in the tests below.
        coordinateInstance_4: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.WGS84,
            CrsCoordinateTest.stockholmCentralStation_WGS84_longitude + delta,
            CrsCoordinateTest.stockholmCentralStation_WGS84_latitude + delta
        )
        # Note that below are the Are*NOT*Equal assertions made instead of AreEqual as further above when a smaller delta value was used
        self.assertNotEqual(coordinateInstance_1, coordinateInstance_4)
        self.assertNotEqual(hash(coordinateInstance_1), hash(coordinateInstance_4))
        self.assertTrue(coordinateInstance_1 != coordinateInstance_4)
        self.assertTrue(coordinateInstance_4 != coordinateInstance_1)
        self.assertIsNot(coordinateInstance_4, coordinateInstance_1)

    def test_string(self):
        coordinate: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.SWEREF_99_18_00, 6579457.649, 153369.673)
        self.assertEqual(
            "CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00(EPSG:3011) ]",
            str(coordinate)
        )
        coordinate2: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.WGS84, 59.330231, 18.059196)
        expectedDefaultToStringResultForCoordinate2 = "CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84(EPSG:4326) ]"
        self.assertEqual(
            expectedDefaultToStringResultForCoordinate2 ,
            str(coordinate2)
        )

    # This is not really a "Test" method used for assertions, but can be used for code examples
    # e.g. verify that this code below works and then it can be paste into some example page at github
    # def test_example(self):
    def example(self):  # rename this method with test_ prefix as in the above row, if/when you want to execute it
        stockholmWGS84: CrsCoordinate = CrsCoordinate.create_coordinate(
            CrsProjection.WGS84,
            CrsCoordinateTest.stockholmCentralStation_WGS84_latitude,
            CrsCoordinateTest.stockholmCentralStation_WGS84_longitude
        )

        stockholmSweref99tm: CrsCoordinate = stockholmWGS84.transform(CrsProjection.SWEREF_99_TM)
        print(f"stockholmSweref99tm X: {stockholmSweref99tm.get_longitude_x()}")
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
