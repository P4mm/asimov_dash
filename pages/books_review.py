import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Use caminhos relativos para os arquivos no ambiente virtual
df_reviews = pd.read_csv(r"C:\Users\User\Desktop\asimov_dash\customer_reviews.csv")

# Forneça o caminho absoluto para o arquivo com espaços
df_top100_books = pd.read_csv(r"C:\Users\User\Desktop\asimov_dash\Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

#df_book
#df_reviews_f

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

# Divider with custom color
divider_color = "#4BFF51"
st.markdown(
    f'<div style="border-top: 2px solid {divider_color};"></div>',
    unsafe_allow_html=True
)

for row in df_reviews_f.values:
  message = st.chat_message(f"{row[4]}")
  message.write(f"**{row[2]}**")
  message.write(row[5])