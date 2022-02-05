class Solution:

    # bottom-up DP
    # I have no idea what the time/space complexities are
    def generate_parentheses_dp(self, n: int) -> list[str]:
        # wfp[n] = "(wfp[n-1])", "wfp[j]wfp[n-j]" for j = 1, ..., n-1

        def combine(a: list[str], b: list[str]) -> list[str]:
            res = []
            for x in a:
                for y in b:
                    res.append(x+y)

            return res

        wfp = [[] for i in range(n + 1)]
        wfp[0] = [""]
        for i in range(1, n+1):
            opts = [*map(lambda s: f'({s})', wfp[i-1])]
            for j in range(1, n):
                opts.extend(combine(wfp[j], wfp[i-j]))
            wfp[i] = opts

        return list(set(wfp[n]))  # TODO: this is shit

    def generate_parentheses_bt(self, n: int) -> list[str]:
        return


sol = Solution().generate_parentheses(5)
print(sol)
print(len(sol), len(set(sol)))
