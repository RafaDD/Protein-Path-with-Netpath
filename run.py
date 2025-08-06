from protein_path import protein_path
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    finder = protein_path()
    paths = finder.find_shortest()
    print(f'Path:')
    if len(paths) == 0:
        print('None')
        exit()
    else:
        for path in paths:
            for i in range(len(path) - 1):
                print(f'{path[i]} -> ', end='')
            print(path[-1])

    nlist = [[] for _ in range(len(paths[0]))]
    G = nx.DiGraph()
    for path in paths:
        for i in range(len(path) - 1):
            G.add_edge(path[i], path[i+1])
            nlist[i].append(path[i])
            nlist[i+1].append(path[i+1])
    for i in range(len(nlist)):
        nlist[i] = list(dict.fromkeys(nlist[i]))

    max_num = -1

    pos_x = np.linspace(-1, 1, len(nlist)+2)
    pos = {}
    for i in range(len(nlist)):
        max_num = max(max_num, len(nlist[i]))
        pos_y = np.linspace(-1, 1, len(nlist[i])+2)
        for j in range(len(nlist[i])):
            pos[nlist[i][j]] = np.array([pos_x[i+1], pos_y[j+1]])

    node_size = min(5000, 30000 / max_num)
    font_size = int(node_size / 250)
    plt.figure(figsize=(20, 10))
    nx.draw(G, pos, with_labels=True, arrows=True, node_color='skyblue', node_size=node_size, font_size=font_size)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='wedge', arrowsize=10)
    plt.savefig(f'imgs/{nlist[0][0]}->{nlist[-1][0]}.png', dpi=200)