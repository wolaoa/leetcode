#!/usr/bin/python
#encoding: utf-8 
import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_039 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test combinationSum 001"
        source1 = [2, 3, 6, 7] 
        target = 7
        res = self.obj.combinationSum(source1, target)
        expectedAns = [[2, 2, 3], [7]]
        self.assertItemsEqual(expectedAns, res)
    
    def test002(self):
        print "test combinationSum 002"
        source1 = [10, 1, 2, 7, 6, 5]
        target = 7
        res = self.obj.combinationSum(source1, target)
        expectedAns = [
            [1, 1, 5], 
            [1, 6], 
            [2, 5], 
            [7], 
            [1, 1, 1, 1, 1, 1, 1], 
            [1, 1, 1, 1, 1, 2], 
            [1, 1, 1, 2, 2], 
            [1, 2 ,2, 2]]
        self.assertItemsEqual(expectedAns, res)
    
    def test003(self):
        print "test combinationSum 003 with only one item"
        source1 = [1]
        target = 1
        res = self.obj.combinationSum(source1, target)
        expectedAns = [[1]]
        self.assertItemsEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 