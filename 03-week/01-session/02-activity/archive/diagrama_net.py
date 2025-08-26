import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("Netflix Dataset.csv")

# Mostrar las primeras filas para verificar
print(df.head())

# ----------------------
# 1. Conteo de Películas vs Series
# ----------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x="Type", palette="Set2")
plt.title("Cantidad de Películas vs Series en Netflix")
plt.xlabel("Tipo de contenido")
plt.ylabel("Cantidad")
plt.show()

# ----------------------
# 2. Contenido agregado por año
# ----------------------
plt.figure(figsize=(10,5))
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
sns.countplot(data=df, x="release_year", palette="mako", order=df['release_year'].value_counts().index.sort_values())
plt.title("Cantidad de títulos lanzados por año")
plt.xlabel("Año de lanzamiento")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.show()

# ----------------------
# 3. Top 10 países con más títulos
# ----------------------
plt.figure(figsize=(10,5))
df['country'] = df['country'].fillna("Desconocido")
top_paises = df['country'].value_counts().head(10)
sns.barplot(x=top_paises.values, y=top_paises.index, palette="viridis")
plt.title("Top 10 países con más títulos en Netflix")
plt.xlabel("Cantidad de títulos")
plt.ylabel("País")
plt.show()
