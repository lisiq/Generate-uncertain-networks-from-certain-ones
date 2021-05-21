def uncertain_network_generator(G, p):
    new_edges = []
    for edge in list(G.edges):
        P = np.random.normal(0.8, 0.1**2, 1)
        while (p <= 0) or (p >1):
            P = np.random.normal(0.8, 0.1**2, 1)
        new_edges.append((edge[0], edge[1], {'weight' : P[0]}))
    G = nx.Graph()
    G.add_edges_from(new_edges)
    non_existential_edge_count = len(G.edges) * p
    complement_edges = list(nx.complement(G).edges)
    while non_existential_edge_count > 0:
        new_edge = random.sample(complement_edges, 1)[0]
        complement_edges.remove(new_edge)
        P = np.random.normal(0.2, 0.1**2, 1)
        while (p <= 0) or (p >1):
            P = np.random.normal(0.8, 0.1**2, 1)
        G.add_edge(new_edge[0], new_edge[1], weight=P[0])
        non_existential_edge_count = non_existential_edge_count - 1
    return G