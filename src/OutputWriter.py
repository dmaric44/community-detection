import tkinter as tk

class OutputWriter:
    def __init__(self, root, window):
        self.root = root
        self.window = window

    def write(self, text):
        self.window.config(state="normal")
        self.window.insert(tk.END, text + '\n')
        self.window.config(state="disabled")
        self.window.see("end")
        self.root.update_idletasks()