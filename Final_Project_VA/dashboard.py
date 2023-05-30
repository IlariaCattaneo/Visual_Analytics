import pandas as pd
import plotly.express as px
import warnings
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import dcc
from dash import html
import math
import base64

# MAKE SURE YOU USE YOUR PATH TO DATASETS CORRECTLY
temperature_var = pd.read_csv('temperature_var.csv')
production_cereal = pd.read_csv('production_cereal.csv')
gdp = pd.read_csv('gdp.csv')
population = pd.read_csv('population.csv')
emission_share = pd.read_csv('emission_share.csv')
emission_share_w = pd.read_csv('emission_share.csv')
employement_agr = pd.read_csv('employement_agr.csv')
precipitations = pd.read_csv('precipitations.csv')
temperature_data = pd.read_csv('temperature_data.csv')

precipitations = precipitations.rename(columns={'Entity':'Country'})
production_cereal_temperature = pd.merge(temperature_var, production_cereal, on=['Country', 'Year'])
production_cereal_precipitation = pd.merge(production_cereal, precipitations, on=['Country', 'Year'])
merged_data = pd.merge(production_cereal_precipitation, gdp, on=['Country', 'Year'])
merged_data = merged_data.rename(columns={'Element_x':'Production', 'Item_x' : 'Type of Production', 'Unit_x' : 'Unit_Production', 'Value_x':'Value_Production', 'Element_y':'Currency', 'Item_y':'Name of metric',
                                          'Unit_y' : 'Unit_Millions', 'Value_y':'GDP'})


pio.templates.default = "plotly_dark"


# FIRST GRAPH ASIA
warnings.filterwarnings("ignore")

map_data_1 = production_cereal_temperature[['Country', 'Year', 'Value_x', 'Unit_y', 'Value_y']]

map_data_1['Year'] = pd.to_datetime(map_data_1['Year'], format='%Y').dt.strftime('%Y')
map_data_1['Value_x'] = pd.to_numeric(map_data_1['Value_x'])
map_data_1['Value_y'] = pd.to_numeric(map_data_1['Value_y'])

temperature_range = [map_data_1['Value_y'].min(), map_data_1['Value_y'].max()]

fig14 = px.choropleth(
    map_data_1,
    locations='Country',
    locationmode='country names',
    color='Value_y',
    hover_name='Country',
    hover_data=['Year', 'Value_x', 'Unit_y', 'Value_y'],
    animation_frame='Year',
    color_continuous_scale='Viridis',
    range_color=temperature_range,
    title='Cereal production by Country and Year for Asia',
    labels={'Value_y': 'Crop Production'}
)

fig14.update_traces(
    text=map_data_1['Value_y'].astype(str) + ' ' + map_data_1['Unit_y'],
    hovertemplate='<b>%{hovertext}</b><br>Cereal production: %{text}'
)

fig14.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('asia')
    ),
    coloraxis_colorbar=dict(title='Cereal production'),
    coloraxis_colorbar_len=0.5,
    width=1280,
    height=720
)

fig14.update_layout(template='plotly_dark')

# CROP FOR EU
fig15 = px.choropleth(
    map_data_1,
    locations='Country',
    locationmode='country names',
    color='Value_y',
    hover_name='Country',
    hover_data=['Year', 'Value_x', 'Unit_y', 'Value_y'],
    animation_frame='Year',
    color_continuous_scale='Viridis',
    range_color=temperature_range,
    title='Cereal production by Country and Year for Europe',
    labels={'Value_y': 'Crop Production'}
)

fig15.update_traces(
    text=map_data_1['Value_y'].astype(str) + ' ' + map_data_1['Unit_y'],
    hovertemplate='<b>%{hovertext}</b><br>Cereal production: %{text}'
)

fig15.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('europe')
    ),
    coloraxis_colorbar=dict(title='Cereal production'),
    coloraxis_colorbar_len=0.5,
    width=1280,
    height=720
)

fig15.update_layout(template='plotly_dark')

warnings.filterwarnings("ignore")

map_data_1 = production_cereal_temperature[['Country', 'Year', 'Value_x', 'Unit_y', 'Value_y']]

map_data_1['Year'] = pd.to_datetime(map_data_1['Year'], format='%Y').dt.strftime('%Y')
map_data_1['Value_x'] = pd.to_numeric(map_data_1['Value_x'])
map_data_1['Value_y'] = pd.to_numeric(map_data_1['Value_y'])

