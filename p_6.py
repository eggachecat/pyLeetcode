import numpy as np
import math


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        s = [ord(c) for c in s]
        len_even = numRows
        len_odd = numRows - 2
        ans = np.zeros((numRows, math.ceil(len(s) / (numRows - 1))))
        i = 0
        while True:
            if len(s) == 0:
                break
            if i % 2 == 0:
                for j, c in enumerate(s[:len_even]):
                    ans[j, i] = c
                s = s[len_even:]
            else:
                for j, c in enumerate(s[:len_odd]):
                    ans[len_odd - j, i] = c
                s = s[len_odd:]

            i += 1
        return "".join([chr(c) for c in ans[np.nonzero(ans)].astype(int)])


s_ = Solution()
print(s_.convert("ABCDE", 4))
