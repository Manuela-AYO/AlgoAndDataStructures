from graph import Graph
from dfs import init_dfs
from vertex import Vertex

if __name__ == "__main__":
    adj_list = [
        Vertex([1]),
        Vertex([2, 4, 5]),
        Vertex([3, 6]),
        Vertex([2, 7]),
        Vertex([0, 5]),
        Vertex([6]),
        Vertex([5, 7]),
        Vertex([7])
    ]

    graph = Graph()
    sccs = graph.compute_scc(adj_list)

    adj_list = [
        Vertex([(1, 1)]),
        Vertex([2, 4, 5]),
        Vertex([3, 6]),
        Vertex([2, 7]),
        Vertex([0, 5]),
        Vertex([6]),
        Vertex([5, 7]),
        Vertex([7])
    ]
    print(sccs)