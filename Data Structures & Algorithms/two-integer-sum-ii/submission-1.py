class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        viewed = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in viewed:
                return [viewed[complement] + 1, i + 1]

            viewed[num] = i

        return [-1, -1]