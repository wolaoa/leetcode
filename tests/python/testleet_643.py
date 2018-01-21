import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_643 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test findMaxAverage 001"
        source = [1,12,-5,-6,50,3]
        k = 4
        res = self.obj.findMaxAverage(source, k)
        expectedAns = 12.75000
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test findMaxAverage 002"
        source = [1, 1, 1, -1, 1]
        k = 4
        res = self.obj.findMaxAverage(source, k)
        expectedAns = 0.50000
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test findMaxAverage 003"
        source = [1, 2, 3, 4, 5, 6,7, 8]
        k = 4
        res = self.obj.findMaxAverage(source, k)
        expectedAns = 6.50000
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test findMaxAverage 004"
        source = [4,0,4,3,3]
        k = 5
        res = self.obj.findMaxAverage(source, k)
        expectedAns = 2.80000
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