temperature_range = [map_data_1['Value_x'].min(), map_data_1['Value_x'].max()]

fig1 = px.choropleth(
    map_data_1,
    locations='Country',
    locationmode='country names',
    color='Value_x',
    hover_name='Country',
    hover_data=['Year', 'Value_x', 'Unit_y', 'Value_y'],
    animation_frame='Year',
    color_continuous_scale='Viridis',
    range_color=temperature_range,
    title='Temperature (Celsius) by Country and Year for Asia',
    labels={'Value_x': 'Temperatures (°C)'}
)

fig1.update_traces(
    text=map_data_1['Value_y'].astype(str) + ' ' + map_data_1['Unit_y'],
    hovertemplate='<b>%{hovertext}</b><br>Temperature: %{z:.2f}°C<br>Value: %{text}'
)

fig1.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('asia')
    ),
    coloraxis_colorbar=dict(title='Differences in average Temperature (°C)'),
    coloraxis_colorbar_len=0.5,
    width=1280,
    height=720
)

fig1.update_layout(template='plotly_dark')

# FIRST GRAPH EUROPE
warnings.filterwarnings("ignore")

map_data_1 = production_cereal_temperature[['Country', 'Year', 'Value_x', 'Unit_y', 'Value_y']]

map_data_1['Year'] = pd.to_datetime(map_data_1['Year'], format='%Y').dt.strftime('%Y')
map_data_1['Value_x'] = pd.to_numeric(map_data_1['Value_x'])
map_data_1['Value_y'] = pd.to_numeric(map_data_1['Value_y'])

temperature_range = [map_data_1['Value_x'].min(), map_data_1['Value_x'].max()]

fig9 = px.choropleth(
    map_data_1,
    locations='Country',
    locationmode='country names',
    color='Value_x',
    hover_name='Country',
    hover_data=['Year', 'Value_x', 'Unit_y', 'Value_y'],
    animation_frame='Year',
    color_continuous_scale='Viridis',
    range_color=temperature_range,
    title='Temperature (Celsius) by Country and Year for Europe',
    labels={'Value_x': 'Differences in average temperatures (°C) '}
)

fig9.update_traces(
    text=map_data_1['Value_y'].astype(str) + ' ' + map_data_1['Unit_y'],
    hovertemplate='<b>%{hovertext}</b><br>Temperature: %{z:.2f}°C<br>Value: %{text}'
)

fig9.update_layout(
    margin=dict(l=0, r=0, t=50, b=0),
    coloraxis_colorbar=dict(title='Differences in average Temperature (°C)'),
    coloraxis_colorbar_len=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('europe')
    ),
    width=1280,
    height=720
)

fig9.update_layout(template='plotly_dark')

# SECOND GRAPH
map_data = production_cereal_precipitation[['Country', 'Year', 'Value', 'Average precipitation in depth (mm per year)']]

map_data.loc[:, 'Average precipitation in depth (mm per year)'] = pd.to_numeric(map_data['Average precipitation in depth (mm per year)'])

years = sorted(map_data['Year'].unique())

fig2 = go.Figure()

for year in years:
    year_data = map_data[map_data['Year'] == year]
    fig2.add_trace(
        go.Choropleth(
            locations=year_data['Country'],
            locationmode='country names',
            z=year_data['Average precipitation in depth (mm per year)'],
            colorscale='Blues',
            zmin=0,
            zmax=map_data['Average precipitation in depth (mm per year)'].max(),
            colorbar=dict(title='Average Precipitation (mm/year)'),
            hovertemplate='<b>%{location}</b><br>Value: %{customdata:.2f}<br>Precipitation: %{z:.2f} mm/year',
            customdata=year_data['Value']
        )
    )


fig2.update_layout(
    title='Production of cereals and Average Precipitation by Country and Year',
    geo=dict(showframe=False, showcoastlines=False, projection_type='equirectangular'),
    sliders=[
        {
            'currentvalue': {'prefix': 'Year: '},
            'steps': [{'method': 'update', 'label': str(year), 'args': [{'visible': [year == y for y in map_data['Year'].unique()]}]} for year in years],
            'transition': {'duration': 500},
            'pad': {'t': 50}
        }
    ],
    width=1280,
    height=720
)

fig2.update_layout(template='plotly_dark')

# THIRD GRAPH
cereal_top = production_cereal[(production_cereal['Country'] == 'Kazakhstan') | (production_cereal['Country'] == 'Thailand') | (production_cereal['Country'] == 'France') | (production_cereal['Country'] == 'Poland')]

