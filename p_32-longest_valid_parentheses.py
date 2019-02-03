class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_len = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                # c == ")" and start pop
                len = 0
                c_ = stack.pop()
                if c_ == "(":
                    len += 2


if __name__ == '__main__':
    s = Solution()
    s.longestValidParentheses(")()())")
