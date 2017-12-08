import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_539 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test findMinDifference 001"
        source1 = ["00:00", "00:00"]
        res = self.obj.findMinDifference(source1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test findMinDifference 002"
        source2 = ["00:00","23:58"]
        res = self.obj.findMinDifference(source2)
        expectedAns = 2
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test findMinDifference 003"
        source3 = ["12:31","00:01"]
        res = self.obj.findMinDifference(source3)
        expectedAns = 690
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test findMinDifference 004"
        source4 = ["23:58", "11:32", "12:31", "10:10", "01:02"]
        res = self.obj.findMinDifference(source4)
        expectedAns = 59
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

