import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Contar la frecuencia de cada rol
roles_mas_jugados = df['role'].value_counts().reset_index()
roles_mas_jugados.columns = ['role', 'cantidad']

# Crear el gráfico de torta
fig = px.pie(roles_mas_jugados, values='cantidad', names='role', title='Distribución de Roles Más Jugados')
fig.show()
