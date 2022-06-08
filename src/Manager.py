import math
import util
from Constants import *

import matplotlib.pyplot as plt


class Manager:
    def runAlgorithms(self, algorithms, graph, outputWriter):
        for algorithm in algorithms:
            outputWriter.write(RUNNING + " " + algorithm.name)
            algorithm.run(graph)

    def evaluateAlgorithms(self, algorithms, measures, graph, outputWriter, draw):
        if (len(measures) > 0):
            i = 0
            x = 3
            y = math.ceil(len(measures) / 3)
            plt.figure(0)
            for measure in measures:
                outputWriter.write('\n' + EVALUATING + " " + measure.name)
                i += 1
                results = []
                algorithmNames = []
                for algorithm in algorithms:
                    result = measure.calculate(graph, algorithm)
                    outputWriter.write(" " + algorithm.name + ": " + str(result))
                    results.append(result)
                    algorithmNames.append(algorithm.getLabelName())
                print(x, y, i)
                plt.subplot(x, y, i)
                print(algorithmNames, results)
                plt.bar(algorithmNames, results)
                plt.title(measure.name)
                # plt.xticks(rotation=30, ha='right')
            plt.subplots_adjust(hspace=0.5)
            plt.draw()
            plt.pause(0.001)

        if (draw):
            i = 1
            for algorithm in algorithms:
                plt.figure(i)
                i += 1
                util.drawNxCommunityGraph(graph, algorithm.communities, algorithm.name)

    def evaluateAlgorithm(self, algorithm, measures, graph):
        results = []
        for measure in measures:
            result = measure.calculate(graph, algorithm)
            results.append(result)
        return results

    def analyizeFinalData(self, measures, finalResults: dict, dataLabels: dict):
        for i in range(len(measures)):
            print(measures[i])
            algorithmNames = []
            plt.figure(i)
            for (k, v) in finalResults.items():
                x = []
                y = []
                for (k2, v2) in v.items():
                    if (len(dataLabels) > 0):
                        x.append(dataLabels[k2])
                    else:
                        x.append(k2)
                    y.append(v2[i])
                plt.scatter(x, y)
                algorithmNames.append(k)
            plt.title(measures[i] + " results")
            plt.legend(algorithmNames)
            if (len(dataLabels) > 0):
                plt.xlabel("Dataset")
            else:
                plt.xlabel("Size")
            plt.ylabel(measures[i])
        plt.show()
        # print(k, k2, v2[i])
