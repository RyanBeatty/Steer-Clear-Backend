from steerclear.utils.polygon import SteerClearGISClient
import unittest
import os

cur_dirname = os.path.join(os.path.dirname(__file__), os.pardir)
shapefile_filename = cur_dirname + '/fixtures/shapefiles/campus_map/campus_map.shp'

"""
SteerClearGISClientTestCase
---------------------------
Test case for testing SteerClearGISClient.
Makes sure that SteerClearGISClient can accurately
classify lat/long pairs as oncampus or off campus
"""
class SteerClearGISClientTestCase(unittest.TestCase):

    def setUp(self):
        self.gis_client = SteerClearGISClient(shapefile_filename)

    def test_is_on_campus_points_in_center_of_campus(self):
        # test with lat/long of william and mary
        self._test_point((37.272433, -76.716922), True)

        # test with lat/long of sadler center
        self._test_point((37.271819, -76.714061), True)

        # test point near randolph complex
        self._test_point((37.270857, -76.719126), True)

        # test point near swem library
        self._test_point((37.269832, -76.716803), True)

        # test point near botetourt
        self._test_point((37.270255, -76.721078), True)

    def test_is_on_campus_points_near_perimeter_of_campus(self):
        # test point near barret hall
        self._test_point((37.269028, -76.711410), True)

        # test point near jefferson hall
        self._test_point((37.269501, -76.710186), True)

        # test point near colonial williamsburg but still on campus
        self._test_point((37.270837, -76.707575), True)

        # test point near blow hall
        self._test_point((37.272114, -76.709993), True)

        # test point near bryan hall
        self._test_point((37.272938, -76.712275), True)

        # test point near zable hall
        self._test_point((37.273959, -76.713427), True)

        # test point near frat castles
        self._test_point((37.274754, -76.718091), True)

        # test point near rec center
        self._test_point((37.274705, -76.720931), True)

        # test point near jamestown south
        self._test_point((37.268358, -76.712992), True)

        # test point near PBK
        self._test_point((37.267523, -76.714738), True)

        # test point near business school
        self._test_point((37.266099, -76.717825), True)

    def test_is_on_campus_points_not_on_campus(self):
        pass

    def _test_point(self, point, result):
        r = self.gis_client.is_on_campus(point)
        self.assertEqual(r, result)