import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_300 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test lengthOfLIS 001"
        source = [1, 3, 5, 4, 7]
        res = self.obj.lengthOfLIS(source)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test lengthOfLIS 002"
        source = [2, 2 ,2 ,2 ,2]
        res = self.obj.lengthOfLIS(source)
        expectedAns = 1
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test lengthOfLIS 003"
        source = [1, 3 , 10, 3, 5, 7, 9]
        res = self.obj.lengthOfLIS(source)
        expectedAns = 5
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test lengthOfLIS 004"
        source = [1]
        res = self.obj.lengthOfLIS(source)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test lengthOfLIS 005"
        source = [1,3,6,7,9,4,10,5,6]
        res = self.obj.lengthOfLIS(source)
        expectedAns = 6
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

