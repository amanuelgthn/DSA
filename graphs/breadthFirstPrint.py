#!/usr/bin/env python3

def breadthFirstPrint(graph, source):
    queue = [ source ]
    while queue:
        current = queue[0]
        print(current)
        queue.remove(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
if __name__ == "__main__":
    graph_list = {
        0 : [1, 2, 3],
        2 : [4],
        1 : [],
        3: [],
        4: [],
    }
    breadthFirstPrint(graph_list, 0)