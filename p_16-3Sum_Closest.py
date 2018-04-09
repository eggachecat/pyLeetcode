class Solution:
    def threeSumClosest(self, nums, target):

        ctr = 0
        best_diff = 1000000000
        best_sum = 0

        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_3 = nums[i] + nums[l] + nums[r]

                diff = sum_3 - target


                if best_diff > abs(diff):
                    best_sum = sum_3
                    best_diff = abs(diff)

                if diff < 0:
                    l += 1
                    ctr += 1
                elif diff > 0:
                    r -= 1
                    ctr += 1
                else:
                    return best_sum
        return best_sum


if __name__ == '__main__':
    s_ = Solution()
    nums = [0, 1, 1, 1]
    print(s_.threeSumClosest(nums, -100))
    # s_.threeSum_2(nums)
    # 4498500
    # 4426229
