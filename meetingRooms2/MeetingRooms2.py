#!/usr/bin/env python3

from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> int:
    meetings = []
    for i in intervals:
        meetings.append((i[0], 1))
        meetings.append((i[1], 0))
    meetings.sort()
    ans = 0
    count = 0
    for meeting in meetings:
        if meeting[1] == 1:
            count += 1
        else:
            count -= 1
        ans = max(ans, count)
    return ans

if __name__ == "__main__":
    interval1 = [[0,30],[5,10],[15,20]]
    interval2 = [[7,10],[2,4]]
    print("it worked")
    print("{}\n Answer: {}".format(interval1, minMeetingRooms(interval1)))
    print("{}\n Answer: {}".format(interval2, minMeetingRooms(interval2)))
    