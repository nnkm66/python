# select_files.py
import os
import tkinter as tk
from tkinter import filedialog

def select_files():
    # Seu código existente aqui
    root = tk.Tk()
    root.withdraw()

    caminhos = [os.path.abspath(file) for file in filedialog.askopenfilenames(
        filetypes=[("Arquivos Excel", "*.xlsx")], title="Selecione dois arquivos Excel")]
    root.destroy()

    return caminhos

# # select_files.py

# import os
# import tkinter as tk


# def select_files():
#     # """
#     # Seleciona dois arquivos Excel.

#     # Returns:
#     #     Lista de caminhos dos arquivos.
#     # """

#     root = tk.Tk()
#     root.withdraw()

#     caminhos = [os.path.abspath(file) for file in tk.filedialog.askopenfilenames(
#         filetypes=[("Arquivos Excel", "*.xlsx")], title="Selecione dois arquivos Excel")]
#     root.destroy()

#     return caminhos
