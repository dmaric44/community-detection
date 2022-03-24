import networkx as nx
import snap
import matplotlib.pyplot as plt

import util

if __name__ == '__main__':
    # edgeList = [(1, 2), (1, 3), (2, 3)]
    # G = nx.watts_strogatz_graph(20,6,0.1)

    Rnd = snap.TRnd(0, 1)
    G1 = snap.GenSmallWorld(10, 3, 0.1, Rnd)



    G2 = util.convertSnapToNx(G1)

    modularity, CmtyV = G1.CommunityGirvanNewman()
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


    nx.draw(G2, with_labels=True)
    plt.show()
