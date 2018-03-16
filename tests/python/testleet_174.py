import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_174 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test calculateMinimumHP with same columns and rows"
        source1 = [[0]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test calculateMinimumHP with only one line"
        source1 = [[-2, -3, 3], [-5, -10, 1],[10, 30, -5]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 7
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test calculateMinimumHP with more then one line"
        source1 = [[10]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test calculateMinimumHP with many line"
        source1 = [[-1]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 2
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test calculateMinimumHP with many line"
        source1 = [[-1, -2],[-1, -5]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 8
        self.assertEqual(expectedAns, res)

    def test006(self):
        print "test calculateMinimumHP with many line"
        source1 = [[1]]
        res = self.obj.calculateMinimumHP(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 