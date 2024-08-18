class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        left = [0] * n
        # print(left)
        right = [0] * n

        # Fill left array
        left[0] = height[0]
        for i in range(1, n):
            # print(left[i - 1], height[i])
            left[i] = max(left[i - 1], height[i])

        # Fill right array
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        # Calculate trapped water
        trappedWater = 0
        for i in range(n):
            trappedWater += min(left[i], right[i]) - height[i]

        return trappedWater



s=Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
print(s.trap([4,2,0,3,2,5])) #9