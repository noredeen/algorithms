from collections import defaultdict


class Solution:

    def original_digits(self, s: str) -> str:

        counts = defaultdict(int)
        for c in s:
            counts[c] += 1

        res_counts = [0] * 10

        res_counts[0] = counts["z"]
        res_counts[2] = counts["w"]
        res_counts[4] = counts["u"]
        res_counts[6] = counts["x"]
        res_counts[8] = counts["g"]

        res_counts[3] = counts["h"] - res_counts[8]
        res_counts[5] = counts["f"] - res_counts[4]
        res_counts[7] = counts["s"] - res_counts[6]

        res_counts[9] = counts["i"]-res_counts[5]-res_counts[6]-res_counts[8]
        res_counts[1] = counts["n"] - res_counts[7] - 2*res_counts[9]

        res = ""
        for i in range(10):
            res += str(i) * res_counts[i]

        return res


print(Solution().original_digits("owoztneoer"))
