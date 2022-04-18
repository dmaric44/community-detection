import tkinter as tk


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

    chooseAlgorithmsLabel = tk.Label(master=leftFrame, text="Choose algorithms")
    chooseAlgorithmsLabel.pack()

    girvan_newman = tk.IntVar()
    louvain = tk.IntVar()
    surprise = tk.IntVar()
    leiden = tk.IntVar()
    walktrap = tk.IntVar()

    algorithm1 = tk.Checkbutton(master=leftFrame, text="Girvan-Newmann", variable=girvan_newman, onvalue=1, offvalue=0)
    algorithm1.pack(anchor='w')

    algorithm2 = tk.Checkbutton(master=leftFrame, text="Louvain", variable=louvain, onvalue=1, offvalue=0)
    algorithm2.pack(anchor='w')

    algorithm3 = tk.Checkbutton(master=leftFrame, text="Surprise", variable=surprise, onvalue=1, offvalue=0)
    algorithm3.pack(anchor='w')

    algorithm4 = tk.Checkbutton(master=leftFrame, text="Leiden", variable=leiden, onvalue=1, offvalue=0)
    algorithm4.pack(anchor='w')

    algorithm5 = tk.Checkbutton(master=leftFrame, text="Walktrap", variable=walktrap, onvalue=1, offvalue=0)
    algorithm5.pack(anchor='w')

    startButton = tk.Button(master=leftFrame, text="Run", activeforeground="grey", command=runAlgorithms)
    startButton.pack()

    rightFrame = tk.Frame(master=root, width=100, height=300, bg='green')
    rightFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    root.mainloop()
