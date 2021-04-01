using NUnit.Framework;
using SwedenCrsTransformations;
using System;
using System.Collections.Generic;
using static SwedenCrsTransformationsTests.CrsProjectionFactoryTest; // to be able to use constants such as epsgNumberForSweref99tm

namespace SwedenCrsTransformationsTests {
    
    [TestFixture]
    public class CrsCoordinateTest {

        // https://kartor.eniro.se/m/XRCfh
            //WGS84 decimal (lat, lon)      59.330231, 18.059196
            //RT90 (nord, öst)              6580994, 1628294
            //SWEREF99 TM (nord, öst)       6580822, 674032
        private const double stockholmCentralStation_WGS84_latitude = 59.330231;
        private const double stockholmCentralStation_WGS84_longitude = 18.059196;
        private const double stockholmCentralStation_RT90_northing = 6580994;
        private const double stockholmCentralStation_RT90_easting = 1628294;
        private const double stockholmCentralStation_SWEREF99TM_northing = 6580822;
        private const double stockholmCentralStation_SWEREF99TM_easting = 674032;

        [Test]
        public void Transform() {
            CrsCoordinate stockholmWGS84 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                stockholmCentralStation_WGS84_latitude,
                stockholmCentralStation_WGS84_longitude
            );
            CrsCoordinate stockholmSWEREF99TM = CrsCoordinate.CreateCoordinate(
                CrsProjection.sweref_99_tm,
                stockholmCentralStation_SWEREF99TM_northing,
                stockholmCentralStation_SWEREF99TM_easting
            );
            CrsCoordinate stockholmRT90 = CrsCoordinate.CreateCoordinate(
                CrsProjection.rt90_2_5_gon_v,
                stockholmCentralStation_RT90_northing,
                stockholmCentralStation_RT90_easting
            );
            
            // Transformations to WGS84 (from SWEREF99TM and RT90):
            AssertEqual(
                stockholmWGS84, // expected WGS84
                stockholmSWEREF99TM.Transform(CrsProjection.wgs84) // actual/transformed WGS84
            );
            AssertEqual(
                stockholmWGS84, // expected WGS84
                stockholmRT90.Transform(CrsProjection.wgs84) // actual/transformed WGS84
            );
            // below is a similar test as one of the above tests but using the overloaded Transform method
            // which takes an integer as parameter instead of an instance of the enum CrsProjection
            int epsgNumberForWgs84 = CrsProjection.wgs84.GetEpsgNumber();
            AssertEqual(
                stockholmWGS84,
                stockholmRT90.Transform(epsgNumberForWgs84) // testing the overloaded Transform method with an integer parameter
            );
            

            // Transformations to SWEREF99TM (from WGS84 and RT90):
            AssertEqual(
                stockholmSWEREF99TM, // expected SWEREF99TM
                stockholmWGS84.Transform(CrsProjection.sweref_99_tm) // actual/transformed SWEREF99TM
            );
            AssertEqual(
                stockholmSWEREF99TM, // expected SWEREF99TM
                stockholmRT90.Transform(CrsProjection.sweref_99_tm) // actual/transformed SWEREF99TM
            );


            // Transformations to RT90 (from WGS84 and SWEREF99TM):
            AssertEqual(
                stockholmRT90,  // expected RT90
                stockholmWGS84.Transform(CrsProjection.rt90_2_5_gon_v) // actual/transformed RT90
            );
            AssertEqual(
                stockholmRT90,  // expected RT90
                stockholmSWEREF99TM.Transform(CrsProjection.rt90_2_5_gon_v) // actual/transformed RT90
            );
        }

        private void AssertEqual(CrsCoordinate crsCoordinate_1, CrsCoordinate crsCoordinate_2)  {
            string messageToDisplayIfAssertionFails = "crsCoordinate_1: " + crsCoordinate_1 + " , crsCoordinate_2 : " + crsCoordinate_2;
            Assert.AreEqual(crsCoordinate_1.CrsProjection, crsCoordinate_2.CrsProjection, messageToDisplayIfAssertionFails);
            double maxDifference = crsCoordinate_1.CrsProjection.IsWgs84() ? 0.000007 : 0.5; // the other (i.e. non-WGS84) value is using meter as unit, so 0.5 is just five decimeters difference
            double diffLongitude = Math.Abs((crsCoordinate_1.LongitudeX - crsCoordinate_2.LongitudeX));
            double diffLatitude = Math.Abs((crsCoordinate_1.LatitudeY - crsCoordinate_2.LatitudeY));            
            Assert.IsTrue(diffLongitude < maxDifference, messageToDisplayIfAssertionFails);
            Assert.IsTrue(diffLatitude < maxDifference, messageToDisplayIfAssertionFails);
        }

        
        [Test]
        public void CreateCoordinateByEpsgNumber() {
            const double x = 20.0;
            const double y = 60.0;
            CrsCoordinate crsCoordinate = CrsCoordinate.CreateCoordinate(epsgNumberForSweref99tm, y, x);
            Assert.AreEqual(epsgNumberForSweref99tm, crsCoordinate.CrsProjection.GetEpsgNumber());
            Assert.AreEqual(x, crsCoordinate.LongitudeX);
            Assert.AreEqual(y, crsCoordinate.LatitudeY);
        }

