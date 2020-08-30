class Solution:
    def findRepeatNumber(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

        return

if __name__ == '__main__':
    solution = Solution()
    # m = [2, 3, 1, 0, 2, 5, 3]
    # solution.quick_sort(m, 0, len(m) - 1)
    # print(m)
    print(solution.findRepeatNumber([3, 1, 2, 3]))