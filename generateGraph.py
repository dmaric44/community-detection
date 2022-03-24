import snap
import numpy as np

if __name__ == '__main__':
    Rnd = snap.TRnd(0,1)
    G = snap.GenSmallWorld(10, 3, 0.1, Rnd)

    labels = {}
    for NI in G.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    G.DrawGViz(snap.gvlDot, "10N-15E.png", "", labels)

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