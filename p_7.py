class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) >= 2147483647 // 2:
            return 0

        if x > 0:
            return int("".join(reversed(str(x))))
        else:
            return -1 * int("".join(reversed(str(-x))))


if __name__ == '__main__':
    print(int(0xf7777777))

    sol = Solution()
    print(sol.reverse(1534236469))
