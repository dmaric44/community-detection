import matplotlib.pyplot as plt
import networkx as nx
import snap

if __name__ == '__main__':
    G = snap.GenSmallWorld(10, 3, 0.1)
    for EI in G.Edges():
        print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    # nx.draw(G)

    # plt.show()