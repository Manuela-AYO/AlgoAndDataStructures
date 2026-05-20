from vertex import Vertex
import heapq
from typing import Any
import numpy as np

class Graph:
    """
    This module performs all the operations on the graph as 
    described in the chapter 'Graph' of 'Introduction to algorithms' by
    CLRS.
    The graph is either an adjacency list; in this case, the list of children
    is made of tuples of index node and weight of the edge.
    Or an adjacency matrix where matrix[i,j] = weight if there is an edge
    between i and j and 0 otherwise
    Quick facts about adjacency list vs matrix:
    - the list representation is better for sparse graphs(|E| < |V|^2)
    - the matrix representation is better for dense graphs or when we 
    want to quickly access the neighbor
    """
    def __init__(self, graph: list[list[Any]]):
        self.parents = []
        self.distances = []
        self.graph = graph
        self.is_list_adj = self.is_adj_list()


    def get_predecessor_tree(self):
        return self.parents
    

    def get_path_length(self):
        return self.distances
    

    def is_adj_list(self) -> bool:
        """
        Check if the representation of a graph is an
        adjacency list or a matrix
        Params:
        Returns:
            A boolean
        """
        assert isinstance(self.graph, list) and isinstance(self.graph[0], list), \
            "The representation of the graph should be either an adjacency list or a matrix"
        if isinstance(self.graph[0][0], tuple):
            return True
        return False
        

    def __transpose_adj_list(self, graph: list[list[tuple]]) -> list[list[tuple]]:
        """
        Transpose the adjacency list representation of the graph
        Params:
            graph: the adjacency list representation of the graph
        Returns:
            The transposed adjacency list
        """
        adj_list_transpose = [ [] for _ in graph ]
        for i in range(len(graph)):
            children = graph[i]
            for child in children:
                node = child[0]
                w = child[1]
                adj_list_transpose[node].append((i, w))
        return adj_list_transpose
    

    def __transpose_adj_matrix(self, graph: list[list[int]]) -> list[list[int]]:
        """
        Transpose the adjacency matrix representation of the graph
        Params:
            graph: the adjacency matrix representation of the graph
        Returns:
            The transposed matrix
        """
        mat_transpose = [ [0] * len(graph) for _ in range(len(graph)) ]
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] > 0:
                    mat_transpose[j][i] = graph[i][j]
        return mat_transpose


    def transpose(self, graph):
        try:
            if self.is_adj_list(graph):
                return self.__transpose_adj_list(graph)
            return self.__transpose_adj_matrix(graph)
        except AssertionError as e:
            print(e)
        
        
    def dfs_visit_list(self, nodes_order: list|None=None, type:str='pur') -> list[int]:
        """
        Perform a DFS visit on an adjacent list
        Params:
            adj_list: an adjacency list representation of the graph
        Returns:
            The DFS traversal of the graph
        """
        assert isinstance(self.graph, list)
        visited = [False] * len(self.graph)
        result = []

        def dfs_visit(index):
            """
            Helper function to perform the dfs search
            """
            visited[index] = True
            for node in self.graph[index]:
                index_node = node[0]
                if not visited[index_node]:
                    dfs_visit(index_node)
            if type == 'pur':
                result.append(index)
            else:
                result[-1].append(index)

        if not nodes_order:
            nodes_order = list(range(len(self.graph)))

        for node in nodes_order:
            if not visited[node]:
                if type == 'scc':
                    result.append([])
                dfs_visit(node)
        return result
    

    def dfs_visit_matrix(self, nodes_order: list|None=None, type:str = 'pur') -> list[int]:
        """
        Performs the DFS traversal on adjacency matrix
        Params:
            adj_matrix: the adjacency matrix representation of a graph
        Returns:
            the DFS traversal list of that matrix
        """
        visited = [False] * len(self.graph)
        result = []

        def dfs_visit(index):
            """
            Helper function to perform DFS traversal
            """
            visited[index] = True
            for i in range(len(self.graph)):
                if not visited[i] and self.graph[index][i] > 0:
                    dfs_visit(i)
            if type == 'pur':
                result.append(index)
            else:
                result[-1].append(index)
        
        if not nodes_order:
            nodes_order = list(range(len(self.graph)))

        for node in nodes_order:
            if not visited[node]:
                if type == 'scc':
                    result.append([])
                dfs_visit(node)

        return result
    

    def perform_dfs(self, nodes_order:list|None = None, type:str='pur') -> list[int]:
        try:
            if self.is_adj_list():
                return self.dfs_visit_list(nodes_order, type)
            return self.dfs_visit_matrix(nodes_order, type)
        except AssertionError as e:
            print(e)

        
    def dfs_visit_list_rec(self, i: int, colors:list[int]) -> bool:
        """
        Recursively perform dfs in an adjacent list to know if a 
        directed graph is acyclic
        Params:
            i: the index of the vertex to visit
            colors: the list of colors defining the state of the node in the traversal
        Returns:
            bool: if a child points back to its parent, there is a cycle and this is known
            if a node has as child a node in grey
        """
        colors[i] = 1
        for node in self.graph[i]:
            j = node[0]
            if not colors[j]:
                self.dfs_visit_list_rec(j, colors)
            elif colors[j] == 1:
                return True
        colors[i] = 2
        return False
    

    def dfs_visit_matrix_rec(self, i: int, colors: list[int]) -> bool:
        """
        Recursively perform dfs in an adjacent matrix to know if a 
        directed graph is acyclic
        Params:
            i: the index of the vertex to visit
            colors: the list of colors defining the state of the node in the traversal
        Returns:
            bool: if a child points back to its parent, there is a cycle and this is known
            if a node has as child a node in gray
        """
        colors[i] = 1
        for j in range(len(self.graph)):
            if self.graph[i][j] > 0:
                if not colors[j]:
                    self.dfs_visit_matrix_rec(j, colors)
                elif colors[j] == 1:
                    return True
        colors[i] = 2
        return False
    
    def is_dag(self) -> bool:
        """
        Check if a directed graph is acyclic.
        We do it using the DFS algorithm
        Params:
        Returns:
            boolean - telling whether or not a directed graph is acyclic
        """
        colors = [0] * len(self.graph) # 0 -> White 1 -> Grey 2 -> Black
        for i in range(len(self.graph)):
            if not colors[i]:
                if self.is_list_adj:
                    is_backward_edge = self.dfs_visit_list_rec(i, colors)
                else:
                    is_backward_edge = self.dfs_visit_matrix_rec(i, colors)
                if is_backward_edge:
                    return False
        return True
        
    
    def compute_scc(self, graph):
        """
        Compute the strongly connected components of a graph
        """
        # perform dfs
        result = self.perform_dfs(graph)
        result.reverse()

        # create the transpose of the graph
        graph_T = self.transpose(graph)

        # perform the dfs 
        sccs = self.perform_dfs(graph_T, result, 'scc')
        return sccs
    

    def __get_weighted_edges(self):
        try:
            edges = []
            if self.is_adj_list(self.graph):
                for i in range(len(self.graph)):
                    for child in self.graph[i]:
                        pair = [i, child[0], child[1]]
                        edges.append(pair)
            else:
                for i in range(len(self.graph)):
                    for idx in range(len(self.graph)):
                        if self.graph[i][idx] > 0:
                            pair = [i, idx, self.graph[i][idx]]
                            edges.append(pair)
            return edges
        except AssertionError as e:
            print(e)

    
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


    def mst_prim(self, start_node):
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
            mst_edges.append(u)
            total_cost += weight
            if self.is_adj_list(self.graph):
                for v, w in self.graph[u]:
                    if v not in visited:
                        heapq.heappush(min_heap, (w, v))
            else:
                for j in range(len(self.graph)):
                    if self.graph[u][j] > 0 and j not in visited:
                        v = j
                        w = self.graph[u][j]
                        heapq.heappush(min_heap, (w, v))
        return mst_edges, total_cost
        

    def mst_kruskal(self):
        """
        Returns the minimum spanning tree of the graph using Kruskal algorithm
        """
        # create the list of weights [(ai, bi, weighti)]
        edges = self.__get_weighted_edges()

        # sort the edges by decreasing weights
        edges = sorted(edges, key=lambda x: x[2])
        
        # create the set of vertices and ranks to define representatives
        parent = []
        rank = []

        for node in range(len(self.graph)):
            parent.append(node)
            rank.append(0)

        # our condition is based on the fact that the number of edges of a 
        # tree is the number of vertices - 1
        e = 0
        i = 0
        result = []

        while e < len(self.graph) - 1:
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

        return result, minimumCost

    
    def __relax(self, edge) -> bool:
        assert len(self.distances) > 0 and len(self.parents) > 0, \
            "The graph's parents and distances list have to be initialized"
        u = edge[0]
        v = edge[1]
        w = edge[-1]
        changed = False
        if self.distances[v] > self. distances[u] + w:
            self.distances[v] = self.distances[u] + w
            self.parents[v] = u
            changed = True
        return changed

    
    def bellman_ford(self, source):
        """
        Given a graph, check if there is a shortest path. 
        If not, returns False. Otherwise returns True and build the
        tree of predecessors
        """
        # create the list of weighted edges
        # initialize the single source
        for _ in range(len(self.graph)):
            self.parents.append(None)
            self.distances.append(float('inf'))
        self.distances[source] = 0

        edges = self.__get_weighted_edges()
        changed = False
        for i in range(len(self.parents) - 1):
            for edge in edges:
                changed = self.__relax(edge) or changed
            # this small check is to stop the current loop as soon
            # as the distances at step t-1 == distances at step t
            if not changed:
                break

        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[-1]
            if self.distances[v] > self.distances[u] + w:
                return False
        return True
    

    def __get_children(self, u: int) -> list[tuple[int, Any]]:
        if self.is_list_adj:
            children = self.graph[u]
        else:
            children = []
            for v in range(len(self.graph)):
                w = self.graph[u][v]
                if w > 0:
                    children.append((v, w))
        return children
    
    def dijkstra(self, source: int) -> None:
        """
        Dijkstra algorithm used to find the shortest path from a single source
        Params:
            source: the source node
        Returns:
            None: the algorithm computes the shortest distances and the parents in place
        """
        queue = []
        self.distances = [float('inf')] * len(self.graph)
        self.parents = [None] * len(self.graph)
        self.distances[source] = 0
        heapq.heappush(queue, (0, source))
        while queue:
           d, u = heapq.heappop(queue) 
           if d > self.distances[u]:
               continue
           
           children = self.__get_children(u)
           for v, w in children:
                if self.distances[v] > self.distances[u] + w:
                   self.parents[v] = u
                   self.distances[v] = self.distances[u] + w
                   heapq.heappush(queue, (self.distances[v], v))


    def dag_adj_list(self, nodes_traversal: list[int]) -> None:
        """
        Compute the shortest path values in an adjacent list using 
        topological sort through nodes_traversal
        Params:
            nodes_traversal: list[int] order of nodes to proceed in the relaxation
        Returns:
            None
        """
        for u in nodes_traversal:
            for node in self.graph[u]:
                v = node[0]
                w = node[1]
                self.__relax((u, v, w))

    
    def dag_adj_matrix(self, nodes_traversal: list[int]) -> None:
        """
        Compute the shortest path values in an adjacent matrix using 
        topological sort through nodes_traversal
        Params:
            nodes_traversal: list[int] order of nodes to proceed in the relaxation
        Returns:
            None
        """
        for u in nodes_traversal:
            for v in range(len(self.graph)):
                if self.graph[u][v] > 0:
                    w = self.graph[u][v]
                    self.__relax((u, v, w))
    
    
    def dag_shortest_path(self, source: int):
        """
        Compute the shortest path values in a graph
        Params:
            source: int the source node
        Returns:
            list[int], list[float] respectively the lists of parents and distances
        """
        assert self.is_dag(), "The graph should be a directed acyclic graph"

        dfs_traversal = self.perform_dfs()
        dfs_traversal.reverse()
        for _ in range(len(self.graph)):
            self.parents.append(None)
            self.distances.append(float('inf'))
        self.distances[source] = 0

        if self.is_list_adj:
            self.dag_adj_list(dfs_traversal)
        else:
            self.dag_adj_matrix(dfs_traversal)
        return self.parents, self.distances


    def count_nb_paths_dag(self):
        """
        Count the number of paths in a DAG
        This time, I consider we deal with an adjacency list
        Complexity: Theta(V+E)
        """
        assert self.is_dag(), "The graph should be a DAG"
        assert self.is_list_adj, "Please provide an adjacent list representation"

        nb_paths = [1] * len(self.graph)
        vertices = self.perform_dfs()
        for u in vertices:
            for node in self.graph[u]:
                v = node[0]
                nb_paths[u] += nb_paths[v]
        return sum(nb_paths)