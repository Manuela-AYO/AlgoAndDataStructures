from vertex import Vertex

def init_dfs(adj_list, sort: bool=False):
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
        array.insert(0, index)
    
    if sort:
        adj_list = sorted(adj_list, key=lambda x: x.f, reverse=True)
        print(adj_list)
    for i in range(len(adj_list)):
        if adj_list[i].color == "W":
            dfs_visit(i)
    
    return array


if __name__ == "__main__":
    adj_list = [
        Vertex([1, 2]), 
        Vertex([3]),
        Vertex([]), 
        Vertex([]),
    ]

    array = init_dfs(adj_list)

    print(array)