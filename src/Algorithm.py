from cdlib.classes.node_clustering import NodeClustering

import Constants
import util
import time


class IAlgorithm():
    def run(self, graph):
        pass

    def getLabelName(self):
        pass


class Algorithm(IAlgorithm):
    def __init__(self, name, algorithm):
        self.name = name
        self.algorithm = algorithm
        self.communities = []
        self.coms = None

    def run(self, graph):
        print("running " + self.name)
        start = time.time()
        self.coms = self.algorithm(graph)
        end = time.time()
        for i in self.coms.communities:
            self.communities.append(i)
        # print(self.communities)
        return end-start

    def getLabelName(self):
        return self.name


class GirvanNewman(IAlgorithm):
    def __init__(self):
        self.name = Constants.GIRVAN_NEWMAN
        self.labelName = Constants.GIRVAN_NEWMAN_LABEL
        # self.algorithm = algorithm
        self.communities = []
        self.coms = None

    def run(self, graph):
        print("running " + self.name)
        SNAP_graph = util.convertNxToSnap(graph)
        start = time.time()
        modularity, communities = SNAP_graph.CommunityGirvanNewman()
        end = time.time()

        self.communities = []
        for Cmty in communities:
            community = []
            # print("Community: ")
            for NI in Cmty:
                # print(NI)
                community.append(NI)
            self.communities.append(community)
        # print(self.communities)

        self.coms = NodeClustering(self.communities, graph)
        return end-start


    def getLabelName(self):
        return self.labelName
