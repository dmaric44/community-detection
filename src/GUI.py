import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import tkinter.scrolledtext
import tkinter.messagebox
import networkx as nx
import numpy as np
from cdlib import algorithms as commAlgs
from cdlib import evaluation

from Algorithm import *
from Manager import Manager
from measures import *
from OutputWriter import *

from Constants import *

filenames = ""
PATH = r'C:\FER\10. semestar\Diplomski rad\data'
outputWriter = None


def askOpenFile():
    global filenames
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filenames = filedialog.askopenfilenames(title='Select file', initialdir='/', filetypes=filetypes)
    print(filenames)
    if (len(filenames) == 0):
        print("No file selected")
    elif (len(filenames) == 1):
        selectedFileLabel.config(text=filenames[0].split("/")[-1])
    else:
        selectedFileLabel.config(text="Multiple files selected")


def generateAndSaveGraph():
    status = util.validateCreatingNetworkData(networkSize2.get(), connectedNearestNodes2.get(), rewiringProbability2.get(), numOfGraphs.get())
    if(status == 'No error'):
        nodes = int(networkSize2.get())
        connectedNearestNodes = int(connectedNearestNodes2.get())
        rewiringProbability = float(rewiringProbability2.get())
        noOfGraphs = int(numOfGraphs.get())
        outputWriter.write("\n" + CREATING_DATA)
        util.generateAndSaveGraph(nodes, connectedNearestNodes, rewiringProbability, noOfGraphs, PATH)
        outputWriter.write(DATA_CREATED)
    else:
        tk.messagebox.showerror("Error", status)


def loadAndRunAlgorithms():
    outputWriter.write("\n" + RUN_ANALYSIS)

    algorithm = {}
    algorithms = getAlgorithms()
    for a in algorithms:
        algorithm[a.name] = {}
    print(algorithm)

    measures = getMeasures()
    measureNames = []
    for m in measures:
        measureNames.append(m.name)

    for filename in filenames:
        print(filename)
        outputWriter.write("\n" + RUNNING + ": " + filename)

        G = nx.read_edgelist(filename)
        nodes = G.number_of_nodes()
        algorithms = getAlgorithms()
        measures = getMeasures()
        manager.runAlgorithms(algorithms, G, outputWriter)

        for a in algorithms:
            results = manager.evaluateAlgorithm(a, measures, G)
            if (nodes not in algorithm[a.name]):
                algorithm[a.name][nodes] = [results]
            else:
                algorithm[a.name][nodes].append(results)

    print(measureNames)
    finalResults = {}
    for (k,v) in algorithm.items():
        finalResults[k] = {}
        for (k2,v2) in v.items():
            res = np.zeros(len(measures))
            for data in v2:
                res = np.add(res, np.array(data))
            res = res / len(v2)
            finalResults[k][k2] = res

    for (k,v) in finalResults.items():
        print(k, v)
        outputWriter.write("\n" + k)
        for (k2, v2) in v.items():
            outputWriter.write(" Network size: " + str(k2))
            for i in range(len(v2)):
                outputWriter.write("  " + measureNames[i] + " " + str(v2[i]))


    manager.analyizeFinalData(measureNames, finalResults)



def getAlgorithms():
    algorithms = []
    if girvan_newman.get() == 1:
        algorithms.append(GirvanNewman())
    if louvain.get() == 1:
        algorithms.append(Algorithm(Constants.LOUVAIN, commAlgs.louvain))
    if surprise.get() == 1:
        algorithms.append(Algorithm(Constants.SURPRISE, commAlgs.surprise_communities))
    if leiden.get() == 1:
        algorithms.append(Algorithm(Constants.LEIDEN, commAlgs.leiden))
    if walktrap.get() == 1:
        algorithms.append(Algorithm(Constants.WALKTRAP, commAlgs.walktrap))
    return algorithms


def getMeasures():
    measures = []
    if modularity.get() == 1:
        measures.append(Modularity("Modularity", nx.algorithms.community.modularity))
    if transitivity.get() == 1:
        measures.append(Measure("Transitivity", evaluation.avg_transitivity))
    if size.get() == 1:
        measures.append(Measure("Size", evaluation.size))
    if triangles.get() == 1:
        measures.append(Measure("Triangles", evaluation.triangle_participation_ratio))
    if conductance.get() == 1:
        measures.append(Measure("Conductance", evaluation.conductance))
    return measures


