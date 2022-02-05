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

    # TODO: for practice, implement divide-and-conquer AND binary search


Solution().longest_common_prefix(["hello", "he", "hes"])
