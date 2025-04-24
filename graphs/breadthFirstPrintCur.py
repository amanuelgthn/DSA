#!/usr/bin/env python3

def breadthFirstPrintRecur(graph, source):
    stack = [source]
    current = stack[0]
    for neighbor in graph[current]:
        print(current)
        stack.append(neighbor)
        stack.remove(current)
        breadthFirstPrintRecur(graph, neighbor)

if __name__ == "__main__":
    graph_list = {
        0 : [1, 2, 3],
        2 : [4],
        1 : [],
        3: [],
        4: [],
    }
    breadthFirstPrintRecur(graph_list, 0)
