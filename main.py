import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

employee_df = pd.read_csv(r'files/Human_Resources.csv', encoding='utf-8-sig', delimiter=',')

# print(employee_df.head())

##Caracteristicas de los empleados
print(employee_df.info())

## descrip
print(employee_df.describe())

promedio_edad = employee_df['Age'].mean()
print(f'La edad promedio es: {promedio_edad}')

columna_data_entera = employee_df.select_dtypes(include=['int64'])
# print(f'Prueba {columna_data_entera}')

# Contar cuántas hay
num_enteras = len(columna_data_entera.columns)
print(f'Número de columnas con datos enteros: {num_enteras}')

##convertir la columna 'Attrition' a valores numéricos
employee_df['Attrition'] = employee_df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
print(employee_df.head(4))

employee_df['Over18'] = employee_df['Over18'].apply(lambda x: 1 if x == 'Y' else 0)
employee_df['OverTime'] = employee_df['OverTime'].apply(lambda x: 1 if x == 'Yes' else 0)

# print(employee_df.head(5))
# Mostrar las tres columnas
print(employee_df[['Attrition', 'Over18', 'OverTime']].head(5))

#sns.heatmap(employee_df.isnull(), yticklabels=False, cbar=False, cmap="Blues")
#plt.title("Mapa de calor de valores nulos en el DataFrame")
#plt.show()

#Eliminar columnas que no nos interesan porque sus valores son p0racticamnete no cambian o no tiene sentido
employee_df.drop(['EmployeeCount', 'EmployeeNumber', 'StandardHours'], axis=1,inplace=True)


# Histograma de todas las columnas numéricas
employee_df.hist(
    figsize=(18, 12),    # 🔹 Aumenta el tamaño general
    bins=20,             # 🔹 Controla el número de barras
    color='red',         # 🔹 Color del histograma
    edgecolor='black'    # 🔹 Borde negro para contraste
)

plt.suptitle("Distribución de variables numéricas del dataset", fontsize=16)
plt.tight_layout(pad=2.0, rect=[0, 0, 1, 0.96])  # 🔹 Ajuste automático + espacio para el título
plt.show()