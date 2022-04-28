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


    def analyizeFinalData(self, measures, finalResults:dict):
        for i in range(len(measures)):
            print(measures[i])
            algorithmNames = []
            plt.figure(i)
            for (k,v) in finalResults.items():
                x = []
                y = []
                for (k2, v2) in v.items():
                    x.append(k2)
                    y.append(v2[i])
                plt.scatter(x,y)
                algorithmNames.append(k)
            plt.legend(algorithmNames)
            plt.xlabel("Size")
            plt.ylabel(measures[i])
        plt.show()
                    # print(k, k2, v2[i])

