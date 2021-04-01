using NUnit.Framework;
using SwedenCrsTransformations;
using System.Collections.Generic;
using static SwedenCrsTransformationsTests.CrsProjectionFactoryTest; // to be able to use constants such as epsgNumberForSweref99tm and epsgNumberForWgs84
using static SwedenCrsTransformations.CrsProjection;
namespace SwedenCrsTransformationsTests {
    
    [TestFixture]
    public class CrsProjectionExtensionsTest {

        private HashSet<CrsProjection> _wgs84Projections;
        private HashSet<CrsProjection> _sweref99Projections;
        private HashSet<CrsProjection> _rt90Projections;

        [SetUp]
        public void SetUp() {
            _wgs84Projections = new HashSet<CrsProjection>{ wgs84 };
            _sweref99Projections = new HashSet<CrsProjection>{ 
                sweref_99_12_00, sweref_99_13_30, sweref_99_14_15,
                sweref_99_15_00, sweref_99_15_45, sweref_99_16_30,
                sweref_99_17_15, sweref_99_18_00, sweref_99_18_45,
                sweref_99_20_15, sweref_99_21_45, sweref_99_23_15, sweref_99_tm
            };
            _rt90Projections = new HashSet<CrsProjection>{ 
                rt90_0_0_gon_v, rt90_2_5_gon_o, rt90_2_5_gon_v,
                rt90_5_0_gon_o, rt90_5_0_gon_v, rt90_7_5_gon_v
            };
        }

        [Test]
        public void GetEpsgNumber() {
            Assert.AreEqual(
                epsgNumberForSweref99tm, // constant defined in CrsProjectionFactoryTest
                CrsProjection.sweref_99_tm.GetEpsgNumber()
            );

            Assert.AreEqual(
                epsgNumberForWgs84, // constant defined in CrsProjectionFactoryTest
                CrsProjection.wgs84.GetEpsgNumber()
            );
        }


        [Test]
        public void isWgs84() {
            Assert.AreEqual(numberOfWgs84Projections, _wgs84Projections.Count);

            foreach(var item in _wgs84Projections) {
                Assert.IsTrue(item.IsWgs84());
            }
            foreach(var item in _sweref99Projections) {
                Assert.IsFalse(item.IsWgs84());
            }
            foreach(var item in _rt90Projections) {
                Assert.IsFalse(item.IsWgs84());
            }
        }

        [Test]
        public void isSweref() {
            Assert.AreEqual(numberOfSweref99projections, _sweref99Projections.Count);

            foreach(var item in _wgs84Projections) {
                Assert.IsFalse(item.IsSweref());
            }
            foreach(var item in _sweref99Projections) {
                Assert.IsTrue(item.IsSweref());
            }
            foreach(var item in _rt90Projections) {
                Assert.IsFalse(item.IsSweref());
            }
        }

        [Test]
        public void isRT90() {
            Assert.AreEqual(numberOfRT90projections, _rt90Projections.Count);

            foreach(var item in _wgs84Projections) {
                Assert.IsFalse(item.IsRT90());
            }
            foreach(var item in _sweref99Projections) {
                Assert.IsFalse(item.IsRT90());
            }
            foreach(var item in _rt90Projections) {
                Assert.IsTrue(item.IsRT90());
            }
        }

        [Test]
        public void CreateCoordinate() {
            const double x = 22.5;
            const double y = 62.5;
            CrsCoordinate crsCoordinate = CrsProjection.sweref_99_tm.CreateCoordinate(y, x);
            Assert.AreEqual(epsgNumberForSweref99tm, crsCoordinate.CrsProjection.GetEpsgNumber());
            Assert.AreEqual(CrsProjection.sweref_99_tm, crsCoordinate.CrsProjection);
            const double delta = 0.000001;
            Assert.AreEqual(x, crsCoordinate.LongitudeX, delta);
            Assert.AreEqual(y, crsCoordinate.LatitudeY, delta);
        }
    }
}