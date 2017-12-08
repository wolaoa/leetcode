import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_400 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test findNthDigit 001"
        source1 = 8
        
        res = self.obj.findNthDigit(source1)
        expectedAns = 8
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test findNthDigit 002"
        source1 = 11 
        
        res = self.obj.findNthDigit(source1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
    
    def test003(self):
        print "test findNthDigit 003"
        source1 = 189
        
        res = self.obj.findNthDigit(source1)
        expectedAns = 9
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test findNthDigit 004"
        source1 = 190
        
        res = self.obj.findNthDigit(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test findNthDigit 005"
        source1 = 2889
        res = self.obj.findNthDigit(source1)
        expectedAns = 9
        self.assertEqual(expectedAns, res)

    def test006(self):
        print "test findNthDigit 006"
        source1 = 1
        res = self.obj.findNthDigit(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)
if __name__=='__main__':
    unittest.main() 
