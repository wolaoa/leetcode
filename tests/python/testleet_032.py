import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_032 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test strStr 001"
        source = "(((()(())"
        res = self.obj.longestValidParentheses(source)
        expectedAns = 6
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test strStr 001"
        source = "((()))())"
        res = self.obj.longestValidParentheses(source)
        expectedAns = 8
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test strStr 001"
        source = ")(((())())()))))((((())))))()()(()()()()()"
        res = self.obj.longestValidParentheses(source)
        expectedAns = 12
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test strStr 001"
        source = "()()"
        res = self.obj.longestValidParentheses(source)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test strStr 001"
        source = "))()()()()())((((())))))))"
        res = self.obj.longestValidParentheses(source)
        expectedAns = 10
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 

