"""implementation of the dinic's algorithm
computes the max flow possible within a given network gaph

https://visualgo.net/en/maxflow
https://en.wikipedia.org/wiki/Dinic%27s_algorithm
"""
from data_structures import network_graph

def dinic(graph: network_graph.NGraph) -> int:
    """computes the maximum flow value of the network
    """
    # set-up
    residual_network = network_graph.NGraph(graph.inner, graph.source, graph.sink)
    dinic.max_flow = 0
    dinic.parents = {}
    # retrieve bottle neck function
    def blocking_flow(node, minimum=float('inf')):
        """returns the value of the bottleneck once the sink is been reached
        """
        if not node: return minimum
        minimum = min(minimum, residual_network.capacity(dinic.parents[node], node))
        # recursively find minimum to return
        minimum = blocking_flow(dinic.parents[node], minimum)
        # update residual graph
        residual_network.capacities[dinic.parents[node], node] -= minimum
        return minimum
    # standard bfs
    def bfs(start, end):
        """standard bfs, with implicit queue
        modified to stop once the sink is been reached and increase the max flow
        """
        dinic.parents = {graph.source:None}
        frontier = [graph.source]
        while frontier:
            _next = []
            for current_node in frontier:
                for node in graph.neighbors(current_node):
                    if node not in dinic.parents\
                        and residual_network.capacity(current_node, node)>0:
                        dinic.parents[node] = current_node
                        # sink within reach, increase max-flow
                        if node == graph.sink:
                            dinic.max_flow += blocking_flow(graph.sink)
                            return True
                        _next.append(node)
            frontier = _next
    # repeat until there are no more augmenting paths... s -> t
    while(bfs(graph.source, graph.sink)): pass
    return dinic.max_flow


# test
graph = {0: [(1,5), (2,8), (3,3), (4,3), (5,7), (9,7)],
        1: [(9,4)],
        2: [(9,9)],
        3: [(6,1)],
        4: [(7,4)],
        5: [(8,6)],
        6: [(9,1)],
        7: [(9,6)],
        8: [(9,5)],
        }
graph = network_graph.NGraph(graph, 0, 9)
# ford flukerson killer...
graph = {0: [(2,8), (1,8)],
        1: [(3,8)],
        2: [(3,8), (1,1)],
        }
graph = network_graph.NGraph(graph, 0, 3)
# final case...
graph = {0: [(2,5), (3,3)],
        1: [(4,4)],
        2: [(4,3), (1,3), (3,3)],
        3: [(1,5)],
        }
graph = network_graph.NGraph(graph, 0, 4)
