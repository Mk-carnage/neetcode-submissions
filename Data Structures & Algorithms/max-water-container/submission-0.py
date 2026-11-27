class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left  = 0
        right = len(heights) -1
        area = 0

        while left < right :
            minheight = min(heights[left],heights[right])
            current_area = minheight * (right-left)
            area = max(area,current_area)

            if heights[left] < heights[right]:
                left +=1
            else:
                right-=1
            
            
        return area