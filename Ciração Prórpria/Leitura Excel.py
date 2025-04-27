import pandas as pd

# Lê o arquivo Excel
ler = pd.read_excel(r"C:\Teste\Produto.xlsx",
                    sheet_name='Planilha1', header=None)

# Cria o DataFrame
df = pd.DataFrame({
    'SKU': ler.iloc[:, 1],
    'NOME': ler.iloc[:, 2],
    'VENDA': ler.iloc[:, 3]
})

# Agrupa por SKU e calcula totais
resumo = df.groupby('SKU').agg(
    Total_Vendas=('VENDA', 'sum'),
    Contagem=('VENDA', 'count'),
    Nomes=('NOME', lambda x: ', '.join(x.unique()))
).reset_index()

# Nome do arquivo de saída
nome_arquivo = r"C:\Teste\Relatorio.txt"

# Escreve os resultados no arquivo .txt
with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write("RELATÓRIO DE VENDAS POR SKU\n")
    arquivo.write("=============================================\n\n")

    for index, row in resumo.iterrows():
        sku = row['SKU']
        total = row['Total_Vendas']
        contagem = row['Contagem']
        nomes = row['Nomes']

        # Escreve no arquivo
        arquivo.write(f"SKU: {sku}\n")
        arquivo.write(f"  > Nomes associados: {nomes}\n")
        arquivo.write(f"  > Total de Vendas: {total}\n")
        arquivo.write(f"  > Ocorrências: {contagem}\n")
        arquivo.write("-" * 50 + "\n")  # Linha separadora

print(f"Relatório salvo em: {nome_arquivo}")
