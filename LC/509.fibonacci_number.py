class Solution:

    def fib_dp(self, n: int) -> int:
        if n <= 1:
            return n

        prev1 = 1
        prev2 = curr = 0
        for i in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return curr

    def fib_matrix(self, n: int) -> int:
        if n <= 1:
            return n

        matrix = [[1, 1], [1, 0]]
        self.matrix_power(matrix, n)

    # TODO: fill this in
    def matrix_power(self, matrix: list[list[int]], n: int) -> int:
        return 1

    def mult_matrix(self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        result = [
            [
                A[0][0] * B[0][0] + A[0][1] * B[1][0],
                A[0][0] * B[0][1] + A[0][1] * B[1][1],
            ],
            [
                A[1][0] * B[0][0] + A[1][1] * B[1][0],
                A[1][0] * B[0][1] + A[1][1] * B[1][1],
            ]
        ]

        return result
