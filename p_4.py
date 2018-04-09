import numpy as np


# def find_kth(nums_1, nums_2, k):
#     len_1 = len(nums_1)
#     len_2 = len(nums_2)
#
#     if len(nums_1) == 0:
#         return nums_2[k]
#
#     if len(nums_2) == 0:
#         return nums_1[k]
#
#     if len_1 == 1 and len_2 == 1:
#         return max([nums_1[0], nums_2[0]])
#
#     if len_1 > len_2:
#         idx_1 = min([len_1 // 2, k])
#         idx_2 = k - idx_1
#     else:
#         idx_2 = min([len_2 // 2, k])
#         idx_1 = k - idx_2
#
#     n_1 = nums_1[idx_1]
#     n_2 = nums_2[idx_2]
#
#     if n_1 > n_2:
#         return find_kth(nums_1[:idx_1], nums_2[idx_2:], k - idx_2)
#     else:
#         return find_kth(nums_1[idx_1:], nums_2[:idx_2], k - idx_1)
#
#
# if __name__ == '__main__':
#     ctr = 0
#     # np.random.seed(0)
#
#     for _ in range(100):
#         nums_1_ = np.random.randint(0, 10000, 37)
#         nums_2_ = np.random.randint(0, 10000, 28)
#         k_ = 6
#         ans = np.sort(np.hstack((nums_1_, nums_2_)))[k_]
#         res = find_kth(np.sort(nums_1_), np.sort(nums_2_), k_)
#         ctr += int(ans == res)
#         print("ans:", res, ans, ans == res)
#     print(ctr)
#

class Solution:
    def find_kth(self, nums_1, nums_2, k):

        print(nums_1, nums_2, k)

        len_1 = len(nums_1)
        len_2 = len(nums_2)

        if len(nums_1) == 0:
            return nums_2[k]

        if len(nums_2) == 0:
            return nums_1[k]

        if k == len_1 + len_2 - 1:
            return max([nums_1[-1], nums_2[-1]])

        if len_1 < len_2:
            idx_1 = min([len_1 // 2, k])
            idx_2 = k - idx_1
        else:
            idx_2 = min([len_2 // 2, k])
            idx_1 = k - idx_2
        print(nums_1, nums_2, k, len_1, idx_1, len_2, idx_2)
        n_1 = nums_1[idx_1]
        n_2 = nums_2[idx_2]

        if n_1 > n_2:
            return self.find_kth(nums_1[:idx_1], nums_2[idx_2:], k - idx_2)
        else:
            return self.find_kth(nums_1[idx_1:], nums_2[:idx_2], k - idx_1)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)

        total = len_1 + len_2

        if total % 2 == 0:
            return (self.find_kth(nums1, nums2, -1 + total // 2) +
                    self.find_kth(nums1, nums2, total // 2)) / 2
        else:
            return self.find_kth(nums1, nums2, -1 + (total + 1) // 2)


s = Solution()
a = [1]
b = [2]
res = s.findMedianSortedArrays(a, b)
print(res)
