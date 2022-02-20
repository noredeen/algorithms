class Solution:

    # Time: O(# of chars in all strs) -- Space: O(1)
    # vertical scan
    def longest_common_prefix(self, strs: list[str]) -> str:
        min_len = min(map(lambda s: len(s), strs))
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return strs[j][:i]

        return strs[0][:min_len - 1]

    # TODO: for practice, implement binary search
    # O(mlogn) space: logn recursive calls and each stores m
    def d_n_c(self, strs: list[str]) -> str:

        def lcp(l: int, r: int) -> str:
            if l == r:
                return strs[l]

            mid = (l + r) // 2
            left = lcp(l, mid)
            right = lcp(mid+1, r)
            return common_prefix(left, right)

        def common_prefix(str1: str, str2: str) -> str:
            for i in range(min(len(str1), len(str2))):
                if str1[i] != str2[i]:
                    return str1[:i]

            return str1[:min(len(str1), len(str2))]

        return lcp(0, len(strs)-1)


print(Solution().d_n_c(["hello", "he", "hes"]))
