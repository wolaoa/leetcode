import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_674 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test findLengthOfLCIS 001"
        source = [1, 3, 5, 4, 7]
        res = self.obj.findLengthOfLCIS(source)
        expectedAns = 3
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test findLengthOfLCIS 002"
        source = [2, 2 ,2 ,2 ,2]
        res = self.obj.findLengthOfLCIS(source)
        expectedAns = 1
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test findLengthOfLCIS 003"
        source = [1, 3 , 10, 3, 5, 7, 9]
        res = self.obj.findLengthOfLCIS(source)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test findLengthOfLCIS 004"
        source = [1]
        res = self.obj.findLengthOfLCIS(source)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test findLengthOfLCIS 005"
        source = []
        res = self.obj.findLengthOfLCIS(source)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

