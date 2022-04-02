import matplotlib.pyplot as plt
import snap
import numpy as np
import util
import networkx as nx

if __name__ == '__main__':
    Rnd = snap.TRnd(0,1)
    G = snap.GenSmallWorld(100, 10, 0.1, Rnd)

    # labels = {}
    # for NI in G.Nodes():
    #     labels[NI.GetId()] = str(NI.GetId())
    # G.DrawGViz(snap.gvlDot, "10N-15E.png", "", labels)

    modularity, CmtyV = G.CommunityGirvanNewman()
    orderNum = 1
    print("Girvan Newman:")
    for Cmty in CmtyV:
        print("Community %d: " % orderNum)
        for NI in Cmty:
            print(NI, end=' ')
        print()
        orderNum += 1
    print("The modularity of the network is %f" % modularity)
    print()

    G1 = util.convertSnapToNx(G)
    nx.draw(G1, with_labels=True)
    plt.show()