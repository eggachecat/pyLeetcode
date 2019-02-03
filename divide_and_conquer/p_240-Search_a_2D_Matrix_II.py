"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
]
Given target = 5, return true.

Given target = 20, return false.
"""


class Solution:

    def searchRow(self, row, target):
        print(row, target)
        l = 0
        r = len(row)
        if r == 0:
            return False
        i = int((l + r) / 2)
        while True:
            if target == row[i]:
                return True

            if l == i or r == i:
                return False

            if target > row[i]:
                l = i
                i = int((i + r) / 2)
                continue

            if target < row[i]:
                r = i
                i = int((l + i) / 2)
                continue

    def searchMatrixFool(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix:
            if self.searchRow(row, target):
                return True

        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        lt = [0, 0]
        rb = [len(matrix) - 1, len(matrix[0]) - 1]
        p = [int((lt[0] + rb[0]) / 2), int((lt[1] + rb[1]) / 2)]

        while True:
            print(lt, p, rb)
            if (lt[0] == p[0] and lt[1] == p[1]) or (rb[0] == p[0] and rb[1] == p[1]):
                break

            if target < matrix[p[0]][p[1]]:
                rb = [p[0], p[1]]
                p = [int((lt[0] + p[0]) / 2), int((lt[1] + p[1]) / 2)]
                continue

            if target > matrix[p[0]][p[1]]:
                lt = [p[0], p[1]]
                p = [int((p[0] + rb[0]) / 2), int((p[1] + rb[1]) / 2)]
                continue

            if target == matrix[p[0]][p[1]]:
                return True
        return self.searchRow(matrix)

if __name__ == '__main__':
    sol = Solution()
    # print(sol.searchRow([1, 2, 3, 4, 5], -1))
    print(sol.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24]], 5))
