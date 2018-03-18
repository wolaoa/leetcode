import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_338 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test countBits with same columns and rows"
        source1 = 2
        res = self.obj.countBits(source1)
        expectedAns = [0,1,1]
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test countBits with only one line"
        source1 = 0
        res = self.obj.countBits(source1)
        expectedAns = [0]
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test countBits with more then one line"
        source1 = 10
        res = self.obj.countBits(source1)
        expectedAns = [0,1,1,2,1,2,2,3,1,2,2]
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 