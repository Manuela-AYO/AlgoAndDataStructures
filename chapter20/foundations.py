def multi_to_simple_graph(adj_list):
    simple_adj_list = []
    for v in adj_list:
        new_v = v.copy()
        new_v.children = set(v.children)
        simple_adj_list.append(new_v)