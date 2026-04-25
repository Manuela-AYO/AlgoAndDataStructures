from vertex import Vertex
import heapq

class Graph:
    def __init__(self):
        pass

    def __transpose_adj_list(self, graph):
        adj_list_transpose = [ vertex.copy() for vertex in graph ]

        for i in range(len(graph)):
            adj_list_transpose[i].children = []
            adj_list_transpose[i].color = "W"

        for i in range(len(graph)):
            children = graph[i].children
            for child in children:
                adj_list_transpose[child].children.append(i)
        return adj_list_transpose

    def transpose(self, graph):
        if isinstance(graph, list):
            return self.__transpose_adj_list(graph)
        

    def init_dfs(self, adj_list, sort: bool=False):
        """
        Compute dfs and make a topological sort
        """
        time = 0
        array = []

        def dfs_visit(index):
            nonlocal time
            nonlocal array
            time += 1
            v = adj_list[index]
            v.d = time
            v.color = "G"
            for child in v.children:
                if adj_list[child].color == "W":
                    dfs_visit(child)
            time += 1
            v.f = time
            v.color = "B"
            if sort:
                array[-1].append(index)
            else:
                array.insert(0, index)
        
        if sort:
            indices = sorted(range(len(adj_list)),
                             key = lambda i: adj_list[i].f,
                             reverse=True)
        else:
            indices = range(len(adj_list))

        for index in indices:
            if adj_list[index].color == "W":
                if sort:
                    array.append([])
                dfs_visit(index)
    
        return array


        
    def compute_scc(self, graph):
        """
        Compute the strongly connected components of a graph
        """
        # perform dfs
        self.init_dfs(graph)

        # create the transpose of the graph
        graph_T = self.transpose(graph)

        # perform the dfs 
        sccs = self.init_dfs(graph_T, sort=True)
        return sccs
    

    def __get_weighted_edges(self, graph):
        edges = []
        if isinstance(graph, list):
            for i in range(len(graph)):
                for child in graph[i].children:
                    pair = [i, child[0], child[1]]
                    edges.append(pair)
        return edges

    
    def __find(self, parent: list, u):
        if parent[u] != u:
            parent[u] = self.__find(parent, parent[u])
        return parent[u]
    

    def __union(self, parent, rank, u, v):
        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u
            rank[u] += 1


    def __minHeapify(self, A, i: int):
        left = i-1
        right = i+1
        if left < len(A) and A[left].key < A[i].key:
            smallest = left
        else:
            smallest = i
        if right < len(A) and A[right].key < A[smallest].key:
            smallest = right
        if smallest != i:
            temp = A[i]
            A[i] = A[smallest]
            A[smallest] = temp
            self.__minHeapify(A, smallest)


    def mst_prim(self, graph, start_node):
        """
        Returns the minimum spanning tree of the graph using Prim's algorithm
        """
        visited = set()
        min_heap = [(0, start_node)]
        total_cost = 0
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += weight
            for v, w in graph[u].children:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))
                    mst_edges.append((u, v, w))
        return mst_edges
        

    def mst_kruskal(self, graph):
        """
        Returns the minimum spanning tree of the graph using Kruskal algorithm
        """
        # create the list of weights [(ai, bi, weighti)]
        edges = self.__get_weighted_edges(graph)

        # sort the edges by decreasing weights
        edges = sorted(edges, key=lambda x: x[2])
        
        # create the set of vertices and ranks to define representatives
        parent = []
        rank = []

        for node in range(len(graph)):
            parent.append(node)
            rank.append(0)

        # our condition is based on the fact that the number of edges of a 
        # tree is the number of vertices - 1
        e = 0
        i = 0
        result = []

        while e < len(graph) - 1:
            # pick the smallest edge and
            u, v, w = edges[i]
            i = i+1

            # get the representatives
            x = self.__find(parent, u)
            y = self.__find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.__union(parent, rank, x, y)

        minimumCost = 0
        for u, v, w in result:
            minimumCost += w

        print(f"Minimum spanning tree cost: {minimumCost}")