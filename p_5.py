class Solution:
    def transform(self, s):
        s_ = []
        for c in s:
            s_.extend(["#", c])
        return "".join(s_ + ["#"])

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ctr = [0]
        max_len = 1
        s = self.transform(s)
        for i in range(1, len(s)):
            c = s[i]



s = Solution()
print(s.transform("asdas"))
# print(s.isPalindrome("bb"))
# print(s.longestPalindrome("aaaabaaa"))

# class Solution:
#     def isPalindrome(self, s):
#         for i in range(len(s) // 2):
#             if s[i] != s[-i - 1]:
#                 return False
#         return True
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         len_ = 1
#         p = s[0]
#
#         for i in range(1, len(s)):
#             s_ = s[:i + 1]
#             p_ = s_[-len_ - 1:]
#             p__ = s_[-len_ - 2:]
#             # print(s_, len_, p_, p__)
#
#             if self.isPalindrome(p__):
#                 p = p__
#                 len_ = len(p__)
#             elif self.isPalindrome(p_):
#                 p = p_
#                 len_ = len(p_)
#         return p
#
#
# s = Solution()
# # print(s.isPalindrome("bb"))
# print(s.longestPalindrome("aaaabaaa"))
