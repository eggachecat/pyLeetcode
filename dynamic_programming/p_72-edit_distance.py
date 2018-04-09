import numpy as np


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        if len(word1) * len(word2) == 0:
            return len(word1) + len(word2)

        word1 = "#" + word1
        word2 = "#" + word2
        len1 = len(word1)
        len2 = len(word2)

        if len1 * len2 == 0:
            return len1 + len2

        D = [[0 for j in range(len2)] for i in range(len1)]
        for _ in range(len1):
            D[_][0] = _
        for _ in range(len2):
            D[0][_] = _

        for i in range(1, len1):
            for j in range(1, len2):
                D[i][j] = min([D[i - 1][j] + 1, D[i][j - 1] + 1,
                               D[i - 1][j - 1] if word1[i] == word2[j] else D[i - 1][j - 1] + 1])

        return D[len1 - 1][len2 - 1]


if __name__ == '__main__':
    w1 = "plasma"

    w2 = "altruism"
    s = Solution()
    print(s.minDistance(w1, w2))
