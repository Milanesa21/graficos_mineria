import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('EUmatch.csv')

# Sumar el daño a objetivos por rol
daño_objetivos_por_rol = df.groupby('role')['damage_objectives'].sum().reset_index()

# Asignar colores distintos a cada rol
colores_roles = px.colors.qualitative.Set1[:len(daño_objetivos_por_rol)]

# Crear el gráfico de torta para daño a objetivos por rol
fig_objetivos = px.pie(daño_objetivos_por_rol, values='damage_objectives', names='role',
                    title='Porcentaje de Daño a Objetivos por Rol', color='role', color_discrete_sequence=colores_roles)
fig_objetivos.show()