class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lenNum1 = len(nums1)
        lenNum2 = len(nums2)
        
        nums1.sort()
        nums2.sort()
        
        res = set()

        
        i = j = 0
        while i < lenNum1 and j < lenNum2:
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return list(res)
            
        
