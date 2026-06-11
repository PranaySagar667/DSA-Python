# ─────────────────────────────────────────────
# 3. Merge Intervals (LeetCode #56)
# Given a list of intervals, merge all overlapping ones.
#
# Approach: Sort by start time; greedily merge if current start
#           <= last merged end
# Time : O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:                      # overlap — extend
            merged[-1][1] = max(last_end, end)
        else:                                       # no overlap — new interval
            merged.append([start, end])

    return merged


# ---- Test ----
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))   # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]]))                  # [[1,5]]
