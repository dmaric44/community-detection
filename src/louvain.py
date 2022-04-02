from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import snap
import matplotlib.pyplot as plt

import util

if __name__ == '__main__':
    # G = nx.generators.watts_strogatz_graph(1000, 20, 0.1)
    G1 = util.loadDataFromSNAP(r"C:\FER\10. semestar\Diplomski rad\community-detection\SNAP_data\facebook_combined.txt")
    G = util.convertSnapToNx(G1)

    coms = algorithms.louvain(G, weight='weight', resolution=1.)
    communities = []
    for i in coms.communities:
        print(i)
        communities.append(i)

    mod = nx.algorithms.community.modularity(G,communities)
    print(mod)

    mod = evaluation.surprise(G, coms)
    print(mod)
    print()

    coms = algorithms.surprise_communities(G)
    communities = []
    for i in coms.communities:
        print(i)
        communities.append(i)

    mod = nx.algorithms.community.modularity(G, communities)
    print(mod)

    mod = evaluation.surprise(G, coms)
    print(mod)
    print()

    coms = algorithms.leiden(G)
    communities = []
    for i in coms.communities:
        print(i)
        communities.append(i)

    mod = nx.algorithms.community.modularity(G, communities)
    print(mod)

    mod = evaluation.surprise(G, coms)
    print(mod)
    print()

    coms = algorithms.walktrap(G)
    communities = []
    for i in coms.communities:
        print(i)
        communities.append(i)

    mod = nx.algorithms.community.modularity(G, communities)
    print(mod)

    mod = evaluation.surprise(G, coms)
    print(mod)
    print()

    # Girvan-Newman
    # G = util.convertNxToSnap(G)
    # modularity, CmtyV = G.CommunityGirvanNewman()
    # orderNum = 1
    # print("Girvan Newman:")
    # for Cmty in CmtyV:
    #     print("Community %d: " % orderNum)
    #     for NI in Cmty:
    #         print(NI, end=' ')
    #     print()
    #     orderNum += 1
    # print("The modularity of the network is %f" % modularity)
    # print()

    # nx.draw(G, with_labels=True)
    # plt.show()