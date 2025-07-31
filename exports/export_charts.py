import pandas as pd
import plotly.express as px

df = pd.read_csv("data/Rainfall_Data_LL.csv")

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

df_melted = df.melt(id_vars=['SUBDIVISION', 'YEAR'],
                    value_vars=months,
                    var_name='Month',
                    value_name='Rainfall_mm')

df_melted.columns = ['Subdivision', 'Year', 'Month', 'Rainfall_mm']
df_melted['Month'] = df_melted['Month'].str.capitalize()
df_melted.dropna(inplace=True)

# Loop through subdivisions
for subdivision in df_melted['Subdivision'].unique():
    yearly_df = df_melted[df_melted['Subdivision'] == subdivision] \
        .groupby('Year')['Rainfall_mm'].sum().reset_index()
    
    fig = px.line(yearly_df, x='Year', y='Rainfall_mm',
                  title=f"{subdivision} - Yearly Rainfall (1901–2017)",
                  markers=True)
    
    filename = f"exports/{subdivision.replace(' ', '_')}_rainfall_trend.png"
    fig.write_image(filename)

print("Export complete. Check the 'exports' folder.")
