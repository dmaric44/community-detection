class Manager():

    def runAlgorithms(self, algorithms, graph):
        for algorithm in algorithms:
            algorithm.run(graph)

    def evaluateAlgorithms(self, algorithms, measures, graph):
        for algorithm in algorithms:
            print(algorithm.name)
            for measure in measures:
                print(measure.name)
                measure.calculate(graph, algorithm)