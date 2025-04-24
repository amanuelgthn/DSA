#!/usr/bin/env python3

def depthFirstPrintRecur(graph, source):
    print(source)
    for neighbor in graph[source]:
        depthFirstPrintRecur(graph,neighbor)
    

if __name__ == "__main__":
    graph_list = {
        0 : [1, 2, 3],
        2 : [4],
        1 : [],
        3: [],
        4: [],
    }
    depthFirstPrintRecur(graph_list, 0)