class Solution:

    def generate(self, num_rows: int) -> list[list[int]]:
        ans = [[]] * num_rows
        ans[0] = [1]
        for i in range(1, num_rows):
            row = [0] * (i + 1)
            row[0] = 1
            for j in range(1, len(ans[i - 1]) - 1):
                row[j] = ans[i - 1][j] + ans[i - 1][j - 1]
            row[i] = 1
            ans[i] = row

        return ans


Solution().generate(5)
