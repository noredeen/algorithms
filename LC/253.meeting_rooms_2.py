import heapq


class Solution:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        # very nice problem
        # [0, 30], [25, 40], [27, 60]
        # [0, 30], [25, 40], [35, 60]
        # [0, 500], [25, 40], [45, 60]
        # [1, 5], [8, 9], [8, 9]
        # [4,19], [6,13], [11,20], [13,17]

        def does_overlap(int1: list[int], int2: list[int]) -> bool:
            return int1[1] > int2[0]

        end_times_min_heap = sorted(
            map(lambda intrv: intrv[1], intervals))
        heapq.heapify(end_times_min_heap)

        intervals.sort(key=lambda intrv: intrv[0])

        rooms_needed = 1
        for i in range(len(intervals)-1):
            if does_overlap(intervals[i], intervals[i+1]):
                min_end_time = heapq.heappop(end_times_min_heap)

                if min_end_time <= intervals[i+1][0]:
                    continue

                heapq.heappush(end_times_min_heap, min_end_time)
                rooms_needed += 1

            else:
                heapq.heappop(end_times_min_heap)

        return rooms_needed


print(Solution().min_meeting_rooms([[0, 30], [25, 40], [27, 60]]))  # -> 3
print(Solution().min_meeting_rooms([[0, 30], [25, 40], [35, 60]]))  # -> 2
print(Solution().min_meeting_rooms([[0, 500], [25, 40], [45, 60]]))  # -> 2
print(Solution().min_meeting_rooms([[7, 10], [2, 4]]))  # -> 1
