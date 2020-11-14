import unittest
from city_functions import cities


class CityCountryTest(unittest.TestCase):
    """test for city_functions.py"""

    def test_city_country(self):
        formatted_city_country = cities("santiago", "chile", 1000)
        self.assertEqual(formatted_city_country, "Santiago, Chile - population 1000")

unittest.main()