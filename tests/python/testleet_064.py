import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_064 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test minPathSum with same columns and rows"
        source1 = [[1,3,1],[1,5,1],[4,2,1]]

        res = self.obj.minPathSum(source1)
        expectedAns = 7
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test minPathSum with only one line"
        source1 = [[1, 2, 3]]

        res = self.obj.minPathSum(source1)
        expectedAns = 6
        self.assertEqual(expectedAns, res)
    
    def test003(self):
        print "test minPathSum with columns more then rows"
        source1 = [[1, 2 ,3], [4, 5 ,6]]

        res = self.obj.minPathSum(source1)
        expectedAns = 12
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test minPathSum with only one item"
        source1 = [[1]]

        res = self.obj.minPathSum(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test minPathSum with empty matrix"
        source1 = []

        res = self.obj.minPathSum(source1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

    def test006(self):
        print "test minPathSum with rows more than columns"
        source1 = [[1],[3]]
        res = self.obj.minPathSum(source1)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 