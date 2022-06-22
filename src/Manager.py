import math
import util
from Constants import *

import matplotlib.pyplot as plt


class Manager:
    def runAlgorithms(self, algorithms, graph, outputWriter):
        times = []
        for algorithm in algorithms:
            outputWriter.write(RUNNING + " " + algorithm.name)
            time = algorithm.run(graph)
            times.append(time)
        return times

    def evaluateAlgorithms(self, algorithms, measures, graph, outputWriter, draw):
        if (len(measures) > 0):
            i = 0
            x = 3
            y = math.ceil(len(measures) / 3)
            plt.figure(0)
            for measure in measures:
                print(measure.name)
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
        j = 1
        xN = 3
        yN = math.ceil((len(measures)-1) / 3)
        algorithmNames = []
        algorithmMarks = {GIRVAN_NEWMAN:("blue","o"), LOUVAIN:("cyan","v"), SURPRISE:("orange","s"),
                          LEIDEN:("red","1"), WALKTRAP:("magenta","+")}
        plt.figure(1)
        for i in range(len(measures)-1):
            plt.subplot(xN, yN, j)
            j += 1
            print(measures[i])
            c = 0
            for (k, v) in finalResults.items():
                x = []
                y = []
                for (k2, v2) in v.items():
                    if (len(dataLabels) > 0):
                        x.append(dataLabels[k2])
                    else:
                        x.append(k2)
                    y.append(v2[i])
                print(x,y, k, algorithmMarks[k])
                plt.scatter(x, y, color=algorithmMarks[k][0], marker=algorithmMarks[k][1])
                c+=1
                if(k not in algorithmNames):
                    algorithmNames.append(k)
            plt.title(measures[i] + " results")

            if (len(dataLabels) > 0):
                plt.xlabel("Dataset")
            else:
                plt.xlabel("Size")
            plt.ylabel(measures[i])
        plt.subplots_adjust(hspace=0.5)
        print(algorithmNames)
        plt.figlegend(algorithmNames)
        plt.draw()
        plt.pause(0.001)


        # time plot
        plt.figure(2)
        c = 0
        for (k, v) in finalResults.items():
            x = []
            y = []
            for (k2, v2) in v.items():
                if (len(dataLabels) > 0):
                    x.append(dataLabels[k2])
                else:
                    x.append(k2)
                y.append(v2[len(measures)-1])
            print(x, y, k, algorithmMarks[k])
            plt.scatter(x, y, color=algorithmMarks[k][0], marker=algorithmMarks[k][1])
            c += 1
            if (k not in algorithmNames):
                algorithmNames.append(k)
        plt.title(measures[len(measures)-1] + " results")

        if (len(dataLabels) > 0):
            plt.xlabel("Dataset")
        else:
            plt.xlabel("Size")
        plt.ylabel(measures[len(measures)-1] + " (s)")
        plt.figlegend(algorithmNames)
        plt.draw()
        plt.pause(0.001)