countries = cereal_top['Country'].unique()



dropdown_filter = []
for country in countries:
    dropdown_filter.append(
        dict(
            method='update',
            args=[{'visible': [country == c for c in countries]}],
            label=country
        )
    )

fig3 = go.Figure()

for country in cereal_top['Country'].unique():
    fig3.add_trace(
        go.Scatter(
            x=cereal_top[cereal_top['Country'] == country]['Year'].astype(int),
            y=cereal_top[cereal_top['Country'] == country]['Value'],
            mode='lines',
            name=country,
            visible="legendonly"
        )
    )


fig3.update_layout(
    updatemenus=[go.layout.Updatemenu(
        buttons=dropdown_filter,
        active=0,
        showactive=True,
        direction="down",
        x=0.1,
        xanchor="left",
        y=1.1,
        yanchor="top"
    )],
    hovermode='x',
    xaxis=dict(
        title='Year',
        tickformat="d"
    ),
    yaxis=dict(title='Crop Yield (Tonnes)'),
    title='Crop Yields Over Time (in tonnes) for Kazakhstan, Thailand, Poland, France',
    template='plotly_dark',
    width=1280,
    height=720
)



# FOURTH GRAPH
countries = gdp['Country'].unique()


dropdown_filter = []
for country in countries:
    dropdown_filter.append(
        dict(
            method='update',
            args=[{'visible': [country == c for c in countries]}],
            label=country
        )
    )


fig4 = go.Figure()

for country in gdp['Country'].unique():
    fig4.add_trace(
        go.Scatter(
            x=gdp[gdp['Country'] == country]['Year'],
            y=gdp[gdp['Country'] == country]['Value'],
            mode='lines',
            name=country,
            hovertemplate='Year: %{x}<br>GDP: %{y}<br>%{hovertext}',
            hovertext=[f"GDP: {val:.2f}" for val in gdp[gdp['Country'] == country]['Value']],
            visible="legendonly"
        )
    )


fig4.update_layout(
    updatemenus=[go.layout.Updatemenu(
        buttons=dropdown_filter,
        direction="down",
        pad={"r": 10, "t": 10},
        showactive=True,
        x=0.1,
        xanchor="left",
        y=1.1,
        yanchor="top"
    )],
    xaxis=dict(title='Year'),
    yaxis=dict(title='GDP (USD)'),
    title='GDP over years',
    height=500, width=1440,
    template='plotly_dark'
)

df_cereal = production_cereal_temperature

fig6 = go.Figure()

for country in df_cereal['Country'].unique():
    fig6.add_trace(
        go.Scatter(
            x = df_cereal[df_cereal['Country'] == country]['Year'],
            y = df_cereal[df_cereal['Country'] == country]['Value_y'],
            mode = 'lines',
            name = country,
            visible = "legendonly"
        )
    )


dropdown = []
for country in df_cereal['Country'].unique():
    dropdown.append(
        dict(
            args = ['visible', [country == i for i in df_cereal['Country'].unique()]],
            label = country,
            method = 'restyle'
        )
    )


fig6.update_layout(
    updatemenus = [
        go.layout.Updatemenu(
            buttons = dropdown,
            direction = "down",
            pad = {"r": 10, "t": 10},
            showactive = True,
            x = 0.1,
            xanchor = "left",
            y = 1.1,
            yanchor = "top"
        ),
    ],
    title = "Cereal production over the years",
    xaxis_title = "Year",
    yaxis_title = "Cereal Production (tonnes)",
)


fig6.update_layout(template='plotly_dark')

# SEVENTH GRAPH

df_emissions = emission_share[emission_share['Country'] != 'World']
df_emissions = emission_share[emission_share['Year'] >= 1950]
df_emissions['Normalized Emissions'] = df_emissions['Share of global annual CO₂ emissions'].apply(lambda x: math.log(x, 10))

fig7 = go.Figure()

for year in df_emissions['Year'].unique():
    fig7.add_trace(
        go.Choropleth(
            locations=df_emissions[df_emissions['Year'] == year]['Code'],
            z=df_emissions[df_emissions['Year'] == year]['Normalized Emissions'],
            zmin=df_emissions['Normalized Emissions'].min(),
            zmax=df_emissions['Normalized Emissions'].max(),
            text=df_emissions[df_emissions['Year'] == year]['Share of global annual CO₂ emissions'],
            hovertemplate = '<b>%{location} </b>Absolute CO₂ Emissions: %{text}<br>Log Scaled CO₂ Emissions: %{z:.2f}',
            visible=(year == df_emissions['Year'].min()),
            autocolorscale=True,
            colorbar=dict(title='Normalized Emissions (Log Scale)'),
            colorscale='YlOrRd',
            reversescale=True
        )
    )


