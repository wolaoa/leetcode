import os
import sys

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_722_remove_comments import Solution

if __name__ == "__main__":
    sol = Solution()
    source1 = ["a/*comment", "line", "more_comment*/b"]
    res = sol.removeComments(source1)
    print res

    source2 = [
    "/*Test program */", 
    "int main()", 
    "{ ",
    "  // variable declaration ",
    "int a, b, c;", 
    "/* This is a test",
    "   multiline  ",
    "   comment for ",
    "   testing */", 
    "a = b + c;", 
    "}"
    ]

    res = sol.removeComments(source2)
    print res
