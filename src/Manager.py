class Manager():

    def runAlgorithms(self, algorithms, graph):
        for algorithm in algorithms:
            algorithm.run(graph)
