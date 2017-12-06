import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_231 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test isPowerOfTwo with same columns and rows"
        source1 = 1
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = True
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test isPowerOfTwo with same columns and rows"
        source1 = 0
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = False
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test isPowerOfTwo with same columns and rows"
        source1 = 2
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = True
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test isPowerOfTwo with 1025"
        source1 = 1025
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = False
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test isPowerOfTwo with same columns and rows"
        source1 = 1024
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = True
        self.assertEqual(expectedAns, res)


    def test006(self):
        print "test isPowerOfTwo with negative nums"
        source1 = -1
        res = self.obj.isPowerOfTwo(source1)
        expectedAns = False
        self.assertEqual(expectedAns, res)


if __name__=='__main__':
    unittest.main() 