import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
sys.path.append(CURRDIR)
from leet_071 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test simplifyPath with same columns and rows"
        source1 = "/"
        res = self.obj.simplifyPath(source1)
        expectedAns = "/"
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test simplifyPath with same columns and rows"
        source1 = "/home/"
        res = self.obj.simplifyPath(source1)
        expectedAns = "/home"
        self.assertEqual(expectedAns, res)

    
    def test003(self):
        print "test simplifyPath with same columns and rows"
        source1 = "/a/./b/../../c/"
        res = self.obj.simplifyPath(source1)
        expectedAns = "/c"
        self.assertEqual(expectedAns, res)
    
    def test004(self):
        print "test simplifyPath with same columns and rows"
        source1 = ""
        res = self.obj.simplifyPath(source1)
        expectedAns = "/"
        self.assertEqual(expectedAns, res)
      
    def test005(self):
        print "test simplifyPath with same columns and rows"
        source1 = "//a/../b/../c/../../"
        res = self.obj.simplifyPath(source1)
        expectedAns = "/"
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 