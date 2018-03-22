import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_239 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test maxSlidingWindow 001"
        source = [1,3,-1,-3, 5, 3, 6, 7]
        k = 3
        res = self.obj.maxSlidingWindow(source, k)
        expectedAns = [3,3,5,5,6,7]
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test maxSlidingWindow 002"
        source = [1, 1, 1, -1, 1]
        k = 4
        res = self.obj.maxSlidingWindow(source, k)
        expectedAns = [1, 1]
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test maxSlidingWindow 003"
        source = []
        k = 0
        res = self.obj.maxSlidingWindow(source, k)
        expectedAns = []
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test maxSlidingWindow 004"
        source = [4, 0, 4, 3, 3]
        k = 2
        res = self.obj.maxSlidingWindow(source, k)
        expectedAns = [4, 4, 4, 3]
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

