class Solution:

    def climb_stairs_bottom_up(self, n: int) -> int:
        m = [0] * (n + 1)
        m[0] = 1
        m[1] = 1
        for i in range(2, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        return m[n]

    # mem = [-1] * (n+1)
    # mem[0] = 1
    def climb_stairs_top_down(self, n: int, mem: [int]) -> int:
        if n < 0:
            return 0
        if mem[n] > -1:
            return mem[n]

        mem[n] = self.climb_stairs_top_down(n - 1, mem) + self.climb_stairs_top_down(n - 2, mem)
        return mem[n]
