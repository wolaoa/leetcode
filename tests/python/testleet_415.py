import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_415 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test addStrings 001"
        source1 = "0"
        target = "0"
        res = self.obj.addStrings(source1, target)
        expectedAns = "0" 
        self.assertItemsEqual(expectedAns, res)
    
    def test002(self):
        print "test addStrings 002"
        source1 = "9" 
        target = "99"
        res = self.obj.addStrings(source1, target)
        expectedAns = "108" 
        self.assertItemsEqual(expectedAns, res)
    
    def test003(self):
        print "test addStrings 003 with only one item"
        source1 = "11"
        target = "9"
        res = self.obj.addStrings(source1, target)
        expectedAns = "20" 
        self.assertItemsEqual(expectedAns, res)
    
    def test004(self):
        print "test addStrings 003 with only one item"
        source1 = "819283948192384813984911"
        target = "9"
        res = self.obj.addStrings(source1, target)
        expectedAns= "819283948192384813984920"
        self.assertItemsEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 
