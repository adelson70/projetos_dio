# ANALISE EXPLORATORIA
import pandas as pd
import matplotlib.pyplot as plt 
plt.style.use("seaborn")
pd.options.display.float_format = "{:20,.2f}".format

df = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/AdventureWorks.xlsx")

# VERIFICAR OS TIPOS DE DADOS
print(df.dtypes)

# VISUALIZA DADOS ALEATORIOS
#print(df.sample(15))

# CRIA UMA NOVA COLUNA DE NOME "Custo"
df["Custo"] = df["Custo Unitário"]*df["Quantidade"]
#print(df.sample())

# CRIA UMA NOVA COLUNA DE NOME "Lucro"
df["Lucro"] = df["Valor Venda"]-df["Custo"]
print(df.sample(10))
print()

# CRIA UMA NOVA COLUNA DE NOME "Tempo de Envio"
df["Tempo Envio"] = (df["Data Envio"]-df["Data Venda"]).dt.days
print(df.sample(5))
print()

# DESCOBRIR A MÉDIA DE ENVIO POR MARCA
media_envio_por_marca = df.groupby(df["Marca"])["Tempo Envio"].mean()
print(media_envio_por_marca)
print()

# DESCOBRIR O LUCRO TOTAL POR MARCA
lucro_total_por_marca = df.groupby(df["Marca"])["Lucro"].sum()
print(lucro_total_por_marca)
print()

# AGRUPANDO POR ANO E POR MARCA
lucro_por_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
print(lucro_por_ano)
print()

# VERIFICAÇÃO PARA VER SE TEM VALORES AUSENTES EM ALGUMA COLUNA E LINHA
valores_ausentes = df.isnull().sum()
print(valores_ausentes)
print()

# VERIFICAR O TOTAL DE PRODUTOS VENDIDOS USANDO groupby
# AGRUPANDO POR PRODUTO
total_produtos_vendidos = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True)
# IMPRIMINDO UM GRAFICO DE BARRAS HORIZONTAIS COM AS INFOS A CIMA
total_produtos_vendidos.plot.barh()
plt.xlabel("Quantidade de Produtos Vendidos")
plt.ylabel("Marca do Produto")
plt.show()
print(total_produtos_vendidos)
print()

# IMPRIME UM GRAFICO DE BARRAS VERTICAIS PARA SABER O LUCRO POR ANO
lucro_ao_ano = df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()
lucro_ao_ano.plot.bar(title="Lucro por Ano")
plt.xlabel("Ano")
plt.ylabel("Lucro")
plt.show()
print()

# CRIANDO UM DF COM APENAS AS VENDAS DE 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]
print(df_2009)
print()

# GRAFICO DE BARRA HORIZONTAL AGRUPANDO POR MARCA E SEU RESPECTIVO VALOR TOTAL
df_2009_venda = df.groupby(df["Marca"])["Valor Venda"].sum().sort_values(ascending=False)
print(df_2009_venda)
df_2009_venda.sort_values(ascending=True).plot.barh(title="Total de Venda Por Marca em 2009")
plt.xlabel("Valor Total")
plt.ylabel("Marca")
plt.show()
print()

# GRAFICO DE LINHAS COM LUCRO POR MES DO ANO DE 2009
lucro_ao_mes_2009 = df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum()
lucro_ao_mes_2009.plot(title="Lucro x Mês")
plt.legend()
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()
print()

# GRAFICO DE BARRAS VERTICAIS PARA LUCRO POR MARCA DO ANO DE 2009
lucro_2009 = df_2009.groupby(df_2009["Marca"])["Lucro"].sum()
lucro_2009.plot.bar(title="Lucro Total de 2009 Por Ano")
plt.legend()
plt.xlabel("Marca")
plt.xticks(rotation="horizontal") # DEIXA O TEXTO NA HORIZONTAL DO EIXO X
plt.ylabel("Lucro")
plt.show()
print()

# IMPRIME UM GRAFICO DE BARRAS VERTICAL PARA LUCRO POR CLASSE DO ANO DE 2009
lucro_por_classe = df_2009.groupby(df_2009["Classe"])["Lucro"].sum()
lucro_por_classe.plot.bar(title="Lucro por Classe do Ano de 2009")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation="horizontal")
plt.show()
print()

# USANDO describe - PARA FAZER ANALISES ESTATISTICAS
estatistica_tempo_envio = df["Tempo Envio"].describe()
print(estatistica_tempo_envio)

# IMPRIMINDO GRAFICO DE BOXPLOT PARA VERIFICAR O TEMPO DE ENVIO
plt.boxplot(df["Tempo Envio"])
plt.show()
print()

# IDENTIFICANDO O OUTLIER (VALOR MUITO ALTO FORA DO PADRÃO)
maior_tempo_envio = df["Tempo Envio"].max() # DESCOBRINDO QUAL É O MAIOR TEMPO DE ENVIO
# FILTRANDO PARA SABER QUAL FOI O PRODUTO COM MAIOR TEMPO DE ENVIO
outlier = df[df["Tempo Envio"] == maior_tempo_envio] 
print(outlier)

# CRIAR UM NOVO ARQUIVO COM AS NOVAS INFORMAÇÕES CRIADAS
df.to_csv("Novo_csv.csv",index=False) # DEIXAR INDEX FALSE PARA ELE NÃO LEVAR PARA A PLANINHA