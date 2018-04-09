class Solution:
    def isCharMatch(self, s_c, p_c):
        if p_c == ".":
            return True
        return s_c == p_c

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        exist_shit = p.find(".*")
        if exist_shit > 0:
            print(ex)
            exit()

        automato = []
        for i, c in enumerate(p):
            if c == "*":
                if i + 1 < len(p):
                    automato.append([i - 1, i + 1])
                else:
                    automato.append([i - 1])
            else:
                automato.append([i])

        print(automato)
        print([[p[__] for __ in _] for _ in automato])

        terminal_index = len(p)
        i = 0
        j = 0

        while True:
            print("----------")
            print(i, len(s), j)
            if i == len(s):
                if j == terminal_index:
                    return True
                else:
                    if p[-2] == "*" and p[-1] == s[-1]:
                        return True
                    return False

            pattern_index_list = automato[j]
            match = False
            print(pattern_index_list)
            for index in pattern_index_list:
                print(i, s[i], index, p[index])
                if self.isCharMatch(s[i], p[index]):
                    i += 1
                    j = index + 1
                    match = True
                    break

            if not match:
                print("No match!")
                return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isMatch("aaaab", ".*b"))
# exit()
# while True:
#
#     if (j == n_p or (j == n_p - 1 and p[j] == "*")) and i == n_s:
#         return True
#
#     if i == n_s:
#         return False
#
#     print(i, j)
#
#     cur_char = s[i]
#     cur_ptn = p[j] if j < n_p else "$"
#
#     if cur_ptn == "*":
#         if self.isCharMatch(cur_char, p[j - 1]):
#             i += 1
#             continue
#
#         if j + 1 == n_p:
#             return False
#
#         if self.isCharMatch(cur_char, p[j + 1]):
#             i += 1
#             j += 2
#             continue
#
#         return False
#
#     if not self.isCharMatch(cur_char, cur_ptn):
#         return False
#
#     i += 1
#     j += 1


# if __name__ == '__main__':
#     sol = Solution()
#     sol.isMatch("aa", ".*a")
