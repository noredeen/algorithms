class Solution:

    # Time: O(n^2) -- Space: O(n^2)
    # P(i,j) = P(i+1,j-1) AND s[i] == s[j]
    def longest_palindrome_dp(self, s: str) -> str:
        m = [[False for i in range(len(s))] for j in range(len(s))]
        max_pal = ""
        max_len = 0

        for gap in range(len(s)):
            for i in range(len(s) - gap):
                j = i + gap

                if gap == 0:
                    m[i][j] = True
                elif gap == 1:
                    m[i][j] = s[i] == s[j]
                else:
                    m[i][j] = m[i + 1][j - 1] and s[i] == s[j]

                if m[i][j] and j - i + 1 > max_len:
                    max_pal = s[i:j + 1]
                    max_len = j - i + 1

        return max_pal

    # Time: O(n^2) -- Space: O(1)
    # A palindrome mirrors around its center, so we look for such centers
    # A center can be a letter (the 'b' in 'aba') or a space between two letters as in 'aa'
    def longest_palindrome_center(self, s: str) -> str:
        res_lo = res_hi = 0
        for i in range(len(s)):
            on_letter_len = self.expand_around_center(s, i, i)
            on_space_len = self.expand_around_center(s, i, i + 1)

            print(on_letter_len, on_space_len)
            max_len = max(on_letter_len, on_space_len)
            if max_len > res_hi - res_lo:
                res_lo = i - (max_len - 1) // 2  # TODO: why?
                res_hi = i + max_len // 2  # TODO: why?

        return s[res_lo:res_hi + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        le = left
        r = right
        while le >= 0 and r < len(s) and s[le] == s[r]:
            le -= 1
            r += 1

        return r - le - 1

    # Time: O(n) -- Space: O(1)
    # This is not trivial
    def longest_palindrome_manacher(self, s: str):
        return "TODO"


x = "cbc"
Solution().longest_palindrome_center(x)
