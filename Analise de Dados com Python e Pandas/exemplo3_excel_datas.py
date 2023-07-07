import pandas as pd

df1 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Aracaju.xlsx")
df2 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Natal.xlsx")
df4 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Recife.xlsx")
df5 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Salvador.xlsx")

# .concat - JUNTA TODOS OS ARQUIVOS NUM SÓ
df = pd.concat([df1,df2,df3,df4,df5])

df["Receita"] = df["Vendas"]*df["Qtde"]

# TRANSFORMA O DATA EM NUMERO INTEIRO
df["Data"] = df["Data"].astype("int64")
print(df.head())

# TRANSFORMA A COLUNA DE DATA(INT) EM DATA(DATA)
df["Data"] = pd.to_datetime(df["Data"])
print(df.head())

# RETORNA A RECEITA TOTAL POR ANO - .dt = date time
receita_por_ano = df.groupby(df["Data"].dt.year)["Receita"].sum()
print(receita_por_ano)

# CRIAR UMA COLUNA DE ANO_VENDA NO DATASET
df["Ano_Venda"] = df["Data"].dt.year # dt.year - IRA PUXAR APENAS O ANO DA DATA
print(df.head())

# METODO PARA RETORNAR A DATA MAIS ANTIGA DO CONJUNTO DE DADOS
data_antiga = df["Data"].min()
print(data_antiga)

# CALCULA A DIFERENÇA ENTRE 2 DATAS INFORMADAS
df["Diferença_dias"] = df["Data"]-df["Data"].min() # NESTE CASO AS DATAS SERÃO SUBTRAIDAS DA DATA MAIS ANTIGA
print(df.sample(10))

# CRIA UMA COLUNA QUE RETORNA O TRIMESTE EM RELAÇÃO A DATA
df["Trimestre_Vendas"] = df["Data"].dt.quarter #.quarter - IRA RETORNAR O TRIMESTRE DA DATA
print(df.sample(10))

# FILTRAR DADOS USANDO .loc
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print("Vendas de Março de 2019")
print(vendas_marco_19.sample(10))

# value_counts - TRAS A QUANTIDADE TOTAL DE LINHAS QUE UM DETERMINADO VALOR TEM
quantidade_vendas_por_loja = df["LojaID"].value_counts(ascending=False)
print(quantidade_vendas_por_loja)