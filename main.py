import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

employee_df = pd.read_csv(r'files/Human_Resources.csv', encoding='utf-8-sig',delimiter=',')

#print(employee_df.head())

##Caracteristicas de los empleados
print(employee_df.info())

## descrip
print(employee_df.describe())

promedio_edad = employee_df['Age'].mean()
print(f'La edad promedio es: {promedio_edad}')

columna_data_entera = employee_df.select_dtypes(include=['int64'])
print(f'Prueba {columna_data_entera}')

# Contar cuántas hay
num_enteras = len(columna_data_entera.columns)
print(f'Número de columnas con datos enteros: {num_enteras}')


