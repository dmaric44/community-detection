from cdlib.classes.node_clustering import NodeClustering

import Constants
import util


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
        self.coms = self.algorithm(graph)
        for i in self.coms.communities:
            self.communities.append(i)

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
        modularity, communities = util.convertNxToSnap(graph).CommunityGirvanNewman()

        self.communities = []
        for Cmty in communities:
            community = []
            print("Community: ")
            for NI in Cmty:
                print(NI)
                community.append(str(NI))
            self.communities.append(community)
        print(self.communities)

        self.coms = NodeClustering(self.communities, graph)


    def getLabelName(self):
        return self.labelName
