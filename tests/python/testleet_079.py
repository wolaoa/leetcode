import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_079 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test exist with same columns and rows"
        source1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word    = "ABCCED"
        res = self.obj.exist(source1, word)
        expectedAns = True
        self.assertEqual(expectedAns, res)
 
    def test002(self):
        print "test exist with only one line"
        source1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word    = "SEE"
        res = self.obj.exist(source1, word)
        expectedAns = True
        self.assertEqual(expectedAns, res)

    def test003(self):
        print "test exist with more then one line"
        source1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word    = "ABCB"
        res = self.obj.exist(source1, word)
        expectedAns = False
        self.assertEqual(expectedAns, res)

    def test004(self):
        print "test exist with many line"
        source1 = [["a"]]
        word    = "a"
        res = self.obj.exist(source1, word)
        expectedAns = True
        self.assertEqual(expectedAns, res)

    def test005(self):
        print "test exist with many line"
        source1 = [["a"]]
        word    = "b"
        res = self.obj.exist(source1, word)
        expectedAns = False
        self.assertEqual(expectedAns, res)

    def test006(self):
        print "test exist with many line"
        source1 = [["C","A","A"],["A","A","A"],["B","C","D"]]
        word    = "AAB"
        res = self.obj.exist(source1, word)
        expectedAns = True
        self.assertEqual(expectedAns, res)

    def test007(self):
        print "test exist with many line"
        source1 = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
        word    = "aaaaaaaaaaab"
        res = self.obj.exist(source1, word)
        expectedAns = False
        self.assertEqual(expectedAns, res)
    


if __name__=='__main__':
    unittest.main() 