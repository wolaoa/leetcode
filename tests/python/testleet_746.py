import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_746 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test minCostClimbingStairs with same columns and rows"
        source1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        res = self.obj.minCostClimbingStairs(source1)
        expectedAns = 6
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test minCostClimbingStairs with only one line"
        source1 = [10, 15, 20]
        res = self.obj.minCostClimbingStairs(source1)
        expectedAns = 15
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test minCostClimbingStairs with more then one line"
        source1 = [0,0,0,0]
        res = self.obj.minCostClimbingStairs(source1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 