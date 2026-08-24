class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     Duplicate = set()
     for i in nums:
        if i in Duplicate:
            return True 
        Duplicate.add(i)
     return False 

        