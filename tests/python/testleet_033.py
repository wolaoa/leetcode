import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_033 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test strStr 001"
        source1 = [0, 1, 2, 4, 5, 6, 7]
        res = self.obj.search(source1, 2)
        expectedAns = 2
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test strStr 001"
        source2 = [4, 5, 6, 7, 0, 1, 2]
        res = self.obj.search(source2 , 2)
        expectedAns = 6
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test strStr 001"
        source3 = [5, 6, 7, 0, 1, 2, 4]
        res = self.obj.search(source3, 2)
        expectedAns = 5
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test strStr 001"
        source4 = [5, 6, 7, 0, 1, 2, 4]
        res = self.obj.search(source4, 8)
        expectedAns = -1
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 

