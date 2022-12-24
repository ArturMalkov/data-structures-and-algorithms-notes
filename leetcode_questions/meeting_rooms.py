"""
252 leetcode problem
"""


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# sort meetings based on start time - O(nlog(n))
def can_attend_meetings(intervals: list[Interval]) -> bool:
    intervals.sort(key=lambda x: x.start)

    for i in range(1, len(intervals)):
        i1 = intervals[i-1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False

    return True
