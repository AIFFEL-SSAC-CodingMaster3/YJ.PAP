from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

a = Solution()
a.search([-1,0,3,4,5,7,9,10,12], target = 10)

'''
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x * x + y * y, x, y))

        result = []
        for _ in range(K):
            result.append(heapq.heappop(heap)[1:])
        return result


a = Solution()
a.search([[1,3],[-2,2]], K = 2)
'''