import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
sys.path.append(CURRDIR)
from leet_091 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test restoreIpAddresses with same columns and rows"
        source1 = "0000"
        res = self.obj.restoreIpAddresses(source1)
        expectedAns = ["0.0.0.0"]
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test restoreIpAddresses with same columns and rows"
        source1 = "00012"
        res = self.obj.restoreIpAddresses(source1)
        expectedAns = ["0.0.0.12"]
        self.assertEqual(expectedAns, res)

    
    def test003(self):
        print "test restoreIpAddresses with same columns and rows"
        source1 = "010010"
        res = self.obj.restoreIpAddresses(source1)
        expectedAns = ["0.10.0.10","0.100.1.0"]
        self.assertEqual(expectedAns, res)
    
    def test004(self):
        print "test restoreIpAddresses with same columns and rows"
        source1 = "25525511135"
        res = self.obj.restoreIpAddresses(source1)
        expectedAns = ["255.255.11.135","255.255.111.35"]
        self.assertEqual(expectedAns, res)
      
    def test005(self):
        print "test restoreIpAddresses with same columns and rows"
        source1 = "101023"
        res = self.obj.restoreIpAddresses(source1)
        expectedAns = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 