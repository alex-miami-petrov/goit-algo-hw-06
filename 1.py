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

plt.title("Транспортна мережа міста")
plt.show()


print(f"Кількість вузлів: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("\nСписок вузлів:", G.nodes())
print("\nСписок ребер з вагами:", G.edges(data=True))

