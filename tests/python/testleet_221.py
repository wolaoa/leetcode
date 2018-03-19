#!/usr/bin/python
#encoding: utf-8 
import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_221 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        num1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        res = self.obj.maximalSquare(num1)
        expectedAns = 4
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        num1 = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
        res = self.obj.maximalSquare(num1)
        expectedAns = 9
        self.assertEqual(expectedAns, res)

    def test003(self):
        num1 = [["0"]]
        res = self.obj.maximalSquare(num1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

    def test004(self):
        num1 = [["1"]]
        res = self.obj.maximalSquare(num1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test005(self):
        num1 = [["1", "0", "1", "1"], ["1", "1", "0", "1"],["1", "1", "1", "0"], ["1", "1", "1", "1"]]
        res = self.obj.maximalSquare(num1)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 
