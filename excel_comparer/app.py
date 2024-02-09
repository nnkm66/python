# app.py

import os
from tkinter import messagebox
import pandas as pd
from tkinter import *
from tkinter.ttk import Treeview

from compare_files import compare_files
from display_results import display_results
from display_data import display_data
from select_files import select_files


class ExcelComparerApp:
    # """
    # Classe para comparação de arquivos Excel.

    # Atributos:
    #     root: Janela principal da aplicação.
    #     file_paths: Caminhos dos arquivos Excel selecionados.
    #     file_labels: Rótulos dos arquivos Excel selecionados.
    #     result_text1: Campo de texto para exibir os resultados da comparação do arquivo 1.
    #     result_text2: Campo de texto para exibir os resultados da comparação do arquivo 2.
    #     treeview1: Objeto Treeview para exibir os dados do arquivo 1.
    #     treeview2: Objeto Treeview para exibir os dados do arquivo 2.
    # """

    def __init__(self, root):
        self.root = root
        self.file_paths = []
        self.file_labels = []
        self.result_text1 = Text(self.root, wrap="word", state="disabled")
        self.result_text2 = Text(self.root, wrap="word", state="disabled")
        self.treeview1 = Treeview(self.root, columns=["Coluna", "Qtde. Notas", "Total"], show="headings", selectmode="browse")
        self.treeview2 = Treeview(self.root, columns=["Coluna", "Qtde. Notas", "Total"], show="headings", selectmode="browse")

        # Posicionamento dos widgets
        self.result_text1.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.treeview1.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.result_text2.grid(row=3, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.treeview2.grid(row=4, column=4, padx=10, pady=10, sticky="nsew")

        # Eventos
        self.root.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # """
        # Evento de clique do mouse.

        # Args:
        #     event: Evento do mouse.
        # """
        # Selecionar arquivos
        if len(self.file_paths) == 0:
            self.file_paths = select_files()

        # Validar arquivos
        if len(self.file_paths) != 2:
            messagebox.showerror("Erro", "Selecione dois arquivos Excel.")
            return

        # Definir rótulos dos arquivos
        self.file_labels[0] = os.path.basename(self.file_paths[0])
        self.file_labels[1] = os.path.basename(self.file_paths[1])

        # Comparar arquivos
        resultados = compare_files(self.file_paths)

        # Exibir resultados
        display_results(resultados, 0)
        display_data(pd.read_excel(self.file_paths[0]), 0)
        display_results(resultados, 1)
        display_data(pd.read_excel(self.file_paths[1]), 1)

    def mainloop(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = ExcelComparerApp(root)
    app.mainloop()
