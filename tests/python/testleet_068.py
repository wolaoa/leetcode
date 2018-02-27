import os
import sys
import unittest

CURRDIR = os.path.abspath("../../python/")
sys.path.append(CURRDIR)
from leet_068 import Solution

class TestSolution(unittest.TestCase): 
    def setUp(self):
        self.obj = Solution()
    
    def tearDown(self): 
        pass

    def test001(self):
        print "test fullJustify with same columns and rows"
        source1 = [""]
        cnt = 0
        res = self.obj.fullJustify(source1, cnt)
        expectedAns = [""]
        self.assertEqual(expectedAns, res)
    
    def test002(self):
        print "test fullJustify with same columns and rows"
        source1 = ["This", "is", "an", "example", "of", "text", "justification."]
        cnt = 16
        res = self.obj.fullJustify(source1, cnt)
        expectedAns = ["This    is    an","example  of text","justification.  "]
        self.assertEqual(expectedAns, res)

    
    def test003(self):
        print "test fullJustify with same columns and rows"
        source1 = ["This", "is", "an", "example", "of", "text", "justification."]
        cnt = 23
        res = self.obj.fullJustify(source1, cnt)
        expectedAns = ['This  is  an example of', 'text justification.    ']
        self.assertEqual(expectedAns, res)
    
    def test004(self):
        print "test fullJustify with same columns and rows"
        source1 = ["Listen","to","many,","speak","to","a","few."]
        cnt = 6
        res = self.obj.fullJustify(source1, cnt)
        expectedAns = ['Listen', 'to    ', 'many, ', 'speak ', 'to   a', 'few.  ']
        self.assertEqual(expectedAns, res)
      
    def test005(self):
        print "test fullJustify with same columns and rows"
        source1 = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]
        cnt = 12
        res = self.obj.fullJustify(source1, cnt)
        expectedAns = ["My     momma","always said,","\"Life    was","like  a  box","of          ","chocolates. ","You    never","know    what","you're gonna","get.        "]
        self.assertEqual(expectedAns, res)

if __name__=='__main__':
    unittest.main() 