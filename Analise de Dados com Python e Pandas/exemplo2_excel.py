import pandas as pd

df1 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Aracaju.xlsx")
df2 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Fortaleza.xlsx")
df3 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Natal.xlsx")
df4 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Recife.xlsx")
df5 = pd.read_excel("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Salvador.xlsx")

# .concat - JUNTA TODOS OS ARQUIVOS NUM SÓ
df = pd.concat([df1,df2,df3,df4,df5])

# .sample - IRA RETORNAR UMA AMOSTRA ALEATORIA
print(df.sample(5)) # PARAMETRO 5 IRA RETORNAR 5 AMOSTRAS ALEATORIAS
print()

# .astype(AQUI O NOVO TIPO DE VALOR) - ALTERA O TIPO DE VALOR DA COLUNA
df["LojaID"] = df["LojaID"].astype("object")

print(df.dtypes)
print()

# .isnull().sum()- IRA RETORNAR A QUANTIDADE DE LINHAS QUE POSSUI VALOR NULO
print(df.isnull().sum())

# .fillna - SUBSTITUI OS VALORES NULOS POR 0
df["Vendas"].fillna(0, inplace=True) #inplace = True substitui na memoria (importante!)


# .dropna() - IRA APAGAR AS LINHAS COM VALORES NULOS
df.dropna(inplace=True) # NÃO PRECISA ESPECIFICAR A COLUNA MAS SIM O DATASET

# dropna(subset=["Vendas"]) - IRA APAGAR OS VALORES NULOS DE UMA COLUNA ESPECIFICA
df.dropna(subset=["Vendas"],inplace=True)

# dropna(how="all") - IRA REMOVER TODAS AS LINHAS QUE TIVEREM ALGUM VALOR FALTANTE
df.dropna(how="all",inplace=True)

# CRIANDO UMA NOVA COLUNA - EX: Receitas = quantidade de vendas X preço
df["Receita"] = df["Vendas"]*df["Qtde"]
print(df.head())

# IRA RETORNAR O MAIOR VALOR DA COLUNA ESPECIFICADA
# NESTE CASO SERA A COLUNA RECEITA
maior_receita = df["Receita"].max()
print(maior_receita)

# IRA RETORNAR O MENOR VALOR DA COLUNA ESPECIFICADA
# NESTE CASO SERA A COLUNA RECEITA
menor_receita = df["Receita"].min()
print(menor_receita)

# nlargest(quantidade de linhas,coluna de referencia) - IRA RETORNAR UM RANKING DE MAIOR VALOR
# COM BASE NA QUANTIDADE DE LINHAS SOLICITADAS
# E A COLUNA ESPECIFICADA SERA A REFERENCIA PARA ESSE RANKING
ranking_maior_receita = df.nlargest(3,"Receita")
print(ranking_maior_receita)
print() #só para ter um espaço


# nsmallest(quantidade de linhas,coluna de referencia) - IRA RETORNAR UM RANKING DE MENOR VALOR
# COM BASE NA QUANTIDADE DE LINHAS SOLICITADAS
# E A COLUNA ESPECIFICADA SERA A REFERENCIA PARA ESSE RANKING
ranking_menor_receita = df.nsmallest(3,"Receita")
print(ranking_menor_receita)

#groupby - AGRUPA OS DADOS DAS COLUNAS ESPECIFICADAS
receita_total_por_cidade = df.groupby("Cidade")["Receita"].sum()
print(receita_total_por_cidade)