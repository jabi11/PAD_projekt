# %%
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
# df.info()
df.columns = df.columns.str.strip()
numeric_columns = ['x dimension', 'y dimension', 'z dimension', 'depth', 'price', 'table']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
df['clarity'] = df['clarity'].astype("string")
df['clarity'] = df['clarity'].str.upper()
df['color'] = df['color'].astype("string")
df['color'] = df['color'].str.upper()
df['cut'] = df['cut'].astype("string")
df['cut'] = df['cut'].str.upper()
df = df.sort_values("price")
df['carat'].fillna(method='ffill', inplace=True)
df['price'].fillna(method='ffill', inplace=True)
df['table'].fillna(method='bfill', inplace=True)
# df = df.dropna(axis=0, subset=['x dimension', 'y dimension', 'z dimension', 'depth', 'price'])
# df['price'] = df['price'].astype("int64")
df.info()
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

selected_column = st.selectbox("Wybierz kolumnę do wyświetlenia", df.columns)

st.subheader(f"Liczba wystąpień w podziale na {selected_column}")
how_many_of_each_column = df[selected_column].value_counts()
how_many_of_each_column.plot(kind='bar', color='skyblue', edgecolor='black')
st.bar_chart(how_many_of_each_column)

selected_column_x = st.selectbox("Wybierz kolumnę do wyświetlenia na osi x", df.columns)
selected_column_y = st.selectbox("Wybierz kolumnę do wyświetlenia na osi y", df.columns)

st.subheader(f"Histogram {selected_column_x} do {selected_column_y}")
st.scatter_chart(data=df,x=selected_column_x, y=selected_column_y)

st.subheader("Wykres regresji price do wybranej zmiennej")
selected_column_reg = st.selectbox("Wybierz zmienną do wyświetlenia na osi y", df.columns)

fig, ax = plt.subplots()
sns.regplot(data=df, x="price", y=selected_column_reg, ax=ax)
st.pyplot(fig)
