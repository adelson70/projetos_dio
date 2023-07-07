import pandas as pd
import matplotlib.pyplot as plt 

df1 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Aracaju.xlsx")
df2 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Natal.xlsx")
df4 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Recife.xlsx")
df5 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Salvador.xlsx")

# .concat - JUNTA TODOS OS ARQUIVOS NUM SÓ
df = pd.concat([df1,df2,df3,df4,df5])

df["Receita"] = df["Vendas"]*df["Qtde"]

# CRIAR UMA COLUNA DE ANO_VENDA NO DATASET
df["Ano_Venda"] = df["Data"].dt.year # dt.year - IRA PUXAR APENAS O ANO DA DATA

# CRIA UMA COLUNA DE VENDA POR MES NO DATASET
df["Mes_Venda"] = df["Data"].dt.month

# CRIA UMA COLUNA DE VENDA POR DIA NO DATASET
df["Dia_Venda"] = df["Data"].dt.day

# CALCULA A DIFERENÇA ENTRE 2 DATAS INFORMADAS
df["Diferença_dias"] = df["Data"]-df["Data"].min() # NESTE CASO AS DATAS SERÃO SUBTRAIDAS DA DATA MAIS ANTIGA

# CRIA UMA COLUNA QUE RETORNA O TRIMESTE EM RELAÇÃO A DATA
df["Trimestre_Vendas"] = df["Data"].dt.quarter #.quarter - IRA RETORNAR O TRIMESTRE DA DATA

# value_counts - TRAS A QUANTIDADE TOTAL DE LINHAS QUE UM DETERMINADO VALOR TEM
quantidade_vendas_por_loja = df["LojaID"].value_counts(ascending=False)
print(quantidade_vendas_por_loja)

# plot.bar() - IMPRIME UM GRAFICO DE BARRAS
grafico_barras_vertical = quantidade_vendas_por_loja.plot.bar()
plt.show() # USANDO BIBLIOTECA MATPLOT PARA IMPRIMIR O GRAFICO

# plot.barh() - IMPRIME UM GRAFICO DE BARRAS HORIZONTAIS
grafico_barras_horizontal = quantidade_vendas_por_loja.plot.barh()
plt.show() # USANDO A BIBLIOTECA MATPLOT PARA IMPRIMIR O GRAFICO 

# plot.pie() - IMPRIME UM GRAFICO DE PIZZA
venda_total_por_ano = df.groupby(df["Ano_Venda"])["Receita"].sum().plot.pie()
plt.show()

# ADICIONANDO TITULOS E LEGENDA AO GRAFICO
# NESTE CASO O TOTAL DE VENDAS POR CIDADE
total_vendas_por_cidade = df["Cidade"].value_counts().plot.bar(title="Total Vendas Por Cidade",color="Red")
plt.xlabel("Cidade") # Eixo X receberá esse nome
plt.ylabel("Total de Vendas") # Eixo Y receberá esse nome
plt.show()

# GRAFICO DE LINHA COM LEGENDA
total_produtos_vendidos_por_mes = df.groupby(df["Mes_Venda"])["Qtde"].sum().plot(title="Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Venda Total")
plt.legend() # CRIA UMA LEGENDA PRO GRAFICO
plt.show()

# SELECIONANDO APENAS AS VENDAS DO ANO 2019
df_2019 = df[df["Ano_Venda"] == 2019]
# TOTAL DE PRODUTOS VENDIDOS POR MÊS DO ANO 2019
total_vendas_por_mes_2019 = df_2019.groupby(df_2019["Mes_Venda"])["Qtde"].sum().plot(title="Vendas de 2019 por Mês",marker="o")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.legend()
plt.show()

# plt.hist - GRAFICO HISTOGRAMA
histograma = plt.hist(df["Qtde"],color="blue")
plt.show()


# plt.scatter - GRAFICO DE DISPERSÃO
grafico_dispersao = plt.scatter(x = df_2019["Dia_Venda"], y = df_2019["Receita"])
plt.xlabel("Dia do Mês")
plt.ylabel("Receita do Dia")
plt.show()

# plt.savefig("titulo.png") - SALVA O GRAFICO EM IMAGEM
grafico_pizza = df.groupby(df["Ano_Venda"])["Receita"].sum().plot.pie()
plt.legend()
plt.savefig("Receita por ano.png")