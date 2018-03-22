import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_165 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test compareVersion 001"
        source1 = "0"
        target = "0"
        res = self.obj.compareVersion(source1, target)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test compareVersion 002"
        source1 = "0"
        target = "1.0"
        res = self.obj.compareVersion(source1, target)
        expectedAns = -1 
        self.assertEqual(expectedAns, res)
    
    def test003(self):
        print "test compareVersion 003 with only one item"
        source1 = "1"
        target = "1.1"
        res = self.obj.compareVersion(source1, target)
        expectedAns = -1
        self.assertEqual(expectedAns, res)
    
    def test004(self):
        print "test compareVersion 003 with only one item"
        source1 = "1.0.0.0"
        target = "1"
        res = self.obj.compareVersion(source1, target)
        expectedAns= 0
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test compareVersion 003 with only one item"
        source1 = "123.123.123.123412341234"
        target = "123.123.123"
        res = self.obj.compareVersion(source1, target)
        expectedAns= 1
        self.assertEqual(expectedAns, res)


if __name__=='__main__':
    unittest.main() 
