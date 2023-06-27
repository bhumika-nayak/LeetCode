class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if (nums[i]==val):
                nums[i]=101
        nums.sort()
        for i in range(len(nums)):
            if (nums[i]<101):
                k=k+1
            else:
                break
        return k
            
        
            
                
                
        