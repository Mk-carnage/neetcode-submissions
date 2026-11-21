class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicate = []
        for num in nums:
            if num in seen:
                duplicate.append(num)
            else:
                seen.add(num)
        if len(duplicate)>0:
            return True
        else:
            return False