def generateAndRunAlgorithms():
    status = util.validateCreatingNetworkData(networkSize.get(), connectedNearestNodes.get(), rewiringProbability.get())
    if(status == "No error"):
        outputWriter.write("\n" + QUICK_TEST)
        graph = nx.generators.watts_strogatz_graph(int(networkSize.get()), int(connectedNearestNodes.get()),
                                                   float(rewiringProbability.get()))
        algorithms = getAlgorithms()
        measures = getMeasures()

        manager.runAlgorithms(algorithms, graph, outputWriter)
        manager.evaluateAlgorithms(algorithms, measures, graph, outputWriter, draw.get())

    else:
        tk.messagebox.showerror("Error", status)


if __name__ == '__main__':
    manager = Manager()
    root = tk.Tk()

    # topFrame = tk.Frame(master=root, width=300, height=40)#, bg='red')
    # topFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    # bottomFrame = tk.Frame(master=root, width=300, height=40)#, bg='blue')
    # bottomFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    leftFrame = tk.Frame(master=root, width=150, height=200)#, bg='yellow')
    leftFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    dataFrame = tk.Frame(master=leftFrame, highlightbackground="black", highlightthickness=2)
    dataFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    tabControl = ttk.Notebook(master=dataFrame)

    networkSize = tk.StringVar()
    connectedNearestNodes = tk.StringVar()
    rewiringProbability = tk.StringVar()
    draw = tk.IntVar()

    generateDataTab = ttk.Frame(master=tabControl)
    networkSizeLabel = tk.Label(master=generateDataTab, text="Size of network")
    networkSizeLabel.grid(row=0, column=0)
    networkSizeEntry = tk.Entry(master=generateDataTab, textvariable=networkSize)
    networkSizeEntry.grid(row=0, column=1)

    connectedNearestNodesLabel = tk.Label(master=generateDataTab, text="Number of nearest neighbours")
    connectedNearestNodesLabel.grid(row=1, column=0)
    connectedNearestNodesEntry = tk.Entry(master=generateDataTab, textvariable=connectedNearestNodes)
    connectedNearestNodesEntry.grid(row=1, column=1)

    rewiringProbabilityLabel = tk.Label(master=generateDataTab, text="Probability of rewiring each edge")
    rewiringProbabilityLabel.grid(row=2, column=0)
    rewiringProbabilityEntry = tk.Entry(master=generateDataTab, textvariable=rewiringProbability)
    rewiringProbabilityEntry.grid(row=2, column=1)

    tk.Checkbutton(generateDataTab, text="draw graph", variable=draw).grid(row=3, column=0)

    startButton = tk.Button(master=generateDataTab, text="Run", activeforeground="grey",
                            command=generateAndRunAlgorithms)
    startButton.grid(row=4, column=1)

    analizeDataTab = ttk.Frame(master=tabControl)
    chooseDataFileButton = tk.Button(master=analizeDataTab, text="Select data", command=askOpenFile)
    chooseDataFileButton.pack()

    selectedFileLabel = tk.Label(master=analizeDataTab, text="No file selected")
    selectedFileLabel.pack()

    startRealDataButton = tk.Button(master=analizeDataTab, text="Run", activeforeground="grey",
                                    command=loadAndRunAlgorithms)
    startRealDataButton.pack(fill=tk.BOTH)

    networkSize2 = tk.StringVar()
    connectedNearestNodes2 = tk.StringVar()
    rewiringProbability2 = tk.StringVar()
    numOfGraphs = tk.StringVar()

    generateAndSaveDataTab = ttk.Frame(master=tabControl)
    networkSizeLabel2 = tk.Label(master=generateAndSaveDataTab, text="Size of network")
    networkSizeLabel2.grid(row=0, column=0)
    networkSizeEntry2 = tk.Entry(master=generateAndSaveDataTab, textvariable=networkSize2)
    networkSizeEntry2.grid(row=0, column=1)

    connectedNearestNodesLabel2 = tk.Label(master=generateAndSaveDataTab, text="Number of nearest neighbours")
    connectedNearestNodesLabel2.grid(row=1, column=0)
    connectedNearestNodesEntry2 = tk.Entry(master=generateAndSaveDataTab, textvariable=connectedNearestNodes2)
    connectedNearestNodesEntry2.grid(row=1, column=1)

    rewiringProbabilityLabel2 = tk.Label(master=generateAndSaveDataTab, text="Probability of rewiring each edge")
    rewiringProbabilityLabel2.grid(row=2, column=0)
    rewiringProbabilityEntry2 = tk.Entry(master=generateAndSaveDataTab, textvariable=rewiringProbability2)
    rewiringProbabilityEntry2.grid(row=2, column=1)

    numberOfGraphsLabel = tk.Label(master=generateAndSaveDataTab, text="Number of graphs")
    numberOfGraphsLabel.grid(row=3, column=0)
    numberOfGraphsEntry = tk.Entry(master=generateAndSaveDataTab, textvariable=numOfGraphs)
    numberOfGraphsEntry.grid(row=3, column=1)

    startButton2 = tk.Button(master=generateAndSaveDataTab, text="Generate data", activeforeground="grey",
                             command=generateAndSaveGraph)
    startButton2.grid(row=4, column=1)

    tabControl.add(generateDataTab, text='Quick test')
    tabControl.add(analizeDataTab, text='Run analysis')
    tabControl.add(generateAndSaveDataTab, text='Create data')

    tabControl.pack(fill=tk.BOTH)

    algoirithmsFrame = tk.Frame(master=leftFrame, highlightbackground="black", highlightthickness=2)
    algoirithmsFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    chooseAlgorithmsLabel = tk.Label(master=algoirithmsFrame, text="Choose algorithms")
    chooseAlgorithmsLabel.pack()

    girvan_newman = tk.IntVar()
    louvain = tk.IntVar()
    surprise = tk.IntVar()
    leiden = tk.IntVar()
    walktrap = tk.IntVar()

    algorithm1 = tk.Checkbutton(master=algoirithmsFrame, text="Girvan-Newmann", variable=girvan_newman, onvalue=1,
                                offvalue=0)
    algorithm1.pack(anchor='w')

    algorithm2 = tk.Checkbutton(master=algoirithmsFrame, text="Louvain", variable=louvain, onvalue=1, offvalue=0)
    algorithm2.pack(anchor='w')

    algorithm3 = tk.Checkbutton(master=algoirithmsFrame, text="Surprise", variable=surprise, onvalue=1, offvalue=0)
    algorithm3.pack(anchor='w')

    algorithm4 = tk.Checkbutton(master=algoirithmsFrame, text="Leiden", variable=leiden, onvalue=1, offvalue=0)
    algorithm4.pack(anchor='w')

    algorithm5 = tk.Checkbutton(master=algoirithmsFrame, text="Walktrap", variable=walktrap, onvalue=1, offvalue=0)
    algorithm5.pack(anchor='w')

    evaluationFrame = tk.Frame(master=leftFrame, highlightbackground="black", highlightthickness=2)
    evaluationFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    evaluationLabel = tk.Label(master=evaluationFrame, text="Select evaluation measures")
    evaluationLabel.pack()

    modularity = tk.IntVar()
    transitivity = tk.IntVar()
    size = tk.IntVar()
    triangles = tk.IntVar()
    conductance = tk.IntVar()

    measure1 = tk.Checkbutton(master=evaluationFrame, text="modularity", variable=modularity, onvalue=1, offvalue=0)
    measure1.pack(anchor='w')

    measure2 = tk.Checkbutton(master=evaluationFrame, text="transitivity", variable=transitivity, onvalue=1, offvalue=0)
    measure2.pack(anchor='w')

    measure3 = tk.Checkbutton(master=evaluationFrame, text="size", variable=size, onvalue=1, offvalue=0)
    measure3.pack(anchor='w')

    measure4 = tk.Checkbutton(master=evaluationFrame, text="triangles ratio", variable=triangles, onvalue=1, offvalue=0)
    measure4.pack(anchor='w')

    measure5 = tk.Checkbutton(master=evaluationFrame, text="conductance", variable=conductance, onvalue=1, offvalue=0)
    measure5.pack(anchor='w')

    rightFrame = tk.Frame(master=root, width=100, height=300, bg='green')
    rightFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    outputWindow = tk.scrolledtext.ScrolledText(rightFrame, height=30, width=50)
    outputWindow.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    outputWindow.config(state="disabled")

    outputWriter = OutputWriter(root, outputWindow)

    root.mainloop()
