# ─────────────────────────────────────────────
# 5. Meeting Rooms II — Minimum Meeting Rooms (LeetCode #253)
# Given meeting time intervals, find minimum number of rooms required.
#
# Approach: Sort start & end times separately; use two pointers
#           If next meeting starts before previous ends → need new room
# Time : O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────
def min_meeting_rooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends   = sorted(i[1] for i in intervals)

    rooms = 0
    max_rooms = 0
    j = 0   # pointer for ends

    for i in range(len(starts)):
        if starts[i] < ends[j]:
            rooms += 1          # new room needed
        else:
            j += 1              # a meeting ended, room freed

        max_rooms = max(max_rooms, rooms)

    return max_rooms


# ---- Test ----
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))   # 2
print(min_meeting_rooms([[7, 10], [2, 4]]))               # 1