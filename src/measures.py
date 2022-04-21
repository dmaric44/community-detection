class IMeasure:
    def calculate(self, graph, algorithm):
        pass


class Measure(IMeasure):
    def __init__(self, name, measure):
        self.name = name
        self.measure = measure

    def calculate(self, graph, algorithm):
        measure = self.measure(graph, algorithm.coms)
        print(measure)


class Modularity(IMeasure):
    def __init__(self, name, measure):
        self.name = name
        self.measure = measure

    def calculate(self, graph, algorithm):
        measure = self.measure(graph, algorithm.communities)
        print(measure)