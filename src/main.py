import matplotlib.pyplot as plt
import networkx as nx
import snap
import util

if __name__ == '__main__':
    # G = snap.GenSmallWorld(10, 3, 0.1)
    # for EI in G.Edges():
    #     print("edge: (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    # nx.draw(G)

    # plt.show()

    G1 = util.loadDataFromSNAP(r"C:\FER\10. semestar\Diplomski rad\community-detection\SNAP_data\facebook_combined.txt")
    G2 = util.convertSnapToNx(G1)
    comp = nx.algorithms.community.girvan_newman(G2)
    print(tuple(sorted(c) for c in next(comp)))
