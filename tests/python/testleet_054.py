import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_054 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test spiralOrder with odd columns and rows"
        source1 = [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        res = self.obj.spiralOrder(source1)
        expectedAns = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test spiralOrder with only one item"
        source1 = [[1]]
        res = self.obj.spiralOrder(source1)
        expectedAns = [1]
        self.assertEqual(expectedAns, res)
    
    def test003(self):
        print "test spiralOrder with even columns and rows"
        source1 = [
            [1, 2],
            [3, 4],
        ]
        res = self.obj.spiralOrder(source1)
        expectedAns = [1, 2, 4, 3]
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test spiralOrder with empty matrix"
        source1 = []
        res = self.obj.spiralOrder(source1)
        expectedAns = []
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test spiralOrder with even rows and odd columns"
        source1 = [
            [1, 2, 3],
            [6, 5, 4],
        ]
        res = self.obj.spiralOrder(source1)
        expectedAns = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expectedAns, res)

    def test006(self):
        print "test spiralOrder with even rows and odd columns"
        source1 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        res = self.obj.spiralOrder(source1)
        expectedAns = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6 ,7, 11, 10]
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 