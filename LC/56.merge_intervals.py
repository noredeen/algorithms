class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interv: interv[0])  # merge sort -- O(nlogn)
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    # Follow-up: how do we do this with a large stream of intervals?
    # i.e we don't have all of them at a time so we can't sort

    def merge_stream(self, intervals: list[list[int]]) -> list[list[int]]:
        return


print(Solution().merge([[1, 3], [8, 10], [2, 6], [15, 18]]))
