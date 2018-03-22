#!/usr/bin/python
#encoding: utf-8 
import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_172 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        num1 = 9
        res = self.obj.trailingZeroes(num1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        num1 = 10
        res = self.obj.trailingZeroes(num1)
        expectedAns = 2
        self.assertEqual(expectedAns, res)

    def test003(self):
        num1 = 0
        res = self.obj.trailingZeroes(num1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)

    def test004(self):
        num1 = 10000
        res = self.obj.trailingZeroes(num1)
        expectedAns = 2499
        self.assertEqual(expectedAns, res)

    def test005(self):
        num1 = 5
        res = self.obj.trailingZeroes(num1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 
