import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_518 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test change 001"
        amount = 5
        source = [1, 2, 5]
        res = self.obj.change(amount, source)
        expectedAns = 4
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test change 002"
        amount = 3
        source = [2]
        res = self.obj.change(amount, source)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test change 003"
        amount = 10
        source = [10]
        res = self.obj.change(amount, source)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test change 004"
        amount = 3
        source = [1, 2]
        res = self.obj.change(amount, source)
        expectedAns = 2
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

