import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_073 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test setZeroes with same columns and rows"
        source1 = []
        res = self.obj.setZeroes(source1)
        expectedAns = []
        self.assertItemsEqual(expectedAns, source1)
 
    def test002(self):
        print "test setZeroes with only one line"
        source1 = [[1]]
        self.obj.setZeroes(source1)
        expectedAns = [[1]]
        self.assertItemsEqual(expectedAns, source1)

    def test003(self):
        print "test setZeroes with more then one line"
        source1 = [[0, 1], [1, 1]]

        self.obj.setZeroes(source1)
        expectedAns = [[0 , 0], [0, 1]]
        self.assertItemsEqual(expectedAns, source1)

    def test004(self):
        print "test setZeroes with many line"
        source1 = [[0, 1 , 0],[1, 1, 1], [0, 1, 0]]

        self.obj.setZeroes(source1)
        expectedAns = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertItemsEqual(expectedAns, source1)

    def test005(self):
        print "test setZeroes with many line"
        source1 = [[0, 1]]

        res = self.obj.setZeroes(source1)
        expectedAns = [[0, 0]]
        self.assertItemsEqual(expectedAns, source1)

if __name__=='__main__':
    unittest.main() 