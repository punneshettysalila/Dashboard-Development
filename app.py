import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# Load and preprocess dataset
df = pd.read_csv("data/Rainfall_Data_LL.csv")

# Melt the monthly columns into long format
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

# Convert to long format for better visualization
df_melted = df.melt(id_vars=['SUBDIVISION', 'YEAR'],
                    value_vars=months,
                    var_name='Month',
                    value_name='Rainfall_mm')

# Clean and format
df_melted.dropna(inplace=True)
df_melted.columns = ['Subdivision', 'Year', 'Month', 'Rainfall_mm']
df_melted['Month'] = df_melted['Month'].str.capitalize()
df_melted['Year'] = df_melted['Year'].astype(int)

# Initialize Dash app with Bootstrap for styling
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "India Rainfall Dashboard"

# App layout
app.layout = html.Div([
    html.H1("India Rainfall Analysis (1901–2017)", style={'textAlign': 'center', 'fontFamily': 'Times new Roman'}),

    html.Div([
        html.Div([
            html.Label("Select Subdivision:"),
            dcc.Dropdown(
                id='subdivision-dropdown',
                options=[{'label': s, 'value': s} for s in sorted(df_melted['Subdivision'].unique())],
                value='ANDAMAN & NICOBAR'
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            html.Label("Select Year Range:"),
            dcc.RangeSlider(
                id='year-range-slider',
                min=df_melted['Year'].min(),
                max=df_melted['Year'].max(),
                step=1,
                marks={str(year): str(year) for year in range(df_melted['Year'].min(), df_melted['Year'].max(), 10)},
                value=[2000, 2017]
            )
        ], style={'width': '48%', 'float': 'right'})
    ], style={'padding': '20px'}),

    html.Div(id='average-indicator', style={'textAlign': 'center', 'fontSize': '20px', 'fontWeight': 'bold'}),

    dcc.Graph(id='rainfall-bar-chart'),
    dcc.Graph(id='rainfall-line-chart'),

    html.Div([
        html.Button("📥 Print Dashboard as PDF", id="print-btn", n_clicks=0, className="btn btn-secondary", style={"margin": "20px"}),
        dcc.Interval(id='trigger-print', interval=1000, n_intervals=0, disabled=True)
    ], style={"textAlign": "center", "marginBottom": "30px"})
])

# Callback for updating dashboard
@app.callback(
    [Output('rainfall-bar-chart', 'figure'),
     Output('rainfall-line-chart', 'figure'),
     Output('average-indicator', 'children')],
    [Input('subdivision-dropdown', 'value'),
     Input('year-range-slider', 'value')]
)
def update_dashboard(selected_subdivision, selected_years):
    year_min, year_max = selected_years
    filtered_df = df_melted[(df_melted['Subdivision'] == selected_subdivision) &
                            (df_melted['Year'] >= year_min) &
                            (df_melted['Year'] <= year_max)]

    avg_rainfall = round(filtered_df['Rainfall_mm'].mean(), 2)
    indicator_text = f"Average Rainfall in {selected_subdivision} ({year_min} - {year_max}): {avg_rainfall} mm"

    bar_df = filtered_df.groupby('Month')['Rainfall_mm'].mean().reset_index()
    bar_chart = px.bar(
        bar_df, x='Month', y='Rainfall_mm',
        title=f"Average Monthly Rainfall - {selected_subdivision}",
        labels={'Rainfall_mm': 'Rainfall (mm)'},
        color='Rainfall_mm',
        color_continuous_scale='Blues'
    )

    line_df = filtered_df.groupby('Year')['Rainfall_mm'].sum().reset_index()
    line_chart = px.line(
        line_df, x='Year', y='Rainfall_mm',
        title=f"Total Yearly Rainfall - {selected_subdivision}",
        markers=True
    )

    return bar_chart, line_chart, indicator_text

# Browser-side print (PDF) export using clientside JS
app.clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks > 0) {
            window.print();
        }
        return window.dash_clientside.no_update;
    }
    """,
    Output('trigger-print', 'disabled'),
    Input('print-btn', 'n_clicks')
)

# Run the Dash server
if __name__ == '__main__':
    app.run(debug=True)
