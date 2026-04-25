"""
We are going to implement the breadth-first search algorithm
"""
from vertex import Vertex

class BreadthFirstSearch:
    def __init__(self):
        pass

    def __call__(self, *args, **kwds):
        pass

    def bread_first_adjacent(self, adj_list):
        initial = 0
        for v in adj_list:
            v.parent = None
            if v.initial:
                v.d = v.f = 0
                v.color = "G"
            else:
                v.d = v.f = float('inf')
                v.color = "W"
        queue = []
        queue.append(initial)
        while queue:
            index = queue.pop(0)
            u = adj_list[index]
            for child in adj_list[index].children:
                vertex = adj_list[child]
                if vertex.color == "W":
                    vertex.color = "G"
                    vertex.d = vertex.f = u.d + 1
                    vertex.parent = u
                    queue.append(child)
            u.color = "B"
        
    def multi_to_simple_graph(self, adj_list):
        simple_adj_list = []
        for v in adj_list:
            new_v = v.copy()
            new_v.children = list(set(v.children))
            simple_adj_list.append(new_v)
        return simple_adj_list


if __name__ == "__main__":
    adj_list = [
        Vertex([1, 3], initial=True), 
        Vertex([4]),
        Vertex([4, 5]), 
        Vertex([1]),
        Vertex([3]),
        Vertex([5])
    ]

    multigraph_list = [
        Vertex([1, 3, 3, 3, 1], initial=True), 
        Vertex([4, 4]),
        Vertex([4, 4, 5]), 
        Vertex([1, 1, 1, 1]),
        Vertex([3, 3, 3]),
        Vertex([5, 5, 5, 5])
    ]

    bfs = BreadthFirstSearch()
    bfs.bread_first_adjacent(adj_list)

    simple_list = bfs.multi_to_simple_graph(multigraph_list)
    print(simple_list)