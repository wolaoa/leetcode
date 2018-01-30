import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_056 import *

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test merge with odd columns and rows"
        inputs = [[1,3],[2,6],[8,10],[15,18]]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1,6],[8,10],[15,18]]
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test merge with only one item"
        inputs = [[1, 1]]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1, 1]]
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)    

    def test003(self):
        print "test merge with even columns and rows"
        inputs = [
            [1, 2],
            [3, 4],
        ]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1, 2], [3, 4]]
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

    def test004(self):
        print "test merge with empty matrix"
        inputs = []
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = []
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  
    def test005(self):
        print "test merge with even rows and odd columns"
        inputs = [
            [1, 4],
            [2, 3],
        ]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1, 4]]
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

    def test006(self):
        print "test merge with even rows and odd columns"
        inputs = [
            [1, 4],
            [2, 5],
            [3, 6],
            [6, 7]
        ]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1,7]]
        outputs = self.obj.merge(source1)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

if __name__=='__main__':
    unittest.main() 