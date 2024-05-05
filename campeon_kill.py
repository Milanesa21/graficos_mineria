import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Agrupar por campeón y sumar las kills
kills_por_campeon = df.groupby('champion')['kills'].sum().reset_index()

# Ordenar por cantidad de kills y tomar los primeros 10
top_campeones_kills = kills_por_campeon.sort_values(by='kills', ascending=False).head(10)

# Asignar colores distintos a cada campeón
colores = px.colors.qualitative.Plotly[:10]

# Crear el gráfico de barras con colores distintos
fig = px.bar(top_campeones_kills, x='champion', y='kills', title='Top 10 de Campeones con Más Kills',
            color='champion', color_discrete_sequence=colores)
fig.show()
