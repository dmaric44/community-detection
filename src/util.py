import networkx as nx
import snap


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
        edgesList.append((n1,n2))

    G = snap.TUNGraph.New()
    for node in nodesSet:
        G.AddNode(node)
    for e1, e2 in edgesList:
        G.AddEdge(e1, e2)
    return G