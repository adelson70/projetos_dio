import pandas as pd

# VARIAVEL RECEBE UM ARQUIVO CSV COM SEPERADOR ; (PONTO E VIRGULA)
df = pd.read_csv("C:/Users/BITTE/OneDrive/Documentos/Programador/Linguagens/Python_Estudos/programinhas/Pandas/datasets/Gapminder.csv",sep=";")

# RENOMEIA AS COLUNAS
df = df.rename(columns={"country":"Pais","continent":"Continente","year":"Ano",\
                        "lifeExp":"Expectativa de Vida","pop":"Populção","gdpPercap":"PIB",})

# .head IMPRIME A TABELA
print(df.head())

# .shape INFORMA A QUANTIDADE DE LINHAS E COLUNAS DA TABELA
print(df.shape)

# .dtypes INFORMA O TIPO DE CADA COLUNA
print(df.dtypes)

# .tail() IMPRIME AS ULTIMAS LINHAS DA TABELA
print(df.tail())

# .describe() RETORNA UMA ESTATISTICA DA TABELA
print(df.describe())

# .unique() RETORNA OS VALORES UNICOS DA COLUNA ESPECIFICADA
print(df["Continente"].unique())

# FILTRO DE DADOS
# .loc IRA RETORNAR O CONTINENTE ESPECIFICADO DENTRO DA COLUNA ESPECIFICADA
oceania = df.loc[df["Continente"] == "Oceania"]
print(oceania.head())

# . gorupby AGRUPA POR UM PARAMETRO ESPECIFICADO
# NESTE CASO A QUANTIDADE DE PAISES POR CONTINENTE
# .nunique() FAZ A CONTAGEM
contagem_paieses = df.groupby("Continente")["Pais"].nunique()
print(contagem_paieses)

# .mean FAZ A MEDIA
# USANDO AINDA .groupby para agrupar os dados
media_vida_por_ano = df.groupby("Ano")["Expectativa de Vida"].mean()
print(media_vida_por_ano)

