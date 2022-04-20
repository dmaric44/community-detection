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