import math

import matplotlib.pyplot as plt

class Manager():
    def runAlgorithms(self, algorithms, graph):
        for algorithm in algorithms:
            algorithm.run(graph)

    def evaluateAlgorithms(self, algorithms, measures, graph):
        i=0
        x=3
        y=math.ceil(len(measures) / 3)
        for measure in measures:
            i += 1
            results = []
            algorithmNames = []
            for algorithm in algorithms:
                result = measure.calculate(graph, algorithm)
                results.append(result)
                algorithmNames.append(algorithm.name)
            print(x,y,i)
            plt.subplot(x,y,i)
            plt.bar(algorithmNames, results)
            plt.title(measure.name)
        plt.subplots_adjust(hspace=0.5)
        plt.show()


    def evaluateAlgorithm(self, algorithm, measures, graph):
        results = []
        for measure in measures:
            result = measure.calculate(graph, algorithm)
            results.append(result)
        return results