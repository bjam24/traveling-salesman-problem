from numpy import ndarray
from networkx import DiGraph, draw
from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def draw_path(distances: ndarray, results: tuple, algorithm_name: str) -> None:
    optimal_path, optimal_distance = results
    mds = MDS(n_components = 2, dissimilarity = 'precomputed', random_state = 42)
    coords = mds.fit_transform(distances)
    G = DiGraph()

    for i in range(len(optimal_path) - 1):
        u = optimal_path[i]
        v = optimal_path[i + 1]
        weight = distances[u, v]
        G.add_edge(u, v, weight = weight)

    plt.figure(figsize = (10, 6))
    plt.title(f'TSP Best Route using {algorithm_name} Algorithm')
    
    pos = {i: (coords[i, 0], coords[i, 1]) for i in range(len(distances))}
    draw(G, 
         pos, 
         with_labels = True, 
         node_color = 'red', 
         node_size = 150, 
         font_size = 8, 
         edge_color = 'blue')
    
    plt.figtext(0.5, 0.05, f'Optimal Distance: {optimal_distance}', ha = 'center', va = 'center', fontsize = 12, color = 'black')
    plt.show()