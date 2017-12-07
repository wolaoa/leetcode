import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_028 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test strStr 001"
        source1 = ""
        target = ""
        res = self.obj.strStr(source1, target)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test strStr 002"
        source1 = "abasjkdjflasd" 
        target = "zzz"
        res = self.obj.strStr(source1, target)
        expectedAns = -1 
        self.assertEqual(expectedAns, res)
    
    def test003(self):
        print "test strStr 003 with only one item"
        source1 = "asdf"
        target = "asdfa"
        res = self.obj.strStr(source1, target)
        expectedAns = -1
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test strStr 003 with only one item"
        source1 = "asdfksdjlf"
        target = "ksdj"
        res = self.obj.strStr(source1, target)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test strStr 003 with only one item"
        source1 = "ksdj"
        target = "ksdj"
        res = self.obj.strStr(source1, target)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
if __name__=='__main__':
    unittest.main() 
