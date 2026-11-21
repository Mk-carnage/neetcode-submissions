class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        sorted_count = sorted(count,key = lambda x: count[x],reverse = True)
        return sorted_count[:k]