import networkx as nx
import collections


G = nx.Graph()

nodes = [
    "City Center",
    "North District",
    "South District",
    "East Outskirts",
    "West Outskirts"
]
G.add_nodes_from(nodes)

edges = [
    ("City Center", "North District", {'weight': 10}),
    ("City Center", "South District", {'weight': 15}),
    ("North District", "East Outskirts", {'weight': 20}),
    ("South District", "West Outskirts", {'weight': 25}),
    ("City Center", "East Outskirts", {'weight': 30}),
    ("West Outskirts", "South District", {'weight': 12})
]
G.add_edges_from(edges)


def dfs_path(graph, start, end):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current_node, path = stack.pop()

        if current_node == end:
            return path
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None


def bfs_path(graph, start, end):
    q = collections.deque([(start, [start])])
    visited = set()
    visited.add(start)

    while q:
        current_node, path = q.popleft()

        if current_node == end:
            return path
        
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                q.append((neighbor, path + [neighbor]))


    return None


start_node = "City Center"
end_node = "West Outskirts"

print(f"Пошук шляху з '{start_node}' до '{end_node}':")


dfs_res_path = dfs_path(G, start_node, end_node)

if dfs_res_path:
    print(f"\nШлях DFS: {dfs_res_path}")
    dfs_total_weight = 0
    for i in range(len(dfs_res_path) - 1):
        u, v = dfs_res_path[i], dfs_res_path[i+1]
        dfs_total_weight += G[u][v]["weight"]
    print(f"Загальна вага шляху DFS: {dfs_total_weight} хвилин")
else:
    print(f"\nШлях DFS з '{start_node}' до '{end_node}' не знайдено.")


bfs_res_path = bfs_path(G, start_node, end_node)

if bfs_res_path:
    print(f"\nШлях BFS: {bfs_res_path}")
    bfs_total_weight = 0
    for i in range(len(bfs_res_path) - 1):
        u, v = bfs_res_path[i], bfs_res_path[i+1]
        bfs_total_weight += G[u][v]['weight']
    print(f"Загальна вага шляху BFS: {bfs_total_weight} хвилин")
else:
    print(f"\nШлях BFS з '{start_node}' до '{end_node}' не знайдено.")



