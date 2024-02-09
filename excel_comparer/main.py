# main.py
from tkinter import Tk
from compare_files import compare, display_results
from display_data import display_data
from select_files import select_files
import pandas as pd
def main():
    # Seleciona os arquivos a serem comparados
    caminhos = select_files()

    # Compara os arquivos
    resultados, colunas = compare(caminhos)

    # Exibe os resultados
    for coluna in range(len(resultados[0])):
        display_results(resultados, coluna)
        # Supondo que você queira exibir os dados aqui também
        display_data(pd.read_excel(caminhos[coluna]), coluna)

if __name__ == "__main__":
    main()

# import compare_files
# import display_results
# import display_data
# import select_files


# def main():
#     # Seleciona os arquivos a serem comparados
#     caminhos = select_files()

#     # Compara os arquivos
#     resultados = compare_files.compare(caminhos)

#     # Exibe os resultados
#     for coluna in range(len(resultados[0])):
#         display_results(resultados, coluna)


# if __name__ == "__main__":
#     main()
