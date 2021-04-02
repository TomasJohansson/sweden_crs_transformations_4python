using NUnit.Framework;

namespace MightyLittleGeodesy {
    [TestFixture]
    public class LatLonTest {
        private const double delta = 0.00000000000000000001;
    
        [Test]
        public void latLon() {
            LatLon latLon = new LatLon(12.34, 56.78);
            Assert.AreEqual(latLon.LatitudeY, 12.34, delta);
            Assert.AreEqual(latLon.LongitudeX, 56.78, delta);        
        }
    }
}
