import unittest
from temperature import convert_to_celsius
from temperature import convert_to_fahrenheit

class TestTemperature(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def testCelsius(self):
        self.assertEqual(convert_to_celsius(32), 0.0)
        self.assertEqual(convert_to_celsius(212), 100.0)

    def testFahrenheit(self):
        self.assertEqual(convert_to_fahrenheit(0), 32)
        self.assertEqual(convert_to_fahrenheit(100), 212)

    def testNegativeCelsius(self):
        self.assertEqual(convert_to_celsius(-20), -28.88888888888889)

if __name__ == '__main__':
    unittest.main()
