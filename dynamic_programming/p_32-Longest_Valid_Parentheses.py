class Solution:
    def countParentheses(self, s):
        lc, rc = 0, 0
        for c in s:
            if c == "(":
                lc += 1
            if c == ")":
                rc += 1

        return lc, rc

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "".join(["#" + c for c in s] + ["#"])
        s_l = len(s)

        max_len = 0
        for i in range(2, len(s), 2):
            print("----------------------------")
            for j in range(2, i, 2):
                if i + j < s_l:
                    ll, lr = self.countParentheses(s[i - j:i])
                    rl, rr = self.countParentheses(s[i:i + j])
                    if ll == rr and lr == rl and ll >= lr:
                        len_ = ll + lr
                        print(s[i - j:i], s[i:i + j], ll + lr)
                        if len_ > max_len:
                            max_len = len_

        print(max_len * 2)


if __name__ == '__main__':
    s = Solution()
    t = ")()())(()())"
    print(s.longestValidParentheses(t))
