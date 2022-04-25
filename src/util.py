import matplotlib.pyplot as plt
import networkx as nx
import snap
import random



def convertSnapToNx(snapGraph):
    edgeList = []
    for EI in snapGraph.Edges():
        edgeList.append((EI.GetSrcNId(), EI.GetDstNId()))

    return nx.Graph(edgeList)


def convertNxToSnap(nxGraph):
    edgeList = list(nxGraph.edges)
    nodesSet = set()
    for e1, e2 in edgeList:
        nodesSet.add(e1)
        nodesSet.add(e2)

    G = snap.TUNGraph.New()
    for node in nodesSet:
        G.AddNode(node)
    for e1, e2 in edgeList:
        G.AddEdge(e1, e2)

    return G


def drawSnapGraphPNG(snapGraph, filePath):
    labels = {}
    for NI in snapGraph.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    snapGraph.DrawGViz(snap.gvlDot, filePath, "", labels)


def drawNxCommunityGraph(graph, communities, title, withLabels=True):

    colors = []
    for j in range(len(communities)):
        rand_color = "#"
        for i in range(6):
            rand_color = rand_color + random.choice('ABCDEF0123456789')
        colors.append(rand_color)

    colorMap = []
    for node in graph:
        for i in range(len(communities)):
            if (node in communities[i]):
                colorMap.append(colors[i])

    nx.draw(graph, node_color=colorMap, with_labels=withLabels)
    plt.title(title)
    plt.show()


def loadDataFromSNAP(filename):
    file = open(filename, 'r')

    nodesSet = set()
    edgesList = []
    for line in file:
        edge = line.split()
        n1 = int(edge[0])
        n2 = int(edge[1])
        nodesSet.add(n1)
        nodesSet.add(n2)
        edgesList.append((n1, n2))

    G = snap.TUNGraph.New()
    for node in nodesSet:
        G.AddNode(node)
    for e1, e2 in edgesList:
        G.AddEdge(e1, e2)
    return G

def generateAndSaveGraph(n, k, p, N, PATH):
    for i in range(N):
        filename = PATH + "\\n" + str(n) + "_k" + str(k) + "_" + str(i+1) + ".txt"
        print(filename)
        G = nx.generators.watts_strogatz_graph(n, k, p)
        nx.write_edgelist(G, filename, encoding='utf-8')
