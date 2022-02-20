class Solution:

    # bottom-up DP
    # O(catalan numbers)
    def generate_parentheses_dp(self, n: int) -> list[str]:
        # wfp[n] = "(wfp[n-1])", "wfp[j]wfp[n-j]" for j = 1, ..., n-1

        wfp = [[] for _ in range(n + 1)]
        wfp[0] = [""]
        for i in range(1, n+1):
            opts = []
            for j in range(0, i):
                left = wfp[j]
                right = wfp[i-j-1]
                for le in left:
                    for ri in right:
                        opts.append(f'({le}){ri}')

            wfp[i] = opts

        return wfp[n]

    # TODO: Catalan numbers???
    # keep adding left and right parens as long as the string stays well-formed
    def generate_parentheses_v2(self, n: int) -> list[str]:
        def iter(s: str, left: int, right: int):
            if left + right == 2*n:
                res.append(s)
                return

            if left < n:
                iter(s+'(', left+1, right)

            if right < left:
                iter(s+')', left, right+1)

        res = []
        iter("", 0, 0)
        return res


sol = Solution().generate_parentheses_dp(5)
print(sol)
print(len(sol), len(set(sol)))
