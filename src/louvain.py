from cdlib import algorithms
from cdlib import evaluation
import networkx as nx
import snap
import matplotlib.pyplot as plt

import util

def evaluate(algorithm, graph, communities, coms):
    print(algorithm)
    mod = nx.algorithms.community.modularity(graph, communities)
    print(mod)

    mod = evaluation.surprise(graph, coms)
    print(mod)

    scd = evaluation.avg_transitivity(graph, coms)
    print(scd)

    size = evaluation.size(graph, coms)
    print(size)

    triangles = evaluation.triangle_participation_ratio(graph, coms)
    print(triangles)

    conductance = evaluation.conductance(graph, coms)
    print(conductance)

    print()


if __name__ == '__main__':
    # G = nx.generators.watts_strogatz_graph(1000, 20, 0.1)
    G1 = util.loadDataFromSNAP(r"C:\FER\9. semestar\Diplomski projekt\py_code\test_SNAP\SNAP_data\facebook_combined.txt")
    G = util.convertSnapToNx(G1)

    print("Louvain:")
    coms = algorithms.louvain(G, weight='weight', resolution=1.)
    communities = []
    for i in coms.communities:
        # print(i)
        communities.append(i)
    evaluate("Louvain", G, communities, coms)


    print("surprise:")
    coms = algorithms.surprise_communities(G)
    communities = []
    for i in coms.communities:
        # print(i)
        communities.append(i)

    evaluate("surprise", G, communities, coms)

    print("Leiden:")
    coms = algorithms.leiden(G)
    communities = []
    for i in coms.communities:
        # print(i)
        communities.append(i)
    evaluate("Leiden", G, communities, coms)

    print("walktrap:")
    coms = algorithms.walktrap(G)
    communities = []
    for i in coms.communities:
        # print(i)
        communities.append(i)
    evaluate("walktrap", G, communities, coms)



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