steps = []
for i, year in enumerate(df_emissions['Year'].unique()):
    step = dict(
        method='restyle',
        args=['visible', [False] * len(df_emissions['Year'].unique())],
        label=str(year)
    )
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Year: "},
    pad={"t": 50},
    steps=steps
)]

fig7.update_layout(
    sliders=sliders,
    title_text='Share of global annual CO₂ emissions over the years for Asia',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('asia')
    ),
    width=1280,
    height=720
)

fig7.update_layout(template='plotly_dark')

# SEVENTH GRAPH Without China

df_emissions_w = emission_share_w[(emission_share_w['Country'] != 'China') & (emission_share_w['Country'] != 'World')]
df_emissions_w = df_emissions_w[df_emissions_w['Year'] >= 1950]
df_emissions_w['Normalized Emissions'] = df_emissions_w['Share of global annual CO₂ emissions'].apply(lambda x: math.log(x, 10))

fig16 = go.Figure()

for year in df_emissions_w['Year'].unique():
    fig16.add_trace(
        go.Choropleth(
            locations=df_emissions_w[df_emissions_w['Year'] == year]['Code'],
            z=df_emissions_w[df_emissions_w['Year'] == year]['Normalized Emissions'],
            zmin=df_emissions_w['Normalized Emissions'].min(),
            zmax=df_emissions_w['Normalized Emissions'].max(),
            text=df_emissions_w[df_emissions_w['Year'] == year]['Share of global annual CO₂ emissions'],
            hovertemplate = '<b>%{location} </b>Absolute CO₂ Emissions: %{text}<br>Log Scaled CO₂ Emissions: %{z:.2f}',
            visible=(year == df_emissions_w['Year'].min()),
            autocolorscale=True,
            colorbar=dict(title='Normalized Emissions (Log Scale)'),
            colorscale='YlOrRd',
            reversescale=True
        )
    )

steps = []
for i, year in enumerate(df_emissions_w['Year'].unique()):
    step = dict(
        method='restyle',
        args=['visible', [False] * len(df_emissions_w['Year'].unique())],
        label=str(year)
    )
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Year: "},
    pad={"t": 50},
    steps=steps
)]

fig16.update_layout(
    sliders=sliders,
    title_text='Share of global annual CO₂ emissions over the years for Asia without China',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('asia')
    ),
    width=1280,
    height=720
)

fig16.update_layout(template='plotly_dark')

# EIGTH GRAPH

fig8 = go.Figure()

for year in df_emissions['Year'].unique():
    fig8.add_trace(
        go.Choropleth(
            locations=df_emissions[df_emissions['Year'] == year]['Code'],
            z=df_emissions[df_emissions['Year'] == year]['Normalized Emissions'],
            zmin=df_emissions['Normalized Emissions'].min(),
            zmax=df_emissions['Normalized Emissions'].max(),
            text=df_emissions[df_emissions['Year'] == year]['Share of global annual CO₂ emissions'],
            hovertemplate = '<b>%{location} </b>Absolute CO₂ Emissions: %{text}<br>Log Scaled CO₂ Emissions: %{z:.2f}',
            visible=(year == df_emissions['Year'].min()),
            autocolorscale=True,
            colorbar=dict(title='Normalized Emissions (Log Scale)'),
            colorscale='YlOrRd',
            reversescale=True
        )
    )

# Now we create a slider
steps = []
for i, year in enumerate(df_emissions['Year'].unique()):
    step = dict(
        method='restyle',
        args=['visible', [False] * len(df_emissions['Year'].unique())],
        label=str(year)
    )
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Year: "},
    pad={"t": 50},
    steps=steps
)]

fig8.update_layout(
    sliders=sliders,
    title_text='Share of global annual CO₂ emissions over the years for Europe',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='natural earth',
        scope=('europe')
    ),
    width=1280,
    height=720
)

fig8.update_layout(template='plotly_dark')


# NINTH GRAPH
grouped = production_cereal.groupby(['Year', 'Continent'])['Value'].sum().reset_index()