        [Test]
        public void CreateCoordinate() {
            const double x = 22.5;
            const double y = 62.5;
            CrsCoordinate crsCoordinate = CrsCoordinate.CreateCoordinate(CrsProjection.sweref_99_tm, y, x);
            Assert.AreEqual(epsgNumberForSweref99tm, crsCoordinate.CrsProjection.GetEpsgNumber());
            Assert.AreEqual(CrsProjection.sweref_99_tm, crsCoordinate.CrsProjection);
            Assert.AreEqual(x, crsCoordinate.LongitudeX);
            Assert.AreEqual(y, crsCoordinate.LatitudeY);
        }


        [Test]
        public void EqualityTest() {
            CrsCoordinate coordinateInstance_1 = CrsCoordinate.CreateCoordinate(CrsProjection.wgs84, stockholmCentralStation_WGS84_longitude, stockholmCentralStation_WGS84_latitude);
            CrsCoordinate coordinateInstance_2 = CrsCoordinate.CreateCoordinate(CrsProjection.wgs84, stockholmCentralStation_WGS84_longitude, stockholmCentralStation_WGS84_latitude);
            Assert.AreEqual(coordinateInstance_1, coordinateInstance_2);
            Assert.AreEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_2.GetHashCode());
            Assert.IsTrue(coordinateInstance_1 == coordinateInstance_2);
            Assert.IsTrue(coordinateInstance_2 == coordinateInstance_1);
            Assert.IsTrue(coordinateInstance_1.Equals(coordinateInstance_2));
            Assert.IsTrue(coordinateInstance_2.Equals(coordinateInstance_1));


