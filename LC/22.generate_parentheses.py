class Solution:

    def generate_parentheses(self, n: int) -> list[str]:
        # well-formed parentheses = wfp
        # wfp(n) = wfp(n-1)wfp(n-2)...wfp(0) -- in any order
        # wfp(n) = n '(' and n ')'
        
        # wfp(n) = '(${wfp(n-1)})'
        # wfp(n) = wfp(i)wfp(n-i) for i = 0, ..., n

        # wfp(2) = '(${wfp(1)})', 'wfp(1)wfp(1)'

        # wfp(1) = ()

        # wfp(3) = '(${wfp(2)})', 'wfp(1)wfp(2)' -> 'wfp(1)'

        wfp = [[] for i in range(n + 1)]
        wfp[0] = [""]
        for i in range(n):
            opts = wfp[n - 1].map(lambda s: f'({s})')
            for j in range(1, n):
                lefts = wfp[j]
                rights = wfp[n - j]


