import tkinter as tk
from tkinter import ttk

class Compras_ventana:
    def __init__(self, root):
        self.root = root

    def compra_existente(self):
        frame = tk.Frame(self.root, width=200, height=200, bg='black')
        frame.pack()

    def compra_nuevo(self):
        frame = tk.Frame(self.root, width=200, height=200, bg='red')
        frame.pack()
