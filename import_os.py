import os
import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, VERTICAL
from tkinter import ttk
import matplotlib.pyplot as plt
import io
import base64
from PIL import Image, ImageTk
import pandas as pd


class ExcelComparerApp:
    def __init__(self, root):
        self.root = root  # Define a janela principal
        self.root.title("Excel Comparer")  # Define o título da janela
        self.root.geometry(f"{1920}x{1080}")  # Define o tamanho da janela
        self.root.config(bg="black")

        self.file_paths = [None, None]  # Inicializa os caminhos dos arquivos a serem comparados
        self.file_labels = {}  # Inicializa os rótulos dos arquivos
        self.label_file1 = tk.Label(self.root, text="Arquivo 1:")  # Rótulo para o primeiro arquivo
        self.label_file2 = tk.Label(self.root, text="Arquivo 2:")  # Rótulo para o segundo arquivo

        # Botões para selecionar os arquivos
        self.select_files_button1 = tk.Button(root, text="Selecionar Arquivos 1", command=lambda: self.select_files(0), relief="ridge", borderwidth=5)
        self.select_files_button2 = tk.Button(root, text="Selecionar Arquivos 2", command=lambda: self.select_files(1), relief="ridge", borderwidth=5)
        # Botão para iniciar a comparação
        self.compare_button = tk.Button(root, text="Comparar", command=self.compare_excel_files, relief="ridge", borderwidth=5)
        
        # Botão para reiniciar os resultados
        self.reset_button1 = tk.Button(root, text="Reiniciar Resultados", command=self.reset_results, relief="ridge", borderwidth=5)
        self.reset_button1.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="e")
        self.reset_button1

        # Posiciona os botões e rótulos na janela
        self.select_files_button1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.label_file1.grid(row=0, column=1, pady=10, sticky="w")
        self.select_files_button2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.label_file2.grid(row=1, column=1, pady=10, sticky="w")
        self.compare_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        # Campo de texto para exibir os resultados A
        self.result_text1 = Text(root, wrap="word")
        self.result_text1.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Posiciona o campo de texto abaixo dos botões
       
        # Obtém a posição atual do widget
        x = self.result_text1.winfo_x()
        y = self.result_text1.winfo_y()
        
        # Adiciona uma barra de rolagem vertical
        scrollbar = Scrollbar(root, command=self.result_text1.yview)
        scrollbar.grid(row=3, column=4, sticky='nsew')
        self.result_text1.config(yscrollcommand=scrollbar.set)
        
        x = scrollbar.winfo_x()
        y = scrollbar.winfo_y()
        
        scrollbar.place(x=1151, y=150, height=350)
        ##(x=566, y=150, height=350)

        # Configura a barra de rolagem para rolar uma linha por vez
        scrollbar.config(command=self.result_text1.yview, orient=VERTICAL)

        # Define o tamanho do widget em pixels, mantendo a posição atual
        self.result_text1.place(x=600, y=150, width=550, height=350)
        ##self.result_text1.place(x=15, y=150, width=550, height=350)
        
        # Campo de texto para exibir os resultados B
        self.result_text2 = Text(root, wrap="word")
        self.result_text2.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")  # Posiciona o campo de texto abaixo dos botões
       
        # Obtém a posição atual do widget
        x = self.result_text2.winfo_x()
        y = self.result_text2.winfo_y()
        
        # Adiciona uma barra de rolagem vertical
        scrollbar2 = Scrollbar(root, command=self.result_text1.yview)
        scrollbar2.grid(row=3, column=4, sticky='nsew')
        self.result_text2.config(yscrollcommand=scrollbar2.set)
        
        x = scrollbar2.winfo_x()
        y = scrollbar2.winfo_y()
        
        scrollbar2.place(x=566, y=150, height=350)
        ##(x=1151, y=150, height=350)

        # Define o tamanho do widget em pixels, mantendo a posição atual
        self.result_text2.place(x=15, y=150, width=550, height=350)
        ##self.result_text2.place(x=600, y=150, width=550, height=350)

        # Adiciona um Treeview para exibir os dados do Arquivo 1
        self.treeview_file1 = ttk.Treeview(root, columns=['COLUNA', 'QTD_NOTAS', 'TOTAL1'], show="headings", selectmode="browse")
        
        # self.treeview_file1.heading("#1", text="ID", anchor="w")
        self.treeview_file1.heading("COLUNA", text="COLUNA", anchor="w")
        self.treeview_file1.heading("QTD_NOTAS", text="QTD_NOTAS", anchor="w")
        self.treeview_file1.heading("TOTAL1", text="TOTAL1", anchor="w")
        self.treeview_file1.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Obtém a posição atual do widget
        x = self.treeview_file1.winfo_x()
        y = self.treeview_file1.winfo_y()

        # Define o tamanho do widget em pixels, mantendo a posição atual
        self.treeview_file1.place(x=15, y=520, width=235, height=315)

         # Adiciona um Treeview para exibir os dados do Arquivo 2
        self.treeview_file2 = ttk.Treeview(root, columns=['COLUNA', 'QTD_NOTAS', 'TOTAL2'], show="headings", selectmode="browse")
        self.treeview_file2.heading("COLUNA", text="COLUNA", anchor="w")
        self.treeview_file2.heading("QTD_NOTAS", text="QTD_NOTAS", anchor="w")
        self.treeview_file2.heading("TOTAL2", text="TOTAL2", anchor="w")
        self.treeview_file2.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        # Obtém a posição atual do widget
        x = self.treeview_file2.winfo_x()
        y = self.treeview_file2.winfo_y()

        # Define o tamanho do widget em pixels, mantendo a posição atual
        self.treeview_file2.place(x=600, y=520, width=235, height=315)
        
    def reset_results(self):
        # Limpar os campos de texto
        self.result_text1.config(state=tk.NORMAL)
        self.result_text1.delete(1.0, tk.END)
        self.result_text1.config(state=tk.DISABLED)

        self.result_text2.config(state=tk.NORMAL)
        self.result_text2.delete(1.0, tk.END)
        self.result_text2.config(state=tk.DISABLED)

        # Limpar as árvores
        self.treeview_file1.delete(*self.treeview_file1.get_children())
        self.treeview_file2.delete(*self.treeview_file2.get_children())

        # Limpar os rótulos de arquivo
        self.label_file1.config(text="Arquivo 1:")
        self.label_file2.config(text="Arquivo 2:")

        # Limpar os caminhos dos arquivos
        self.file_paths = [None, None]

    def select_files(self, button_index):
        # Abre a janela de seleção de arquivo
        file_path = filedialog.askopenfilename(
            title="Selecionar Arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx")],
        )

        if file_path:
            # Se um arquivo foi selecionado, atualiza o caminho do arquivo e o rótulo correspondente
            self.file_paths[button_index] = file_path
            if button_index == 0:
                self.label_file1.config(text=f"Arquivo 1: {os.path.basename(file_path)}")
                
                # Lê o arquivo e preenche o Treeview_file1 com os dados
                self.read_and_display_data(file_path, self.treeview_file1)
                
            else:
                self.label_file2.config(text=f"Arquivo 2: {os.path.basename(file_path)}")

                 # Lê o arquivo e preenche o Treeview_file1 com os dados
                self.read_and_display_data(file_path, self.treeview_file2)
                
    def compare_excel_files(self):
    # Compara os arquivos Excel selecionados
        if not all(self.file_paths):
            # Se algum arquivo não foi selecionado, exibe uma mensagem
            self.result_text2.config(state=tk.NORMAL)
            self.result_text2.insert(tk.END, "Selecione dois arquivos para comparar.\n")
            self.result_text2.config(state=tk.DISABLED)
            return
        dataframes1 = []
        dataframes2 = []
        for file in self.file_paths:
            try:
                # Tenta ler cada arquivo como um DataFrame do pandas
                df1 = pd.read_excel(self.file_paths[0])
                df2 = pd.read_excel(self.file_paths[1])
                dataframes1.append(df1)
                dataframes2.append(df2)
            except Exception as e:
                # Se ocorrer um erro, exibe uma mensagem e interrompe a comparação
                self.result_text2.config(state=tk.NORMAL)
                self.result_text2.insert(tk.END, f"Erro ao ler o arquivo {os.path.basename(file)}: {str(e)}\n")
                self.result_text2.config(state=tk.DISABLED)
                return
        COLUNA_comparacao = 'NR_NOTA'  # Define a COLUNA a ser comparada
        COLUNA_somatorio = 'VALOR'     # Define a COLUNA a ser comparada
        notas_processadas_A = set()
        notas_processadas_B = set()
        resultados_A = []
        resultados_B = []
            # Inicializa o total para cada arquivo
        total_A = 0
        total_B = 0
        for i, df1 in enumerate(dataframes1):
                if COLUNA_comparacao not in df1.columns:
                    # Se a COLUNA não existe no DataFrame, exibe uma mensagem e interrompe a comparação
                    self.result_text1.config(state=tk.NORMAL)
                    self.result_text1.insert(tk.END, f"A COLUNA '{COLUNA_comparacao}' não existe no arquivo {os.path.basename(self.file_paths[i % 2])}.\n")
                    self.result_text1.config(state=tk.DISABLED)
                    return
        for g, df2 in enumerate(dataframes2):
                if COLUNA_comparacao not in df2.columns:
                    # Se a COLUNA não existe no DataFrame, exibe uma mensagem e interrompe a comparação
                    self.result_text2.config(state=tk.NORMAL)
                    self.result_text2.insert(tk.END, f"A COLUNA '{COLUNA_comparacao}' não existe no arquivo {os.path.basename(self.file_paths[g % 2])}.\n")
                    self.result_text2.config(state=tk.DISABLED)
                    return    
                # Inicializar uma lista para armazenar os dados que não existem em ambos os arquivos
        dados_nao_existentes_A = []
        dados_nao_existentes_B = []
                # # Percorrer as linhas do arquivo A
        for i, linha_a in dataframes1[i % 2].iterrows():
                    # Verificar se o valor da célula existe no arquivo A
                nota_a = linha_a[COLUNA_comparacao]
                valor_a = linha_a[COLUNA_somatorio]
                    # Verificar se a nota existe no arquivo A
                if nota_a not in df1[COLUNA_comparacao].values and nota_a not in notas_processadas_A:
                        # Acumular os dados que não existem
                        dados_nao_existentes_A.append((nota_a, valor_a))
                        notas_processadas_A.add(nota_a)
                else:
                        # A nota existe em ambos os arquivos, comparar os valores
                    linha_b = dataframes1[(i + 1) % 1][dataframes1[(i + 1) % 1][COLUNA_comparacao] == nota_a].iloc[0]
                    valor_b = linha_b[COLUNA_somatorio]
                    if valor_a != valor_a:
                        resultados_A.append(f"Valor diferente para a nota {nota_a}: Arquivo 2 - {valor_a}, Arquivo 1 - {valor_b}\n")
                    total_A += valor_a     
        for nota_a, valor_a in dados_nao_existentes_A:
                    resultados_A.append(f"Nota não existente na tabela 2 {nota_a} no valor de {valor_a}\n")
                        # Exibe os resultados A
                    for resultado_A in resultados_A:
                        self.result_text1.config(state=tk.NORMAL)
                        self.result_text1.insert(tk.END, resultado_A)
                        self.result_text1.config(state=tk.DISABLED)
        self.treeview_file1.insert("", "end", values=("TOTAL1", "", round(total_A, 2))) 
        total_A = 0        
                # Percorrer as linhas do arquivo B
        for g, linha_b in dataframes2[g % 2].iterrows():
                    # Verificar se o valor da célula existe no arquivo A
                    nota_b = linha_b[COLUNA_comparacao]
                    valor_b = linha_b[COLUNA_somatorio]
                    # Verificar se a nota existe no arquivo A
                    if nota_b not in df2[COLUNA_comparacao].values and nota_b not in notas_processadas_B:
                        # Acumular os dados que não existem
                        dados_nao_existentes_B.append((nota_b, valor_b))
                        notas_processadas_B.add(nota_b)
                    else:
                        # A nota existe em ambos os arquivos, comparar os valores
                        linha_a = df2[df2[COLUNA_comparacao] == nota_b].iloc[0]
                        valor_a = linha_a[COLUNA_somatorio]
                        if valor_b != valor_a:
                            resultados_B.append(f"Valor diferente para a nota {nota_b}: Arquivo 2 - {valor_b}, Arquivo 1 - {valor_a}\n")
                    total_B += valor_b     
        for nota_b, valor_b in dados_nao_existentes_B:
                 resultados_B.append(f"Nota não existente na tabela 2 {nota_b} no valor de {valor_b}\n")
            # Exibe os resultados B
        for resultado_B in resultados_B:
            self.result_text2.config(state=tk.NORMAL)
            self.result_text2.insert(tk.END, resultado_B)
            self.result_text2.config(state=tk.DISABLED)
        self.treeview_file2.insert("", "end", values=("TOTAL2", "", round(total_B, 2)))
        total_B = 0
           
    def read_and_display_data(self, file_path, treeview):
        try:
            # Lê o arquivo como um DataFrame do pandas
            df = pd.read_excel(file_path)

            # Adiciona os dados ao Treeview
            for col in df.columns:
                QTD_NOTAS = df.iloc[0:][col].count()  # Conta a quantidade de dados a partir da linha 2
                treeview.insert("", "end", values=(col, QTD_NOTAS))
        except Exception as e:
            # Se ocorrer um erro, exibe uma mensagem
            self.result_text2.insert(tk.END, f"Erro ao ler o arquivo {os.path.basename(file_path)}: {str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    app = ExcelComparerApp(root)  # Cria a aplicação
    
    image_base64 = "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9omIiIiI0onVdQJgbk7waSYE+0REREREmZSVQb6p/mISqsAYaDc/N2za0d8eFtV+TLtdBciMh4RmQDPgO7Gmm9dwBoYz/cxyRRo+2noQEREREaUMPqEZLS1durTp22+/bVq0aFHTF1980fTee+81BaV79+5hqa6urrm7af7ss89UO/4Dmm+//XbVDGgfOHCgasY4dn/T7sU9TdPsZvfDfOx5e3FPN9J6UPb65JNPdBMRUe7hOYyIIKvq5ONXyEzdePOLZKjfjua5c+eqdjj88MN1U8itt96q/ptxTH/TbqZpl/hH4zUcpoHk9d5ApOEh2noQEREREaVCwdTJR9CNqjTmhiLSy7F+hzPiHZ6IiIiIKNWyLsg3QbKpv44gGs2mRDxRKEE308Y0kbxEGg7dkNyf+Yw2PAS9HkREREREsWRlST6q8JiXWfGiK9qTZYJrTPOCCy5oDsIB/cyLt9GGw3LcfvvtzVVz7KA90vBBrwcRERERUSxFeLlWN3tqamqS33//XX777Tf59ddfZfny5bL77rvLOusUTE2fMCiRR8B+3nnnZey7/pRaqHaFGzMiolzEcxgRQcxIvaioSCUDzatWrdJthQcl9TiBmmo5RERERETZJq7ieJTer7vuurJixQrdpfCY6jdlZWW6CxERERFRdolZXQdQXWft2rWyevVq+emnn1RJ/i677CLt2rXTQxARERERUbbwVZJvquygJB+BPUrzv/zyS92XiIiIiIiyie/qOgjwkdq2bSvrrbeerFy5UhobG1XpPhERERERZQ9f1XUAX9lBlR18ZQfVddasWaP+o9tWW20l7du3V8F/oX51h4iIiIgoW/gO8sHUzUegjxJ8BPpoN91wI4BERERERESZE1eQb4J4O7A3gT4REREREWWHuIJ8MIG+KdXHfzsREREREVFmxR3kG3awb/4TEREREVHmJRzkA4J7+z/YzURERERElH5JBfleGOQTEREREWVW4EE+ERERERFlVsJBPj6h+csvv6gv7PDrOpRq+JXlNm3ayIYbbqh+dTke3FeJiIio0CQU5P/888/q05mdO3fmD2BRWuDFbvz42uLFi9WvLm+00Ua6T3TcV4mIiKgQxR3xmB/B6tatm2ywwQYMmigtsJ9hf8N+h30QKRbuq0RERFSo1ikqKpJ40sqVK1WpKJqJ0g37XZcuXdR+aO+XXon7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"
     
        # Decodifique os dados base64
    image_data = base64.b64decode(image_base64)

        # Converta a imagem PNG para o formato RGB
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
        
    image = image.resize((550,350))

        # Carregue a imagem usando o método ImageTk.PhotoImage()
    logo = ImageTk.PhotoImage(image)
    
        # Adicione a imagem ao seu aplicativo
    logo_label = tk.Label(root, image=logo)
    logo_label.grid(row=3, column=4, columnspan=4, padx=10, pady=10, sticky="sw")
        
    x = logo_label.winfo_x()
    y = logo_label.winfo_y()
        
    logo_label.place(x=1190, y=150, width=550, height=350)
        
    plt.imshow(image)
    plt.show
    
    root.update
    root.mainloop()  # Inicia o loop principal da janela
    root.update_idletasks()
