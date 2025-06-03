# Escreva o seu código aqui :-)
import streamlit as st #impotando a biblioteca que faz tudo no navegador
import pandas as pd #importando a biblioteca e apelidando
import plotly.express as px #importando bibliotega que faz graficos

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("datasets/customer_reviews.csv") #ler o arquivo que ta nesse diretorio, lembrando que ele comeca a ler da pasta que esse proprio documento ta salvo
df_top100_books = pd.read_csv("datasets/Top-100 Trending Books.csv") #df de DataFrame, que eh o tipo do arquivo - uma tabela

#df_reviews ja escreve na pagina a tabela, sem precisar do write

price_max = df_top100_books["book price"].max() # procura o maior valor sreamlit
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max,price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

fig = px.bar(df_top100_books["year of publication"].value_counts())
#esse comando px.baar escolhe o grafico de barras das biblioteca plotly
#e poe num grafico quantos livros tem publicados por anos value.couns(conta) por anos
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2) #cria duas colunas pra textos e imagens
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
