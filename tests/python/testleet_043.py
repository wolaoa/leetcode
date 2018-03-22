#!/usr/bin/python
#encoding: utf-8 
import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_043 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        num1 = '1239489123'
        num2 = '1893894189034812038490'
        res = self.obj.multiply(num1, num2)
        expectedAns = '2347461247421555390057812344270' 
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        num1 = '0'
        num2 = '1893894189034812038490'
        res = self.obj.multiply(num1, num2)
        expectedAns = '0' 
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 
