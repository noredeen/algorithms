import math


class Solution:
    def max_subarray(self, nums: list[int]) -> int:
        return self.find_max(nums, 0, len(nums))

    def find_max_dp(self, nums: list[int], lo: int, hi: int) -> int:
        if lo >= hi:
            return -math.inf

        mid = lo + ((hi - lo) // 2)
        lmax = self.find_max(nums, lo, mid)
        rmax = self.find_max(nums, mid + 1, hi)

        curr = partial_lmax = partial_rmax = 0

        for i in range(mid - 1, lo - 1, -1):
            curr += nums[i]
            partial_lmax = max(curr, partial_lmax)

        curr = 0
        for i in range(mid + 1, hi):
            curr += nums[i]
            partial_rmax = max(curr, partial_rmax)

        best_combined = partial_lmax + nums[mid] + partial_rmax

        return max(lmax, rmax, best_combined)

    # the biggest subarray ending at n is [n] or [M:n]
    def find_max_kadane(self, nums: list[int]):
        current_subarray = max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray


nums1 = [5, 4, -1, 7, 8]
nums2 = [-2,1,-3,4,-1,2,1,-5,4]
nums3 = [-1]
print(Solution().find_max_kadane(nums1, 0, len(nums1)))
