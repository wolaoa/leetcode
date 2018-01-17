#!/usr/bin/python
#encoding: utf-8 
import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_738 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        num1 = 9
        res = self.obj.monotoneIncreasingDigits(num1)
        expectedAns = 9
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        num1 = 10
        res = self.obj.monotoneIncreasingDigits(num1)
        expectedAns = 9
        self.assertEqual(expectedAns, res)

    def test003(self):
        num1 = 1234
        res = self.obj.monotoneIncreasingDigits(num1)
        expectedAns = 1234
        self.assertEqual(expectedAns, res)

    def test004(self):
        num1 = 1243
        res = self.obj.monotoneIncreasingDigits(num1)
        expectedAns = 1239
        self.assertEqual(expectedAns, res)

    def test005(self):
        num1 = 332
        res = self.obj.monotoneIncreasingDigits(num1)
        expectedAns = 299
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 
