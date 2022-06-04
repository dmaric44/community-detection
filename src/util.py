import matplotlib.pyplot as plt
from cdlib import algorithms, viz
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

    plt.title(title + " algorithm")
    nx.draw(graph, pos = nx.spring_layout(graph), node_color=colorMap, with_labels=withLabels)
    plt.draw()
    plt.pause(0.001)


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


def validateCreatingNetworkData(N, k, p, numOfGraphs = None):
    try:
        n = int(N)
        if(n <= 0):
            return "Number of nodes must be greater than 0!"
    except:
        return "Number of nodes must be integer and greater than 0!"
    try:
        K = int(k)
        if (K <= 0):
            return "Number of neighbours must be greater than 0!"
    except:
        return "Number of neighbours must be integer and greater than 0!"

    if(int(k) > int(N)):
        return "Number of neighbours must be less then number of nodes!"

    try:
        P = float(p)
        if(P < 0 or P > 1):
            return "Probability must be in [0,1] interval!"
    except:
        return "Probability must be float value!"

    if(numOfGraphs != None):
        try:
            g = int(numOfGraphs)
            if (g <= 0):
                return "Number of graphs must be greater than 0!"
        except:
            return "Number of graphs must be integer and greater than 0!"

    return "No error"
