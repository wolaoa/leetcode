import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_763 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test partitionLabels 001"
        source = "ababcbacadefegdehijhklij"
        res = self.obj.partitionLabels(source)
        expectedAns = [9, 7, 8]
        self.assertEqual(expectedAns, res)

    def test002(self):
        print "test partitionLabels 002"
        source = "acjkajksdfqojaosdjfoadjioajdfads"
        res = self.obj.partitionLabels(source)
        expectedAns = [32]
        self.assertEqual(expectedAns, res)
        
    def test003(self):
        print "test partitionLabels 003"
        source = "a"
        res = self.obj.partitionLabels(source)
        expectedAns = [1]
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test partitionLabels 004"
        source = "aaaaaaaaa"
        res = self.obj.partitionLabels(source)
        expectedAns = [9]
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test partitionLabels 005"
        source = "asdfasdfiioipiopqwerqwerlkklklzxcvcx"
        res = self.obj.partitionLabels(source)
        expectedAns = [8,8,8,6,1,5]
        self.assertEqual(expectedAns, res)

if __name__ == "__main__":
    unittest.main()

