# display_data.py
import tkinter as tk
from tkinter import ttk

def display_data(df, coluna, colunas):
    # Seu código existente aqui
    root = tk.Tk()
    root.title(f"Dados do Arquivo - {colunas[coluna]}")
    treeview = ttk.Treeview(root, columns=["Coluna", "Qtde. Notas", "Total"], show="headings", selectmode="browse")

    for i in range(len(df)):
        row = [df.columns[i], len(df[df[df.columns[i]] == df.iloc[i, i]]), df.iloc[i, i]]
        treeview.insert('', i, values=row)

    treeview.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    root.mainloop()

# # display_data.py

# import tkinter as tk
# from tkinter import ttk
# from compare_files import colunas

# def display_data(df, coluna):
#     # """
#     # Exibe os dados do arquivo.

#     # Args:
#     #     df: DataFrame com os dados.
#     #     coluna: Coluna da tabela de dados.
#     # """

#     root = tk.Tk()
#     root.title(f"Dados do Arquivo - {colunas[coluna]}")
#     treeview = ttk.Treeview(root, columns=["Coluna", "Qtde. Notas", "Total"], show="headings", selectmode="browse")

#     for i in range(len(df)):
#         row = [df.columns[i], len(df[df[df.columns[i]] == df.iloc[i, i]]), df.iloc[i, i]]
#         treeview.insert('', i, values=row)

#     treeview.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
#     root.mainloop()
