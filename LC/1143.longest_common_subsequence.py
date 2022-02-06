from functools import lru_cache


class Solution:

    def shitty_longest_common_subsequence(self, text1: str, text2: str):

        def lcs(t1: str, t2: str) -> int:
            print(t1, t2)

            if len(t1) == 1 and len(t2) == 1:
                return 1 if t1[0] == t2[0] else 0

            new_t1l = new_t1r = t1
            new_t2l = new_t2r = t2

            if len(t2) > 1:
                new_t2l = t2[:len(t2)//2]
                new_t2r = t2[len(t2)//2:]

            if len(t1) > 1:
                new_t1l = t1[:len(t1)//2]
                new_t1r = t1[len(t1)//2:]

            return max(
                lcs(new_t1l, new_t2l)+lcs(new_t1r, new_t2r),
            )

        return lcs(text1, text2)

    # O(M x N^2) time -- O(M x N) space
    def longest_common_subsequence(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def solve(p1: int, p2: int) -> int:
            if p1 == len(text1) or p2 == len(text2):
                return 0

            index = text2.find(text1[p1], p2)

            case1 = solve(p1+1, p2)

            if index > -1:
                return max(case1, 1+solve(p1+1, index+1))

            return case1

        return solve(0, 0)

    # O(M x N) time -- O(M x N) space
    # This is faster because we don't look for the first occurence
    # of text1[p1] in text2 for each recursive call. Instead, we
    # embed "looking through text2" into the recursive structure
    def longest_common_subsequence_better(self, text1: str, text2: str) -> int:

        @lru_cache(maxsize=None)
        def solve(p1: int, p2: int) -> int:
            if p1 == len(text1) or p2 == len(text2):
                return 0

            # Assuming the matching char is in the optimal solution
            # doesn't block or impact any later optimal decisions
            if text1[p1] == text2[p2]:
                return 1 + solve(p1+1, p2+1)
            else:
                return max(solve(p1, p2+1), solve(p1+1, p2))

        return solve(0, 0)

    # O(M x N) time and space
    # Bottom-up: starting from the end and crawling back to the start
    def longest_common_subsequence_dp(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]

        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]

    # O(M x N) time -- O(min(M, N)) space
    # We only need to remember the current and prev (ahead) column
    # Instead of creating a new array every col, swap prev with current! Reuse garbage!
    def longest_common_subsequence_dp_best(self, text1: str, text2: str) -> int:

        col_ahead = [0] * (len(text1) + 1)
        col_curr = [0] * (len(text1) + 1)
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    col_curr[row] = 1 + col_ahead[row+1]
                else:
                    col_curr[row] = max(col_curr[row+1], col_ahead[row])

            col_ahead, col_curr = col_curr, col_ahead  # nice

        return col_ahead[0]


print(Solution().longest_common_subsequence_dp_best("oxcpqrsvwf", "shmtulqrypy"))
