import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Obtener campeones con más victorias
campeones_victorias = df[df['result'] == True]['champion'].value_counts().reset_index().head(10)
campeones_victorias.columns = ['champion', 'victorias']

# Obtener campeones con más derrotas
campeones_derrotas = df[df['result'] == False]['champion'].value_counts().reset_index().head(10)
campeones_derrotas.columns = ['champion', 'derrotas']

# Asignar colores distintos a cada campeón
colores_victorias = px.colors.qualitative.Set1[:10]
colores_derrotas = px.colors.qualitative.Dark24[:10]

# Crear el gráfico de barras para campeones con más victorias
fig_victorias = px.bar(campeones_victorias, x='champion', y='victorias', title='Campeones con Más Victorias',
                    color='champion', color_discrete_sequence=colores_victorias)
fig_victorias.show()

# Crear el gráfico de barras para campeones con más derrotas
fig_derrotas = px.bar(campeones_derrotas, x='champion', y='derrotas', title='Campeones con Más Derrotas',
                    color='champion', color_discrete_sequence=colores_derrotas)
fig_derrotas.show()
