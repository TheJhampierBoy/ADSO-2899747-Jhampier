import pandas as pd
import matplotlib.pyplot as plt

# Carga el dataset (debe estar en la misma carpeta que este script)
df = pd.read_csv("StressLevelDataset.csv")

# Asegurar el nombre de columna correcto
df.columns = [c.strip() for c in df.columns]
col = "stress_level" if "stress_level" in df.columns else df.columns[0]

# Contar niveles de estrés
counts = df[col].value_counts().sort_index()

# Gráfico de barras
plt.figure(figsize=(8, 5))
plt.bar(counts.index.astype(str), counts.values)
plt.xlabel("Nivel de Estrés")
plt.ylabel("Cantidad de Estudiantes")
plt.title("Distribución de Niveles de Estrés")

for i, v in enumerate(counts.values):
    plt.text(i, v, str(int(v)), ha="center", va="bottom", fontweight="bold")

plt.tight_layout()
plt.savefig("stress_distribution.png", dpi=150)
plt.show()
