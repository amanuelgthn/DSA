#!/usr/bin/env python3
from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:
    graph = {}
    for lst in trust:
        if lst[0] not in graph:
            graph[lst[0]] = [lst[1]]
        else:
            graph[lst[0]].append(lst[1])

if __name__ == "__main__":
    lst = [[1,3],[2,3],[3,1], [2,1]]
    findJudge(3, lst)