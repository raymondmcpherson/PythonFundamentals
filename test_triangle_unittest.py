import unittest
from triangle import area
from triangle import perimeter
from triangle import semiperimeter

class TestTriangle(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def testArea(self):
        self.assertEqual(area(3,4), 6)
        self.assertEqual(area(7,4), 14)

    def testPerimiter(self):
        self.assertEqual(perimeter(3,4,5), 12) 
        self.assertEqual(perimeter(10.5,6,9.3), 25.8)

    def testSemiPerimeter(self):
        self.assertEqual(semiperimeter(3,4,5), 6)
        self.assertEqual(semiperimeter(10.5,6,9.3), 12.9)

if __name__ == '__main__':
    unittest.main()
