import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Cargar los datos desde los archivos CSV por región
df_na = pd.read_csv('NAmatch.csv')
df_eu = pd.read_csv('EUmatch.csv')
df_kr = pd.read_csv('KRmatch.csv')

# Análisis de datos por región
def analyze_data(df):
    # Top 10 Campeones Más Jugados
    campeones_mas_jugados = df['champion'].value_counts().reset_index().head(10)
    campeones_mas_jugados.columns = ['champion', 'cantidad']
    
    # Top 10 Campeones con Más Kills
    top_campeones_kills = df.groupby('champion')['kills'].sum().reset_index().sort_values(by='kills', ascending=False).head(10)
    
    # Porcentaje de Daño a Objetivos por Rol
    daño_objetivos_por_rol = df.groupby('role')['damage_objectives'].sum().reset_index()
    
    # Uso del Flash en D y F
    df['flash'] = df.apply(lambda row: 'D' if row['d_spell'] > row['f_spell'] else 'F', axis=1)
    flash_usage = df['flash'].value_counts().reset_index()
    flash_usage.columns = ['hechizo', 'cantidad']
    
    # Distribución de Roles Más Jugados
    roles_mas_jugados = df['role'].value_counts().reset_index()
    roles_mas_jugados.columns = ['role', 'cantidad']
    
    # Campeones con Más Victorias y Derrotas
    campeones_victorias = df[df['result'] == True]['champion'].value_counts().reset_index().head(10)
    campeones_victorias.columns = ['champion', 'victorias']
    
    campeones_derrotas = df[df['result'] == False]['champion'].value_counts().reset_index().head(10)
    campeones_derrotas.columns = ['champion', 'derrotas']
    
    return {
        'campeones_mas_jugados': campeones_mas_jugados,
        'top_campeones_kills': top_campeones_kills,
        'daño_objetivos_por_rol': daño_objetivos_por_rol,
        'flash_usage': flash_usage,
        'roles_mas_jugados': roles_mas_jugados,
        'campeones_victorias': campeones_victorias,
        'campeones_derrotas': campeones_derrotas
    }

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir las opciones de región para el Dropdown
region_options = [
    {'label': 'NA', 'value': 'NA'},
    {'label': 'EU', 'value': 'EU'},
    {'label': 'KR', 'value': 'KR'}
]

# Definir el layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Análisis de Partidas por Región"),
    
    dcc.Interval(
        id='interval-component',
        interval=60 * 1000,  # Intervalo de actualización en milisegundos (por ejemplo, cada 1 minuto)
        n_intervals=0
    ),
    
    dcc.Dropdown(
        id='region-dropdown',
        options=region_options,
        value='NA',  # Valor predeterminado al iniciar la aplicación
        clearable=False,
        style={'width': '200px', 'margin-bottom': '20px'}
    ),
    
    html.Div(id='region-data-container')  # Contenedor para los gráficos dinámicos
])

# Callback para actualizar los gráficos con los datos correspondientes por región
@app.callback(
    Output('region-data-container', 'children'),
    [Input('region-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_graphs_callback(selected_region, n):
    if selected_region == 'NA':
        data = analyze_data(df_na)
    elif selected_region == 'EU':
        data = analyze_data(df_eu)
    elif selected_region == 'KR':
        data = analyze_data(df_kr)
    else:
        return html.Div("Seleccione una región válida.")
    
    color_sequence = px.colors.qualitative.Pastel  # Secuencia de colores para las barras
    
    return [
        dcc.Graph(figure=px.bar(data['campeones_mas_jugados'], x='champion', y='cantidad', title=f'Top 10 Campeones Más Jugados ({selected_region})', color='champion', color_discrete_sequence=color_sequence)),
        dcc.Graph(figure=px.bar(data['top_campeones_kills'], x='champion', y='kills', title=f'Top 10 Campeones con Más Kills ({selected_region})', color='champion', color_discrete_sequence=color_sequence)),
        dcc.Graph(figure=px.bar(data['daño_objetivos_por_rol'], x='role', y='damage_objectives', title=f'Porcentaje de Daño a Objetivos por Rol ({selected_region})', color='role', color_discrete_sequence=color_sequence)),
        dcc.Graph(figure=px.pie(data['flash_usage'], values='cantidad', names='hechizo', title=f'Uso del Flash en D y F ({selected_region})')),
        dcc.Graph(figure=px.bar(data['roles_mas_jugados'], x='role', y='cantidad', title=f'Distribución de Roles Más Jugados ({selected_region})', color='role', color_discrete_sequence=color_sequence)),
        dcc.Graph(figure=px.bar(data['campeones_victorias'], x='champion', y='victorias', title=f'Campeones con Más Victorias ({selected_region})', color='champion', color_discrete_sequence=color_sequence)),
        dcc.Graph(figure=px.bar(data['campeones_derrotas'], x='champion', y='derrotas', title=f'Campeones con Más Derrotas ({selected_region})', color='champion', color_discrete_sequence=color_sequence))
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
