class Solution:

    # O(nlogn) time -- O(1) space
    def can_attend_meetings(self, intervals: list[list[int]]):
        intervals.sort(key=lambda v: v[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False

        return True
