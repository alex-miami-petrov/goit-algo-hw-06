import networkx as nx
import matplotlib.pyplot as plt


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


print("\n--- Найкоротші шляхи (за часом) між усіма парами вершин ---")


all_nodes = list(G.nodes())


for start_node in all_nodes:
    for end_node in all_nodes:
        if start_node == end_node:
            continue 

        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
            
        length = nx.shortest_path_length(G, source=start_node, target=end_node, weight='weight')

        print(f"\nЗ '{start_node}' до '{end_node}':")
        print(f"  Шлях: {path}")
        print(f"  Загальний час: {length} хвилин")
        
        
print("\n--- Найкоротші шляхи від кожної вершини до всіх інших (як словник) ---")

for source_node in all_nodes:
    shortest_paths_from_source = nx.shortest_path(G, source=source_node, weight='weight')
    shortest_path_lengths_from_source = nx.shortest_path_length(G, source=source_node, weight='weight')

    print(f"\nНайкоротші шляхи та часи від '{source_node}':")
    for target_node in shortest_paths_from_source:
        if source_node != target_node:
            path = shortest_paths_from_source[target_node]
            length = shortest_path_lengths_from_source[target_node]
            print(f"  До '{target_node}': Шлях {path}, Час {length} хвилин")