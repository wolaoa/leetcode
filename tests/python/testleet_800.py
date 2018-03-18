import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_800 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test similarRGB with same columns and rows"
        source1 = "#09f166"
        res = self.obj.similarRGB(source1)
        expectedAns = "#11ee66"
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test similarRGB with only one line"
        source1 = "#abcdef"
        res = self.obj.similarRGB(source1)
        expectedAns = "#aaccee"
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test similarRGB with more then one line"
        source1 = "#16239f"
        res = self.obj.similarRGB(source1)
        expectedAns = "#112299"
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test similarRGB with more then one line"
        source1 = "#16ffef"
        res = self.obj.similarRGB(source1)
        expectedAns = "#11ffee"
        self.assertEqual(expectedAns, res)
if __name__=='__main__':
    unittest.main() 