grouped['Total'] = grouped.groupby('Year')['Value'].transform('sum')

grouped['Percentage'] = (grouped['Value'] / grouped['Total']) * 100
grouped['Percentage'] = grouped['Percentage'].round(2)

filtered_data = grouped[grouped['Continent'].isin(['Europe', 'Asia'])]

europe_data = filtered_data[filtered_data['Continent'] == 'Europe']
asia_data = filtered_data[filtered_data['Continent'] == 'Asia']

fig10 = go.Figure()

fig10.add_trace(go.Bar(
    x=europe_data['Year'],
    y=europe_data['Percentage'],
    name='Europe',
    text=europe_data['Percentage'],
    textposition='auto',
    hovertemplate='Year: %{x}<br>Percentage: %{text:.2f}%<extra></extra>',
    texttemplate='%{text:.2f}%'
))

fig10.add_trace(go.Bar(
    x=asia_data['Year'],
    y=asia_data['Percentage'],
    name='Asia',
    text=asia_data['Percentage'],
    textposition='auto',
    hovertemplate='Year: %{x}<br>Percentage: %{text:.2f}%<extra></extra>',
    texttemplate='%{text:.2f}%'
))

fig10.update_layout(
    xaxis=dict(title='Year', type='category', categoryorder='category ascending'),
    yaxis=dict(title='Percentage of Cereal Production'),
    title='Summary Percentage of Cereal Production in Europe and Asia (Yearly): Bar Chart',
    barmode='group',
    showlegend=True,
)

fig10.update_traces(width=0.4)

fig10.update_layout(
    bargap=0.2,
    bargroupgap=0.1
)
fig10.update_layout(template='plotly_dark')


# TWO TABLES
df = production_cereal
df_europe = df[df['Continent'] == 'Europe']
df_asia = df[df['Continent'] == 'Asia']

countries_eu = df_europe['Country'].unique()

fig11 = go.Figure()

for country in countries_eu:
    temp_df = df[df['Country'] == country][['Year', 'Value']]
    visible = (countries_eu[0] == country)
    fig11.add_trace(go.Table(header=dict(values=['Year', 'Value in Tonnes'], fill_color='darkslategray', line_color='white', font=dict(color='white')),
                            cells=dict(values=[temp_df['Year'], temp_df['Value']], fill_color='black', line_color='white', font=dict(color='white')),
                            visible=visible))

dropdown = [{'label': country, 'method': 'update', 'args': [{'visible': [country == c for c in countries_eu]}]} for country in countries_eu]

fig11.update_layout(updatemenus=[{'buttons': dropdown, 'showactive': True, 'active': 0}],
                  title='Cereal production for European country',
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  height=300, width=200)

countries_as = df_asia['Country'].unique()

fig12 = go.Figure()

for country in countries_as:
    temp_df = df[df['Country'] == country][['Year', 'Value']]
    visible = (countries_as[0] == country)
    fig12.add_trace(go.Table(header=dict(values=['Year', 'Value in Tonnes'], fill_color='darkslategray', line_color='white', font=dict(color='white')),
                            cells=dict(values=[temp_df['Year'], temp_df['Value']], fill_color='black', line_color='white', font=dict(color='white')),
                            visible=visible))

dropdown = [{'label': country, 'method': 'update', 'args': [{'visible': [country == c for c in countries_as]}]} for country in countries_as]

fig12.update_layout(updatemenus=[{'buttons': dropdown, 'showactive': True, 'active': 0}],
                  title='Cereal production for Asian country',
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  height=300, width=200)


grouped_line = production_cereal.groupby(['Year', 'Continent'])['Value'].sum().reset_index()
filtered_data = grouped_line[grouped_line['Continent'].isin(['Europe', 'Asia'])]

europe_data = filtered_data[filtered_data['Continent'] == 'Europe']
asia_data = filtered_data[filtered_data['Continent'] == 'Asia']

fig17 = go.Figure()

fig17.add_trace(go.Scatter(
    x=europe_data['Year'],
    y=europe_data['Value'],
    mode='lines',
    name='Europe',
    hovertemplate='Year: %{x}<br>Total: %{y:.2f}<extra></extra>',
    texttemplate='%{y:.2f}%',
    line=dict(color='blue')
))
fig17.add_trace(go.Scatter(
    x=asia_data['Year'],
    y=asia_data['Value'],
    mode='lines',
    name='Asia',
    hovertemplate='Year: %{x}<br>Total: %{y:.2f}<extra></extra>',
    texttemplate='%{y:.2f}%',
    line=dict(color='red')
))

