import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('KRmatch.csv')

# Crear una nueva columna para identificar qué hechizo es el flash
df['flash'] = df.apply(lambda row: 'D' if row['d_spell'] > row['f_spell'] else 'F', axis=1)

# Contar la cantidad de veces que se usa el flash en D y F
flash_usage = df['flash'].value_counts().reset_index()
flash_usage.columns = ['hechizo', 'cantidad']

# Crear el gráfico de torta
fig = px.pie(flash_usage, values='cantidad', names='hechizo', title='Uso del Flash en D y F')
fig.show()
