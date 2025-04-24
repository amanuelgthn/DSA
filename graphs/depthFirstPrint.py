#!/usr/bin/env python3


def depthFirstPrint(graph, source):
    stack = [ source ]

    while(len(stack)):
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)

if __name__ == "__main__":
    graph_list = {
        0 : [1, 2, 3],
        2 : [4],
        1 : [],
        3: [],
        4: [],
    }
    depthFirstPrint(graph_list, 0)