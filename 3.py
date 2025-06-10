import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start_node, weight_attribute='weight'):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph.nodes()}
    priority_queue = [(0, start_node)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        
        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor].get(weight_attribute, 1)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes


def reconstruct_path(previous_nodes, start_node, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    
    if path[0] == start_node:
        return path
    else:
        return [] # No path found


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


plt.figure(figsize=(10, 7))
pos = {
    "City Center": (0, 0),
    "North District": (0, 1),
    "South District": (0, -1),
    "East Outskirts": (1, 1),
    "West Outskirts": (-1, -1)
}
nx.draw_networkx_nodes(G, pos, node_size=3000, node_color="skyblue", alpha=0.9)
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", alpha=0.7)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Транспортна мережа міста зі зваженими ребрами")
plt.show()


print("\n--- Найкоротші шляхи (за часом) між усіма парами вершин (ВЛАСНА РЕАЛІЗАЦІЯ АЛГОРИТМУ ДЕЙКСТРИ) ---")


all_nodes = list(G.nodes())


for start_node in all_nodes:
    for end_node in all_nodes:
        if start_node == end_node:
            continue 

        distances, previous_nodes = dijkstra(G, start_node, weight_attribute='weight')
        
        path = reconstruct_path(previous_nodes, start_node, end_node)
        length = distances[end_node]

        print(f"\nЗ '{start_node}' до '{end_node}':")
        print(f"  Шлях: {path}")
        print(f"  Загальний час: {length} хвилин")
        
        
print("\n--- Найкоротші шляхи від кожної вершини до всіх інших (як словник) (ВЛАСНА РЕАЛІЗАЦІЯ АЛГОРИТМУ ДЕЙКСТРИ) ---")

for source_node in all_nodes:
    distances, previous_nodes = dijkstra(G, source_node, weight_attribute='weight')

    print(f"\nНайкоротші шляхи та часи від '{source_node}':")
    for target_node in all_nodes:
        if source_node != target_node:
            path = reconstruct_path(previous_nodes, source_node, target_node)
            length = distances[target_node]
            print(f"  До '{target_node}': Шлях {path}, Час {length} хвилин")