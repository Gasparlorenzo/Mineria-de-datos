import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Crear DataFrame
datos = {
    "Cliente": [1, 2, 3, 4, 5],
    "Edad": [25, 40, 32, 22, 35],
    "Plan": ["Básico", "Premium", "Estándar", "Básico", "Premium"],
    "Consumo_GB": [5, 50, 10, 7, 45],
    "Reclamos": [1, 0, 2, 3, 0],
    "Estado_Cuenta": ["Pagado", "Pagado", "Moroso", "Moroso", "Pagado"]
}
df = pd.DataFrame(datos)
# Inspeccionar los datos
print(df.info())
print(df.describe())
# Ver distribución de consumo de datos
sns.histplot(df["Consumo_GB"], bins=5, kde=True)
plt.show()
# Gráfico de barras de Estado de Cuenta
sns.countplot(x=df["Estado_Cuenta"])
plt.show()


"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Crear DataFrame
datos = {
    "Cliente": [1, 2, 3, 4, 5],
    "Edad": [25, 40, 32, 22, 35],
    "Plan": ["Básico", "Premium", "Estándar", "Básico", "Premium"],
    "Consumo_GB": [5, 50, 10, 7, 45],
    "Reclamos": [1, 0, 2, 3, 0],
    "Estado_Cuenta": ["Pagado", "Pagado", "Moroso", "Moroso", "Pagado"]
}
df = pd.DataFrame(datos)
# Ver datos
print("Información del DataFrame:")
print(df.info())

print("\nValores faltantes:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

print("\nEstadísticas descriptivas:")
print(df.describe())

# Histograma de consumo
sns.histplot(df["Consumo_GB"], bins=5, kde=True)
plt.title("Distribución del Consumo de Datos")
plt.xlabel("Consumo (GB)")
plt.ylabel("Frecuencia")
plt.show()

# Gráfico de barras de Estado de Cuenta
sns.countplot(x=df["Estado_Cuenta"])
plt.title("Estado de Cuenta")
plt.xlabel("Estado")
plt.ylabel("Cantidad de clientes")
plt.show()

# Gráfico de dispersión
sns.scatterplot(x=df["Consumo_GB"], y=df["Reclamos"])
plt.title("Consumo de Datos vs Reclamos")
plt.xlabel("Consumo (GB)")
plt.ylabel("Reclamos")
plt.show()
"""

