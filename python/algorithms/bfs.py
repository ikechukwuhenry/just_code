"""implementation of the breadth first search algorithm
https://www.youtube.com/watch?v=s-CYnVz-uh4
https://en.wikipedia.org/wiki/Breadth-first_search
"""
from data_structures import graph
from data_structures import queue

def retrieve_path(parents: dict, end):
    """returns the path from start to the given end
    """
    path = [end]
    current_node = end
    while parents[current_node] != None:
        path.append(parents[current_node])
        current_node = parents[current_node]
    path.reverse()
    return path

def bfs(graph: graph.Graph, start, end) -> list:
    """returns when the first path is found from the start node to the end node
    """
    # special case: start = end
    if start == end: return start
    # set-up
    level = {start: 0}
    parents = {start: None}
    n = 1
    front = [start]  # this is the current frontier being explored
    while front:
        _next = []  # will be the next frontier
        for current_node in front:  # iterate over the nodes in the current frontier
            for neighbor in graph.neighbors(current_node):  # build the next frontier
                # no revisiting
                if neighbor not in level:
                    level[neighbor] = n
                    parents[neighbor] = current_node
                    # match
                    if neighbor == end: return retrieve_path(parents, end)
                    _next.append(neighbor)
        front = _next
        n += 1
    raise ValueError(f'node: {end} not reachable from node: {start}')
# test
g = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
g = graph.Graph(g)