            double delta = 0.000000000000001; // see comments further below regarding the value of "delta"
            CrsCoordinate coordinateInstance_3 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                stockholmCentralStation_WGS84_longitude + delta,
                stockholmCentralStation_WGS84_latitude + delta
            );
            Assert.AreEqual(coordinateInstance_1, coordinateInstance_3);
            Assert.AreEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_3.GetHashCode());
            Assert.IsTrue(coordinateInstance_1 == coordinateInstance_3); // method "operator =="
            Assert.IsTrue(coordinateInstance_3 == coordinateInstance_1);
            Assert.IsTrue(coordinateInstance_1.Equals(coordinateInstance_3));
            Assert.IsTrue(coordinateInstance_3.Equals(coordinateInstance_1));

            // Regarding the chosen value for "delta" (which is added to the lon/lat values, to create a slightly different value) above and below,
            // it is because of experimentation this "breakpoint" value has been determined, i.e. the above value still resulted in equality 
            // but when it was increased as below with one decimal then the above kind of assertions failed and therefore the other assertions below 
            // are used instead e.g. testing the overloaded operator "!=".
            // You should generally be cautios when comparing floating point values but the above test indicate that values are considered equal even though 
            // the difference is as 'big' as in the "delta" value above.

            delta = delta * 10; // moving the decimal one bit to get a somewhat larger values, and then the instances are not considered equal, as you can see in the tests below.
            CrsCoordinate coordinateInstance_4 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                stockholmCentralStation_WGS84_longitude + delta,
                stockholmCentralStation_WGS84_latitude + delta
            );
            // Note that below are the Are*NOT*Equal assertions made instead of AreEqual as further above when a smaller delta value was used
            Assert.AreNotEqual(coordinateInstance_1, coordinateInstance_4);
            Assert.AreNotEqual(coordinateInstance_1.GetHashCode(), coordinateInstance_4.GetHashCode());
            Assert.IsTrue(coordinateInstance_1 != coordinateInstance_4); // Note that the method "operator !=" becomes used here
            Assert.IsTrue(coordinateInstance_4 != coordinateInstance_1);
            Assert.IsFalse(coordinateInstance_1.Equals(coordinateInstance_4));
            Assert.IsFalse(coordinateInstance_4.Equals(coordinateInstance_1));
        }


        [Test]
        public void ToStringTest() {
            CrsCoordinate coordinate = CrsCoordinate.CreateCoordinate(CrsProjection.sweref_99_18_00, 6579457.649, 153369.673);
            Assert.AreEqual(
                "CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00 ]",
                coordinate.ToString()
            );
            CrsCoordinate coordinate2 = CrsCoordinate.CreateCoordinate(CrsProjection.wgs84, 59.330231, 18.059196);
            const string expectedDefaultToStringResultForCoordinate2 = "CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84 ]";
            Assert.AreEqual(
                expectedDefaultToStringResultForCoordinate2 ,
                coordinate2.ToString()
            );
            // now testing the same coordinate as above but with a custom 'ToString' implementation
            CrsCoordinate.SetToStringImplementation(myCustomToStringMethod);
            Assert.AreEqual(
                "18.059196 , 59.330231",
                coordinate2.ToString()
            );
            CrsCoordinate.SetToStringImplementationDefault(); // restores the default 'ToString' implementation
            Assert.AreEqual(
                expectedDefaultToStringResultForCoordinate2 ,
                coordinate2.ToString()
            );
        }

        private string myCustomToStringMethod(CrsCoordinate coordinate) {
            return string.Format(
                "{0} , {1}",
                    coordinate.LongitudeX,
                    coordinate.LatitudeY
            );
        }


        // This is not really a "Test" method used for assertions, but can be used for code examples 
        // e.g. verify that this code below works and then it can be paste into some example page at github
        // [Test]
        public void Example() {
            CrsCoordinate stockholmWGS84 = CrsCoordinate.CreateCoordinate(
                CrsProjection.wgs84,
                stockholmCentralStation_WGS84_latitude,
                stockholmCentralStation_WGS84_longitude
            );

            CrsCoordinate stockholmSweref99tm = stockholmWGS84.Transform(CrsProjection.sweref_99_tm);
            Console.WriteLine("stockholmSweref99tm X: " + stockholmSweref99tm.LongitudeX);
            Console.WriteLine("stockholmSweref99tm Y: " + stockholmSweref99tm.LatitudeY);
            Console.WriteLine("stockholmSweref99tm 'ToString': " + stockholmSweref99tm.ToString());
            // Output from the above:
            //stockholmSweref99tm X: 674032.357
            //stockholmSweref99tm Y: 6580821.991
            //stockholmSweref99tm 'ToString': CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM ]

            IList<CrsProjection> allProjections = CrsProjectionFactory.GetAllCrsProjections();
            foreach(var crsProjection in allProjections) {
                Console.WriteLine(stockholmWGS84.Transform(crsProjection));
            }
            // Output from the above loop:
            //CrsCoordinate [ Y: 6580821.991 , X: 674032.357 , CRS: SWEREF_99_TM ]
            //CrsCoordinate [ Y: 6595151.116 , X: 494604.69 , CRS: SWEREF_99_12_00 ]
            //CrsCoordinate [ Y: 6588340.147 , X: 409396.217 , CRS: SWEREF_99_13_30 ]
            //CrsCoordinate [ Y: 6583455.373 , X: 324101.998 , CRS: SWEREF_99_15_00 ]
            //CrsCoordinate [ Y: 6580494.921 , X: 238750.424 , CRS: SWEREF_99_16_30 ]
            //CrsCoordinate [ Y: 6579457.649 , X: 153369.673 , CRS: SWEREF_99_18_00 ]
            //CrsCoordinate [ Y: 6585657.12 , X: 366758.045 , CRS: SWEREF_99_14_15 ]
            //CrsCoordinate [ Y: 6581734.696 , X: 281431.616 , CRS: SWEREF_99_15_45 ]
            //CrsCoordinate [ Y: 6579735.93 , X: 196061.94 , CRS: SWEREF_99_17_15 ]
            //CrsCoordinate [ Y: 6579660.051 , X: 110677.129 , CRS: SWEREF_99_18_45 ]
            //CrsCoordinate [ Y: 6581507.028 , X: 25305.238 , CRS: SWEREF_99_20_15 ]
            //CrsCoordinate [ Y: 6585277.577 , X: -60025.629 , CRS: SWEREF_99_21_45 ]
            //CrsCoordinate [ Y: 6590973.148 , X: -145287.219 , CRS: SWEREF_99_23_15 ]
            //CrsCoordinate [ Y: 6598325.639 , X: 1884004.1 , CRS: RT90_7_5_GON_V ]
            //CrsCoordinate [ Y: 6587493.237 , X: 1756244.287 , CRS: RT90_5_0_GON_V ]
            //CrsCoordinate [ Y: 6580994.18 , X: 1628293.886 , CRS: RT90_2_5_GON_V ]
            //CrsCoordinate [ Y: 6578822.84 , X: 1500248.374 , CRS: RT90_0_0_GON_V ]
            //CrsCoordinate [ Y: 6580977.349 , X: 1372202.721 , CRS: RT90_2_5_GON_O ]
            //CrsCoordinate [ Y: 6587459.595 , X: 1244251.702 , CRS: RT90_5_0_GON_O ]
            //CrsCoordinate [ Latitude: 59.330231 , Longitude: 18.059196 , CRS: WGS84 ]
        }
    }
}
