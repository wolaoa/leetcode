import os
import sys

CURRDIR = os.path.abspath("../../python/")
print CURRDIR
sys.path.append(CURRDIR)
from leet_033 import Solution

if __name__ == "__main__":
    sol = Solution()
    source1 = [0, 1, 2, 4, 5, 6, 7]
    res = sol.search(source1, 2)
    print res

    source2 = [4, 5, 6, 7, 0, 1, 2]
    res = sol.search(source2 , 2)
    print res
    
    source3 = [5, 6, 7, 0, 1, 2, 4]
    res = sol.search(source3, 2)
    print res

    source4 = [5, 6, 7, 0, 1, 2, 4]
    res = sol.search(source3, 8)
    print res
    