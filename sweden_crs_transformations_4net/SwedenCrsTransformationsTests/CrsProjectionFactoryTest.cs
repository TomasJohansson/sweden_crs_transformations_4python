using NUnit.Framework;
using SwedenCrsTransformations;
using System.Collections.Generic;
using System.Linq;

namespace SwedenCrsTransformationsTests
{
    [TestFixture]
    public class CrsProjectionFactoryTest {

        internal const int epsgNumberForWgs84 = 4326;
        internal const int epsgNumberForSweref99tm = 3006; // https://epsg.org/crs_3006/SWEREF99-TM.html
        internal const int numberOfSweref99projections = 13; // with EPSG numbers 3006-3018
        internal const int numberOfRT90projections = 6; // with EPSG numbers 3019-3024
        internal const int numberOfWgs84Projections = 1; // just to provide semantic instead of using a magic number 1 below
        private const int totalNumberOfProjections = numberOfSweref99projections + numberOfRT90projections + numberOfWgs84Projections;

        private IList<CrsProjection> _allCrsProjections;

        [SetUp]
        public void SetUp() {
            _allCrsProjections = CrsProjectionFactory.GetAllCrsProjections();;
        }


        [Test]
        public void GetCrsProjectionByEpsgNumber() {
            Assert.AreEqual(
                CrsProjection.sweref_99_tm,
                CrsProjectionFactory.GetCrsProjectionByEpsgNumber(epsgNumberForSweref99tm)
            );

            Assert.AreEqual(
                CrsProjection.sweref_99_23_15,
                CrsProjectionFactory.GetCrsProjectionByEpsgNumber(3018) // https://epsg.io/3018
            );

            Assert.AreEqual(
                CrsProjection.rt90_5_0_gon_o,
                CrsProjectionFactory.GetCrsProjectionByEpsgNumber(3024)  // https://epsg.io/3018
            );
        }

        [Test]
        public void VerifyTotalNumberOfProjections() {
            Assert.AreEqual(
                totalNumberOfProjections,
                _allCrsProjections.Count // retrieved with 'GetAllCrsProjections' in the SetUp method
            );
        }    
        [Test]
        public void VerifyNumberOfWgs84Projections() {
            Assert.AreEqual(numberOfWgs84Projections, _allCrsProjections.Where(crs => crs.IsWgs84()).Count());
        }
        [Test]
        public void VerifyNumberOfSweref99Projections() {
            Assert.AreEqual(numberOfSweref99projections, _allCrsProjections.Where(crs => crs.IsSweref()).Count());
        }
        [Test]
        public void VerifyNumberOfRT90Projections() {
            Assert.AreEqual(numberOfRT90projections, _allCrsProjections.Where(crs => crs.IsRT90()).Count());
        }

        [Test]

        public void VerifyThatAllProjectionsCanBeRetrievedByItsEpsgNumber() {
            foreach(var crsProjection in _allCrsProjections) {
                var crsProj = CrsProjectionFactory.GetCrsProjectionByEpsgNumber(crsProjection.GetEpsgNumber());
                Assert.AreEqual(crsProjection, crsProj);
            }
        }    

    }
}