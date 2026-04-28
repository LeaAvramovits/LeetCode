class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = len(height)*[0]
        maxRight = len(height)*[0]
        max=height[0]
        for i in range(len(height)):
          if height[i]>max:
            max=height[i]
          maxLeft[i]=max
        max_val=0
        for i in range(len(height) - 1, -1, -1):
          if height[i] > max_val:
            max_val = height[i]
          maxRight[i] = max_val
        count=0
        for i in range(len(height)):
          count+=min(maxLeft[i],maxRight[i])-height[i]
        return count
        