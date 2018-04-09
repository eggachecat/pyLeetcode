class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        len_arr = [0 for _ in range(n)]
        len_arr[0] = 1

        for i in range(1, n):
            len_arr[i] = max([1] + [1 + len_arr[j] if nums[j] < nums[i] else 0 for j in range(i)])
            print(len_arr)
        return max(len_arr)


if __name__ == '__main__':
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(nums))




# class Solution:
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         ls = [[] for _ in range(n)]
#         ls[0].append([nums[0]])
#
#         len_arr = [[] for _ in range(n)]
#         len_arr[0].append(1)
#
#         for i in range(1, n):
#             ls[i].append([nums[i]])
#             len_arr[i].append(1)
#
#             for j in range(i):
#                 for idx, k in enumerate(ls[j]):
#                     if k[-1] < nums[i]:
#                         ls[i].append(k + [nums[i]])
#                         len_arr[i].append(len_arr[j][idx] + 1)
#
#         return max(sum(len_arr, []))
