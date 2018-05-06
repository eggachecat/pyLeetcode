import random


class Solution:
    def merge_two_list(self, nums1, nums2):
        l = 0
        r = 0

        len1 = len(nums1)
        len2 = len(nums2)

        merged_arr = []
        while True:
            if l == len1:
                merged_arr += nums2[r:]
                break

            if r == len2:
                merged_arr += nums2[l:]
                break

            if nums1[l] < nums2[r]:
                merged_arr.append(nums1[l])
                l += 1
            else:
                merged_arr.append(nums2[r])
                r += 1
        return merged_arr

    def mergeKLists(self, lists):

        while True:
            n_lists = len(lists)
            if n_lists == 1:
                return lists[0]

            new_lists = []
            pairs = [[i, i + 1] if i + 1 < n_lists else (i,) for i in range(0, n_lists, 2)]

            for pair in pairs:
                if len(pair) == 2:
                    new_lists.append(self.merge_two_list(lists[pair[0]], lists[pair[1]]))
                else:
                    new_lists.append(lists[pair[0]])

            lists = new_lists


if __name__ == '__main__':
    s = Solution()
    k = 5
    nums_lists = [[random.randint(0, 1000) for _ in range(100)] for _ in range(k)]
    for nums_list in nums_lists:
        nums_list.sort()
    merged_arr = s.mergeKLists(nums_lists)
    print(merged_arr)
    ans_arr = []
    for i in range(k):
        ans_arr += nums_lists[i]
    ans_arr.sort()
    print(merged_arr == ans_arr)
