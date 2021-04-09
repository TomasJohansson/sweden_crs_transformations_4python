from __future__ import annotations  # this import makes the code in the file less sensitive regarding in which order the classes are defined
import unittest
import os

from sweden_crs_transformations.crs_coordinate import CrsCoordinate
from sweden_crs_transformations.crs_projection import CrsProjection

# py -3.9 -m unittest tests/coordinate_files/test_transforming_coordinates_from_file.py
# py -3.9 -m unittest discover -s tests

class TransformingCoordinatesFromFileTest(unittest.TestCase):

    columnSeparator = "|"

    # // the below file "swedish_crs_transformations.csv" was copied from: https://github.com/TomasJohansson/crsTransformations/blob/a1da6c74daf040a521beb32f9f395124ffe76aa6/crs-transformation-adapter-test/src/test/resources/generated/swedish_crs_coordinates.csv
    # // and it was generated with a method "createFileWithTransformationResultsForCoordinatesInSweden()" at https://github.com/TomasJohansson/crsTransformations/blob/a1da6c74daf040a521beb32f9f395124ffe76aa6/crs-transformation-adapter-test/src/test/java/com/programmerare/com/programmerare/testData/CoordinateTestDataGeneratedFromEpsgDatabaseTest.java
    # private const string relativePathForFileWith_swedish_crs_transformations = "CoordinateFiles/data/swedish_crs_coordinates.csv";
    # // the project file should use "CopyToOutputDirectory" for the above file

    def readAllLinesFromResourceFile(self) -> list[str]:
        thedirectory = os.path.dirname(os.path.realpath(__file__))
        # print(thedirectory)
        csvFilename = 'swedish_crs_coordinates.csv'
        pathForResourceFile = os.path.join(thedirectory, csvFilename)
        theFile = open(pathForResourceFile, 'r')
        allLines = theFile.readlines()
        theFile.close()
        return allLines

    def getCoordinates(self, linesFromCsvFile: list[str]) -> list[Coordinates]:
        listOfCoordinates: list[Coordinates] = []
        for i, line in enumerate(linesFromCsvFile):
            # for (int i = 1; i <linesFromCsvFile.size(); i++) { // skipping the first line i.e. starting at index 1
            # String line = linesFromCsvFile.get(i);
            if i > 0:
                listOfCoordinates.append(Coordinates(line))
        return listOfCoordinates

    def test_assertThatTransformationsDoNotDifferTooMuchFromExpectedResultInFile(self):
        linesFromCsvFile = self.readAllLinesFromResourceFile()
        """
        // The first two lines of the input file (the header row, and a data row):
            // EPSG 4326 (WGS84)Longitude for WGS84 (EPSG 4326)|Latitude for WGS84 (EPSG 4326)|EPSG 3006|X for EPSG 3006|Y for EPSG 3006|EPSG 3007-3024|X for EPSG 3007-3024|Y for EPSG 3007-3024|Implementation count for EPSG 3006 transformation|Implementation count for EPSG 3007-3024 transformation
            // 4326|12.146151472138385|58.46573396912418|3006|333538.2957000149|6484098.2550872|3007|158529.85136620898|6483166.205771873|6|6
        // The last two columns can be ignored here, but the first nine columns are in three pairs with three columns each:
        // an epsg number, and then the longitude(x) and latitude(y) for that coordinate.
        // All three coordinates in one row represents the same location but in different coordinate reference systems.
        // The first two, of the three, coordinates are for the same coordinate reference systems, WGS84 and SWEREF99TM,
        // but the third is different for all rows (18 data rows for the local swedish CRS systems, RT90 and SWEREF99, with EPSG codes 3007-3024).

        // The below loop iterates all lines and makes transformations between (to and from) the three coordinate reference systems
        // and verifies the expected result according to the file, and asserts with an error if the difference is too big.
        // Note that the expected coordinates have been calculated in another project, by using a median value for 6 different implementations.
        // (and the number 6 is actually what the last columns means i.e. how many implementations were used to create the data file)
        """
        listOfCoordinates = self.getCoordinates(linesFromCsvFile)
        self.assertEqual(18, len(listOfCoordinates))
        problemTransformationResults: list[str] = []
        numberOfTransformations: int = 0
        for listOfCoordinatesWhichRepresentTheSameLocation in listOfCoordinates: #type: Coordinates
            coordinates: list[CrsCoordinate] = listOfCoordinatesWhichRepresentTheSameLocation.coordinateList
            for i in range(len(coordinates)):
            # for(int i=0; i<coordinates.size()-1; i++) {
                # for(int j=i+1; j<coordinates.size(); j++) {
                for j in range(len(coordinates)):
                    if (j > i):
                        self.transform(coordinates[i], coordinates[j], problemTransformationResults)
                        self.transform(coordinates[j], coordinates[i], problemTransformationResults)
                        numberOfTransformations += 2

        if (len(problemTransformationResults) > 0):
            for s in problemTransformationResults:
                print(s)

        self.assertEqual(0, len(problemTransformationResults), "For further details see the Console output")

        expectedNumberOfTransformations = 108  # for an explanation, see the lines below:
        """
        // Each line in the input file "swedish_crs_coordinates.csv" has three coordinates (and let's below call then A B C)
        // and then for each line we should have done six number of transformations:
        // A ==> B
        // A ==> C
        // B ==> C
        // (and three more in the opposite directions)
        // And there are 18 local CRS for sweden (i.e number of data rows in the file)
        // Thus the total number of transformations should be 18 * 6 = 108
        """
        self.assertEquals(expectedNumberOfTransformations, numberOfTransformations)




    def transform(self,
        sourceCoordinate: CrsCoordinate,
        targetCoordinateExpected: CrsCoordinate,
        problemTransformationResults: list[str]
    ):
        targetCrs: CrsProjection = targetCoordinateExpected.get_crs_projection()
        targetCoordinate: CrsCoordinate = sourceCoordinate.transform(targetCrs)
        isTargetEpsgWgs84: bool = targetCrs.is_wgs84()
        # double maxDifference = isTargetEpsgWgs84 ? 0.000002 : 0.2;   // fails, Epsg 3022 ==> 4326 , diffLongitude 2.39811809521484E-06
        # double maxDifference = isTargetEpsgWgs84 ? 0.000003 : 0.1;     // fails, Epsg 4326 ==> 3022 , diffLongitude 0.117090131156147
        maxDifference = 0.000003 if isTargetEpsgWgs84 else 0.2  # the other (i.e. non-WGS84) are using meter as unit, so 0.2 is just two decimeters difference
        diffLongitude = abs((targetCoordinate.get_longitude_x() - targetCoordinateExpected.get_longitude_x()))
        diffLatitude = abs((targetCoordinate.get_latitude_y() - targetCoordinateExpected.get_latitude_y()))

        if (diffLongitude > maxDifference or diffLatitude > maxDifference):
            problem = f"""
                "Projection {sourceCoordinate.get_crs_projection()} ==> {targetCoordinateExpected.get_crs_projection()} ,
                diffLongitude {diffLongitude}  , diffLatitude {diffLatitude}"
                "sourceCoordinate xLongitude/yLatitude: {sourceCoordinate.get_longitude_x()}/{sourceCoordinate.get_latitude_y()}"
                "targetCoordinate xLongitude/yLatitude: {targetCoordinate.get_longitude_x()}/{targetCoordinate.get_latitude_y()}"
                "targetCoordinateExpected xLongitude/yLatitude: {targetCoordinateExpected.get_longitude_x()}/{targetCoordinateExpected.get_latitude_y()}"
            """
            problemTransformationResults.append(problem)

class Coordinates:
    def __init__(self, lineFromFile: str):
        array = lineFromFile.split(TransformingCoordinatesFromFileTest.columnSeparator)
        self.coordinateList = [
            # Note that the order of the parameters in the input file (with its lines being used here)
            # are in the order x/Longitude first, but the create method below takes the y/Latitude first
            # (and therefore the parameters are not in the sequential order regarding the array indexes)
            CrsCoordinate.create_coordinate_by_epsg_number(int(array[0]), float(array[2]), float(array[1])),
            CrsCoordinate.create_coordinate_by_epsg_number(int(array[3]), float(array[5]), float(array[4])),
            CrsCoordinate.create_coordinate_by_epsg_number(int(array[6]), float(array[8]), float(array[7]))
        ]
