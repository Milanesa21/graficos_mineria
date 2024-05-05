import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Contar la frecuencia de cada campeón
campeones_mas_jugados = df['champion'].value_counts().reset_index()
campeones_mas_jugados.columns = ['champion', 'cantidad']

# Ordenar por cantidad de veces jugado y tomar los primeros 10
campeones_mas_jugados = campeones_mas_jugados.sort_values(by='cantidad', ascending=False).head(10)

# Asignar colores distintos a cada campeón
colores = px.colors.qualitative.Plotly[:10]

# Crear el gráfico de barras con colores distintos
fig = px.bar(campeones_mas_jugados, x='champion', y='cantidad', title='Top 10 de Campeones Más Jugados',
            color='champion', color_discrete_sequence=colores)
fig.show()
