# %%
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
df = pd.read_csv('messy_data.csv')

# %%
# df

# %%
# a. Usunięcie duplikatów
df = df.drop_duplicates()
# df

# %%
df = df.dropna()
# df


# %%
df.info()
df.columns = df.columns.str.strip()
numeric_columns = ['x dimension', 'y dimension', 'z dimension', 'depth', 'price', 'table']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
df['clarity'] = df['clarity'].astype("string")
df['clarity'] = df['clarity'].str.upper()
df['color'] = df['color'].astype("string")
df['cut'] = df['cut'].astype("string")
df['cut'] = df['cut'].str.upper()
df = df.dropna(axis=0, subset=['x dimension', 'y dimension', 'z dimension', 'depth', 'price'])
df['price'] = df['price'].astype("int64")
# df.info()
# df

# %%
df = df.drop('table', axis=1)
# df

# %%
# wartosci odstajace na carat
q_low = df["carat"].quantile(0.01)
q_hi  = df["carat"].quantile(0.99)
print(q_low)
print(q_hi)
df = df[(df["carat"] < q_hi) & (df["carat"] > q_low)]
# df

# %%
#kolumna cut jako categorical
df['cut'] = df.cut.astype('category')
df['cut'].describe()

# %%
# df.info()
# df

st.header("PAD Projekt")
st.dataframe(df)

st.subheader("Liczba wystąpień w podziale na cięcie")
how_many_of_each_cut = df['cut'].value_counts()
how_many_of_each_cut.plot(kind='bar', color='skyblue', edgecolor='black')
st.bar_chart(how_many_of_each_cut)

st.subheader("Liczba wystąpień w podziale na przejzystosc")
how_many_of_each_clarity = df['clarity'].value_counts()
how_many_of_each_clarity.plot(kind='bar', color='skyblue', edgecolor='black')
st.bar_chart(how_many_of_each_clarity)