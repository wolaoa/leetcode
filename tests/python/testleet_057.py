import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_057 import *

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test insert with odd columns and rows"
        inputs = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))

        inserted = Interval(4,9)
        expectedAns = [[1,2],[3,10],[12,16]]
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test insert with only one item"
        inputs = [[1, 1]]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        inserted = Interval(4,9)
        expectedAns = [[1, 1], [4, 9]]
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)    

    def test003(self):
        print "test insert with even columns and rows"
        inputs = [
            [1, 2],
            [3, 4],
        ]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[1,2], [3,9]]
        inserted = Interval(4,9)
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

    def test004(self):
        print "test insert with empty matrix"
        inputs = []
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        expectedAns = [[0,0]]
        inserted = Interval(0,0)
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

    def test005(self):
        print "test insert with even rows and odd columns"
        inputs = [
            [1, 2],
            [3, 4],
        ]
        source1 = []
        for source in inputs:
            source1.append(Interval(source[0], source[1]))
        inserted = Interval(2, 3)
        expectedAns = [[1, 4]]
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

    def test006(self):
        print "test insert with even rows and odd columns"
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
        inserted = Interval(2, 5)
        outputs = self.obj.insert(source1, inserted)
        res = []
        for output in outputs:
            res.append([output.start, output.end])
        self.assertEqual(expectedAns, res)  

if __name__=='__main__':
    unittest.main() 