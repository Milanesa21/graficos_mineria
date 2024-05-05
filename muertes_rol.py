import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Sumar las muertes por rol
muertes_por_rol = df.groupby('role')['deaths'].sum().reset_index()

# Crear el gráfico de torta
fig = px.pie(muertes_por_rol, values='deaths', names='role', title='Porcentaje de Muertes por Rol')
fig.show()
