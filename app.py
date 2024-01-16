import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Use caminhos relativos para os arquivos no ambiente virtual
df_reviews = pd.read_csv(r"C:\Users\User\Desktop\asimov_dash\customer_reviews.csv")

# Forneça o caminho absoluto para o arquivo com espaços
df_top100_books = pd.read_csv(r"C:\Users\User\Desktop\asimov_dash\Top-100 Trending Books.csv")

price_max = float(df_top100_books["book price"].max())
price_min = float(df_top100_books["book price"].min())

# Adicione um controle deslizante para ajustar o preço máximo
max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max, step=1.0)

# Filtrar os livros pelo preço máximo
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

# Filtrar anos futuros
current_year = pd.to_datetime("now").year
df_books = df_books[df_books["year of publication"] <= current_year]

# Ajuste da largura do gráfico
fig_width = 600

# Crie um gráfico de barras interativo com Plotly Express
fig = px.bar(df_books["year of publication"].value_counts(), x=df_books["year of publication"].value_counts().index, y=df_books["year of publication"].value_counts().values, labels={"x": "Ano de Publicação", "y": "Contagem"}, width=fig_width)
fig2 = px.histogram(df_books["book price"], width=fig_width)

# Exibir as informações geradas
st.write("Informações do Top 100:")

# Ajuste da largura da tabela
st.dataframe(df_books.style.set_table_styles([{'selector': 'table', 'props': [('max-width', f'{fig_width}px')]}]))

# Adicionar localhost para visualizar no navegador
st.balloons()

# Adicionar os gráficos lado a lado
col1, col2 = st.columns(2)

# Adicionar o gráfico na primeira coluna
with col1:
    st.write("Gráfico de Ano de Publicação:")
    st.plotly_chart(fig)

# Adicionar o gráfico histograma na segunda coluna
with col2:
    st.write("Gráfico de Preço:")
    st.plotly_chart(fig2)

# Adicionar localhost para visualizar no navegador
# st.title("Visualização de Dados com Streamlit")
# Pode usar st.table para mostrar o DataFrame em uma tabela interativa
# st.table(df_reviews)

# Adicionar localhost
# st.button("Clique aqui para abrir no navegador")
