class Solution:
    def findRepeatNumber(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return

    # def findRepeatNumber(self, nums):
    #     self.quick_sort(nums, 0, len(nums) - 1)
    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i + 1]:
    #             return nums[i]
    #     return
    #
    # def quick_sort(self, nums, l, r):
    #     if l < r:
    #         i = l
    #         j = r
    #         base = nums[l]
    #         while i < j:
    #             while i < j and nums[j] >= base:
    #                 j -= 1
    #             while i < j and nums[i] <= base:
    #                 i += 1
    #             if i < j:
    #                 nums[i], nums[j] = nums[j], nums[i]
    #
    #         nums[l] = nums[i]
    #         nums[i] = base
    #         self.quick_sort(nums, l, i - 1)
    #         self.quick_sort(nums, i + 1, r)


# def findRepeatNumber(self, nums):
#     tmp = set()
#     for num in nums:
#         if num not in tmp:
#             tmp.add(num)
#         else:
#             return num
#     return


if __name__ == '__main__':
    solution = Solution()
    # m = [2, 3, 1, 0, 2, 5, 3]
    # solution.quick_sort(m, 0, len(m) - 1)
    # print(m)
    print(solution.findRepeatNumber([3, 1, 2, 3]))
