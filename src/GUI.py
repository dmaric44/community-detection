import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def askOpenFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    file = filedialog.askopenfilename(title='Select file', initialdir='/', filetypes=filetypes)
    print(file)

def runAlgorithms():
    if girvan_newman.get() == 1:
        print("GN")
    if louvain.get() == 1:
        print("Louvain")
    if surprise.get() == 1:
        print("Surprise")
    if leiden.get() == 1:
        print("Leiden")
    if walktrap.get() == 1:
        print("Walktrap")


if __name__ == '__main__':
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

    realDataTab = ttk.Frame(master=tabControl)
    chooseDataFileButton = tk.Button(master=realDataTab, text="Select data", command=askOpenFile)
    chooseDataFileButton.pack()

    tabControl.add(generateDataTab, text='Generate data')
    tabControl.add(realDataTab, text='Load data')

    tabControl.pack(fill=tk.BOTH)


    algoirithmsFrame = tk.Frame(master=leftFrame)
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

    startButton = tk.Button(master=algoirithmsFrame, text="Run", activeforeground="grey", command=runAlgorithms)
    startButton.pack()

    evaluationFrame = tk.Frame(master=leftFrame)
    evaluationFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    evaluationLabel = tk.Label(master=evaluationFrame, text="Select evaluation measures")
    evaluationLabel.pack()



    rightFrame = tk.Frame(master=root, width=100, height=300, bg='green')
    rightFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    root.mainloop()
