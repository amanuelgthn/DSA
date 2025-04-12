#!/usr/bin/env python3
""""A function haspath that takes in an object representing the adjacenncy list of a directed acyclic graph and two nodes(src, dst). 
The function should return a boolean indicator whether or not there exists a directed path between the sourcce and destination node"""


def haspath(graph, src, dst):
    queue = [src]
    while len(queue) > 0:
        current = queue[0]
        if queue[0] == dst:
            return True
        queue.remove(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False

if __name__ == "__main__":
    graph = {
        'f': ['g', 'k'],
        'g' : ['h'],
        'h' : [],
        'i' : ['g', 'k'],
        'k' : []
    }

    print(haspath(graph, 'f', 'p'))

    print(haspath(graph, 'f', 'j'))
    

            