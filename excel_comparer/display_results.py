# display_results.py
import tkinter as tk

def display_results(resultados, coluna, colunas):
    # Seu código existente aqui
    root = tk.Tk()
    root.title(f"Comparação de Arquivos Excel - {colunas[coluna]}")
    text = tk.Text(root, wrap="word", state="disabled")
    text.config(height=len(resultados), width=50)
    text.insert(tk.END, "\n".join(map(str, resultados)))
    text.config(state="normal")
    text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    root.mainloop()

# # display_results.py

# import tkinter as tk
# from compare_files import colunas

# def display_results(resultados, coluna):
#     # """
#     # Exibe os resultados da comparação.

#     # Args:
#     #     resultados: Lista de resultados.
#     #     coluna: Coluna da tabela de resultados.
#     # """

#     root = tk.Tk()
#     root.title(f"Comparação de Arquivos Excel - {colunas[coluna]}")
#     text = tk.Text(root, wrap="word", state="disabled")
#     text.config(height=len(resultados), width=50)
#     text.insert(tk.END, "\n".join(resultados))
#     text.config(state="normal")
#     text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
#     root.mainloop()
