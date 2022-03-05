class Solution:

    # We know we must remove any ')' that occurs when the balance is 0
    # We can't remove any arbitrary extra '(', gotta remove the ones without matching ')'
    def minimum(self, s: str) -> str:
        stack = []
        to_remove = set()

        for i in range(len(s)):
            if s[i] == ')' and len(stack) == 0:
                to_remove.add(i)
            elif s[i] == ')':
                stack.pop()
            elif s[i] == '(':
                stack.append(i)

        to_remove = to_remove.union(set(stack))

        res = ""
        for i in range(len(s)):
            if i not in to_remove:
                res += s[i]

        return res

    def another_aprroach(self, s: str) -> str:

        def solve(s: str, open_c: str, close_c: str) -> str:
            balance = 0
            res = ""
            for ch in s:
                if ch == close_c and balance == 0:
                    continue
                elif ch == close_c:
                    balance -= 1
                elif ch == open_c:
                    balance += 1

                res += ch

            return res

        left_corrected = solve(s, '(', ')')
        right_corrected = solve(left_corrected[::-1], ')', '(')

        return right_corrected[::-1]


print(Solution().another_aprroach("L(e)))et((co)d(e"))
