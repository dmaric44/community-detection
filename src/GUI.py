import tkinter as tk
from Algorithm import *
from measures import *
from Manager import Manager
import networkx as nx
from tkinter import ttk
from tkinter import filedialog
import util

from cdlib import algorithms as commAlgs
from cdlib import evaluation

filename = ""

def askOpenFile():
    global filename
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(title='Select file', initialdir='/', filetypes=filetypes)
    selectedFileLabel.config(text=filename.split("/")[-1])


def loadAndRunAlgorithms():
    snapG = util.loadDataFromSNAP(filename)
    nxG = util.convertSnapToNx(snapG)

    measures = getMeasures()
    print(len(measures))
    algorithms = getAlgorithms()
    manager.runAlgorithms(algorithms, nxG)
    manager.evaluateAlgorithms(algorithms, measures, graph)


def getAlgorithms():
    algorithms = []
    if girvan_newman.get() == 1:
        algorithms.append(GirvanNewman())
    if louvain.get() == 1:
        algorithms.append(Algorithm("Louvain", commAlgs.louvain))
    if surprise.get() == 1:
        algorithms.append(Algorithm("Surprise", commAlgs.surprise_communities))
    if leiden.get() == 1:
        algorithms.append(Algorithm("Leiden", commAlgs.leiden))
    if walktrap.get() == 1:
        algorithms.append(Algorithm("Walktrap", commAlgs.walktrap))
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
    graph = nx.generators.watts_strogatz_graph(int(networkSize.get()), int(connectedNearestNodes.get()), float(rewiringProbability.get()))
    algorithms = getAlgorithms()
    measures = getMeasures()

    manager.runAlgorithms(algorithms, graph)
    manager.evaluateAlgorithms(algorithms, measures, graph)

if __name__ == '__main__':
    manager = Manager()
    root = tk.Tk()

    topFrame = tk.Frame(master=root, width=300, height=40, bg='red')
    topFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    bottomFrame = tk.Frame(master=root, width=300, height=40, bg='blue')
    bottomFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    leftFrame = tk.Frame(master=root, width=150, height=200, bg='yellow')
    leftFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    dataFrame = tk.Frame(master=leftFrame)
    dataFrame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    tabControl = ttk.Notebook(master=dataFrame)

    networkSize = tk.StringVar()
    connectedNearestNodes = tk.StringVar()
    rewiringProbability = tk.StringVar()

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

    startButton = tk.Button(master=generateDataTab, text="Run", activeforeground="grey",
                            command=generateAndRunAlgorithms)
    startButton.grid(row=3, column=1)

    realDataTab = ttk.Frame(master=tabControl)
    chooseDataFileButton = tk.Button(master=realDataTab, text="Select data", command=askOpenFile)
    chooseDataFileButton.pack()

    selectedFileLabel = tk.Label(master=realDataTab, text="No file selected")
    selectedFileLabel.pack()

    startRealDataButton = tk.Button(master=realDataTab, text="Run", activeforeground="grey", command=loadAndRunAlgorithms)
    startRealDataButton.pack(fill=tk.BOTH)

    tabControl.add(generateDataTab, text='Generate data')
    tabControl.add(realDataTab, text='Load data')

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

    algorithm1 = tk.Checkbutton(master=algoirithmsFrame, text="Girvan-Newmann", variable=girvan_newman, onvalue=1, offvalue=0)
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

    root.mainloop()