fig17.update_layout(
    xaxis=dict(title='Year', type='category', categoryorder='category ascending'),
    yaxis=dict(title='Amount of Cereal Production'),
    title='Summary of Cereal Production in Europe and Asia (Yearly): Line Chart',
    showlegend=True,
    template='plotly_dark'
)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open('FAO_logo.png', 'rb') as f:
    logo_image = f.read()
logo_encoded = base64.b64encode(logo_image).decode('utf-8')

app.layout = html.Div(style={'backgroundColor': '#0D1117', 'color': '#C9D1D9', 'font-family': 'CMU Serif'}, children=[
    html.Div(style={'display': 'flex', 'align-items': 'center'}, children=[
        html.Img(src='data:image/png;base64,{}'.format(logo_encoded), style={'height': '60px', 'margin-right': '10px'}),
        html.H1('Global Agricultural Trends: Analyzing changes of the different factors in Asian and European Countries', style={'textAlign': 'center', 'color': '#FFFFFF', 'font-family': 'CMU Serif'})
    ]),
    html.Div(
        html.H3("Cereal production choropleth map", style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'}),
    ),
    html.Div(dcc.Graph(id='graphic-14', figure=fig14), style={'width': '100%'}),

    html.Div(dcc.Graph(id='graphic-15', figure=fig15), style={'width': '100%'}),

    html.Div(style={'display': 'flex', 'justify-content': 'center'}, children=[dcc.Graph(id='graphic-3', figure=fig3, style={'margin': '0 auto'})]),

    html.Div(children=[
        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
            html.H2("Visualizing the Relationship between Temperature and Cereal Production in Asia and Europe: A Choropleth Map Comparison", 
                style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'}),
            dcc.Graph(id='graphic-1', figure=fig1)
        ]),

        html.Div(dcc.Graph(id='graphic-9', figure=fig9), style={'width': '100%'}),

        
        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
            html.H2("Visualizing the Contribution of Asia and Europe to Global Carbon Emissions: A Choropleth Map Comparison", 
                style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'}),
            dcc.Graph(id='graphic-7', figure=fig7)
        ]),

        html.Div(dcc.Graph(id='graphic-16', figure=fig16), style={'width': '100%'}),
        
        html.Div(dcc.Graph(id='graphic-8', figure=fig8), style={'width': '100%'}),

        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
            "NOTE: ",
            "In order to provide better visibility we used log scaled values to colorify choropleth map, when you hover to a specific country you can see absolute and log scaled values"
        ]),

        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px', 'display': 'flex',  'justify-content': 'center'}, children=[
            html.H2(children=[
                html.Span("",
                        style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'})
            ]),

]),


        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
            "NOTE: ",
            "The y-axes of the graphs presented in this project have not been normalized. This is because different countries have their own ranges of minimum and maximum values for cereal production and temperature, which can vary significantly depending on a variety of factors such as geography, climate, and agricultural practices. If we were to normalize the y-axes for all countries, some countries would have a flat line because their values are so small compared to other countries. Therefore, we have chosen to present the data as it is without normalization to provide an accurate representation of the trends in cereal production and temperature changes over time for each country."
        ]),

        html.Div(style={'backgroundColor': '#161B22', 'padding': '10px', 'display': 'flex', 'justify-content': 'center'}, children=[
            html.H2("Comparing Crop Yields and GDP Trends in Asian and European Countries", 
                style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'})
        ]),

        html.Div(style={'display': 'flex', 'justify-content': 'center'}, children=[dcc.Graph(id='graphic-4', figure=fig4, style={'margin': '0 auto'})]),

        
    ]),

    html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
        html.H2("Cereal Production in Asia and Europe: Insights", 
                style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'}),
        dcc.Graph(id='graphic-17', figure=fig17),
        dcc.Graph(id='graphic-10', figure=fig10),
    
    ]),

    html.Div(style={'backgroundColor': '#161B22', 'padding': '10px'}, children=[
    html.H2("Sources", style={"font-weight": "bold", "font-size": "20px", 'color': '#C9D1D9', 'textAlign': 'center'}),
    html.A('FAO Data', href='http://www.fao.org/faostat/en/#data', target='_blank', style={'color': '#C9D1D9', 'textDecoration': 'none',"font-size": "20px"})
    
    ])

    
    
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8055)