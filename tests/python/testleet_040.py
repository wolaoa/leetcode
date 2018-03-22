import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_040 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test combinationSum2 001"
        source1 = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        res = self.obj.combinationSum2(source1, target)
        expectedAns = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        self.assertItemsEqual(expectedAns, res)
    
    def test002(self):
        print "test combinationSum2 002"
        source1 = [10, 1, 2, 7, 6, 1, 5]
        target = 7
        res = self.obj.combinationSum2(source1, target)
        expectedAns = [[1, 1, 5], [1, 6], [2, 5], [7]]
        self.assertItemsEqual(expectedAns, res)
    
    def test003(self):
        print "test combinationSum2 003 with only one item"
        source1 = [1]
        target = 1
        res = self.obj.combinationSum2(source1, target)
        expectedAns = [[1]]
        self.assertItemsEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 