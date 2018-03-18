import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_198 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test rob with same columns and rows"
        source1 = []
        res = self.obj.rob(source1)
        expectedAns = 0
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test rob with only one line"
        source1 = [1]
        res = self.obj.rob(source1)
        expectedAns = 1
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test rob with more then one line"
        source1 = [1, 2]
        res = self.obj.rob(source1)
        expectedAns = 2
        self.assertEqual(expectedAns, res)
 
    def test004(self):
        print "test rob with only one line"
        source1 = [1, 5, 2, 6, 9, 8, 7]
        res = self.obj.rob(source1)
        expectedAns = 21
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test rob with more then one line"
        source1 = [1,1,2,1]
        res = self.obj.rob(source1)
        expectedAns = 3
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 