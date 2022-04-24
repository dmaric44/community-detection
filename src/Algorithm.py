from cdlib.classes.node_clustering import NodeClustering
import util

class Algorithm:
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

        print(self.coms)
        print(self.communities)



class GirvanNewman:
    def __init__(self):
        self.name = "Girvan Newman"
        # self.algorithm = algorithm
        self.communities = []
        self.coms = None

    def run(self, graph):
        print("running " + self.name)
        modularity, self.communities = util.convertNxToSnap(graph).CommunityGirvanNewman()
        self.coms = NodeClustering(self.communities, graph)

        print(self.coms)
        print(self.communities)

