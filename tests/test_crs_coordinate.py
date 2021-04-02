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
            """
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

            # Transformations to WGS84 (from SWEREF99TM and RT90):
            self.assertEqual(
                stockholmWGS84,  # expected WGS84
                stockholmSWEREF99TM.transform(CrsProjection.WGS84)  # actual/transformed WGS84
            )

            self.assertEqual(
                stockholmWGS84,  # expected WGS84
                stockholmRT90.transform(CrsProjection.wgs84)  # actual/transformed WGS84
            )
            # below is a similar test as one of the above tests but using the overloaded Transform method
            # which takes an integer as parameter instead of an instance of the enum CrsProjection
            epsgNumberForWgs84: int = CrsProjection.WGS84.get_epsg_number()
            self.assertEqual(
                stockholmWGS84,
                stockholmRT90.transform_by_epsg_number(epsgNumberForWgs84)  # testing the overloaded Transform method with an integer parameter
            )


            # Transformations to SWEREF99TM (from WGS84 and RT90):
            self.assertEqual(
                stockholmSWEREF99TM,  # expected SWEREF99TM
                stockholmWGS84.transform(CrsProjection.SWEREF_99_TM)  # actual/transformed SWEREF99TM
            )

            self.assertEqual(
                stockholmSWEREF99TM,  # expected SWEREF99TM
                stockholmRT90.transform(CrsProjection.SWEREF_99_TM)  # actual/transformed SWEREF99TM
            )


            # Transformations to RT90 (from WGS84 and SWEREF99TM):
            self.assertEqual(
                stockholmRT90,  # expected RT90
                stockholmWGS84.transform(CrsProjection.RT90_2_5_GON_V)  # actual/transformed RT90
            )

            self.assertEqual(
                stockholmRT90,  # expected RT90
                stockholmSWEREF99TM.transform(CrsProjection.RT90_2_5_GON_V)  # actual/transformed RT90
            )
            """

        def assertEqualCoordinate(self, crsCoordinate_1: CrsCoordinate, crsCoordinate_2: CrsCoordinate) :
            messageToDisplayIfAssertionFails = f"crsCoordinate_1: {crsCoordinate_1}  , crsCoordinate_2 : {crsCoordinate_2}"
            self.assertEqual(crsCoordinate_1.get_crs_projection(), crsCoordinate_2.get_crs_projection(), messageToDisplayIfAssertionFails)
            maxDifference = 0.000007 if crsCoordinate_1.get_crs_projection().is_wgs84() else 0.5  # the other (i.e. non-WGS84) value is using meter as unit, so 0.5 is just five decimeters difference
            diffLongitude = abs((crsCoordinate_1.get_longitude_x() - crsCoordinate_2.get_longitude_x()))
            diffLatitude = abs((crsCoordinate_1.get_latitude_y() - crsCoordinate_2.get_latitude_y()))
            self.assertTrue(diffLongitude < maxDifference, messageToDisplayIfAssertionFails)
            self.assertTrue(diffLatitude < maxDifference, messageToDisplayIfAssertionFails)


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
            pass
            """
            CrsCoordinate coordinateInstance_1 = CrsCoordinate.CreateCoordinate(CrsProjection.wgs84, stockholmCentralStation_WGS84_longitude, stockholmCentralStation_WGS84_latitude)
            CrsCoordinate coordinateInstance_2 = CrsCoordinate.CreateCoordinate(CrsProjection.wgs84, stockholmCentralStation_WGS84_longitude, stockholmCentralStation_WGS84_latitude)
            Assert.AreEqual(coordinateInstance_1, coordinateInstance_2)
            Assert.AreEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_2.GetHashCode())
            Assert.IsTrue(coordinateInstance_1 == coordinateInstance_2)
            Assert.IsTrue(coordinateInstance_2 == coordinateInstance_1)
            Assert.IsTrue(coordinateInstance_1.Equals(coordinateInstance_2))
            Assert.IsTrue(coordinateInstance_2.Equals(coordinateInstance_1))


            double delta = 0.000000000000001 // see comments further below regarding the value of "delta"
            CrsCoordinate coordinateInstance_3 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                stockholmCentralStation_WGS84_longitude + delta,
                stockholmCentralStation_WGS84_latitude + delta
            )
            Assert.AreEqual(coordinateInstance_1, coordinateInstance_3)
            Assert.AreEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_3.GetHashCode())
            Assert.IsTrue(coordinateInstance_1 == coordinateInstance_3) // method "operator =="
            Assert.IsTrue(coordinateInstance_3 == coordinateInstance_1)
            Assert.IsTrue(coordinateInstance_1.Equals(coordinateInstance_3))
            Assert.IsTrue(coordinateInstance_3.Equals(coordinateInstance_1))

            // Regarding the chosen value for "delta" (which is added to the lon/lat values, to create a slightly different value) above and below,
            // it is because of experimentation this "breakpoint" value has been determined, i.e. the above value still resulted in equality
            // but when it was increased as below with one decimal then the above kind of assertions failed and therefore the other assertions below
            // are used instead e.g. testing the overloaded operator "!=".
            // You should generally be cautios when comparing floating point values but the above test indicate that values are considered equal even though
            // the difference is as 'big' as in the "delta" value above.

            delta = delta * 10 // moving the decimal one bit to get a somewhat larger values, and then the instances are not considered equal, as you can see in the tests below.
            CrsCoordinate coordinateInstance_4 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                CrsCoordinateTest.stockholmCentralStation_WGS84_longitude + delta,
                CrsCoordinateTest.stockholmCentralStation_WGS84_latitude + delta
            )
            // Note that below are the Are*NOT*Equal assertions made instead of AreEqual as further above when a smaller delta value was used
            Assert.AreNotEqual(coordinateInstance_1, coordinateInstance_4)
            Assert.AreNotEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_4.GetHashCode())
            Assert.IsTrue(coordinateInstance_1 != coordinateInstance_4) // Note that the method "operator !=" becomes used here
            Assert.IsTrue(coordinateInstance_4 != coordinateInstance_1)
            Assert.IsFalse(coordinateInstance_1.Equals(coordinateInstance_4))
            Assert.IsFalse(coordinateInstance_4.Equals(coordinateInstance_1))
            """

        def test_string(self):
            coordinate: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.SWEREF_99_18_00, 6579457.649, 153369.673)
            self.assertEqual(
                "CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00 ]",
                str(coordinate)
            )
            coordinate2: CrsCoordinate = CrsCoordinate.create_coordinate(CrsProjection.WGS84, 59.330231, 18.059196)
            expectedDefaultToStringResultForCoordinate2 = "CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84 ]"
            self.assertEqual(
                expectedDefaultToStringResultForCoordinate2 ,
                str(coordinate2)
            )

        # This is not really a "Test" method used for assertions, but can be used for code examples
        # e.g. verify that this code below works and then it can be paste into some example page at github
        # [Test]
        def example(self):
            stockholmWGS84: CrsCoordinate = CrsCoordinate.create_coordinate(
                CrsProjection.WGS84,
                CrsCoordinateTest.stockholmCentralStation_WGS84_latitude,
                CrsCoordinateTest.stockholmCentralStation_WGS84_longitude
            )

            stockholmSweref99tm: CrsCoordinate = stockholmWGS84.transform(CrsProjection.SWEREF_99_TM)
            print(f"stockholmSweref99tm X: {stockholmSweref99tm.get_longitude_x()}")
            print(f"stockholmSweref99tm Y: {stockholmSweref99tm.get_latitude_y()}")
            print(f"stockholmSweref99tm 'ToString': {stockholmSweref99tm}")
            # Output from the above:
            # TODO

            # IList<CrsProjection> allProjections = CrsProjectionFactory.GetAllCrsProjections()
            # foreach(var crsProjection in allProjections) {
                # print(stockholmWGS84.Transform(crsProjection))
            # Output from the above loop:
            # TODO
