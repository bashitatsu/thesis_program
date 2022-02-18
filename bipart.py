from networkx.algorithms import bipartite
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.layout import bipartite_layout


B = nx.Graph()
B.add_nodes_from(["O_ORF1ab", "O_ORF1a", "O_surface glycoprotein", "O_ORF3a","O_envelope protein","O_membrane glycoprotein", "O_ORF6", "O_ORF7a", "O_ORF7b", "O_ORF8", "O_nucleocapsid phosphoprotein","O_ORF10"], bipartite=0)
B.add_nodes_from(["O_ORF1ab", "O_ORF1a", "O_surface glycoprotein", "O_ORF3a","O_envelope protein","O_membrane glycoprotein", "O_ORF6", "O_ORF7a", "O_ORF7b", "O_ORF8", "O_nucleocapsid phosphoprotein","O_ORF10"], bipartite=1)
B.add_edges_from([(1, "a"), (1, "b"), (2, "b"), (2, "c"), (3, "c"), (4, "a")])

# pos = bipartite_layout(B, top_nodes)

# nx.draw(B, pos=pos, node_color='lightgreen')
# nx.draw_networkx_labels(B, pos=pos)
# plt.show()

G = nx.DiGraph()

# 重み付きのファイルの読み込み
G = nx.read_weighted_edgelist('distance_data.txt', delimiter=",",nodetype=str)
# bottom_nodes, top_nodes = bipartite.sets(G.nodes())
# レイアウトと頂点の色を適当に設定
pos = nx.spring_layout(G)
edge_labels = {(i, j): w['weight'] for i, j, w in G.edges(data=True)}
nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
nx.draw_networkx(G, pos, with_labels=True, alpha=0.5)
# グラフの描画
# nx.draw_networkx_edge_labels(G,pos)
# nx.draw_networkx(G, pos, with_labels=True,alpha=0.5)

# 表示
plt.axis("off")
plt.show()