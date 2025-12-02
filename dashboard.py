import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
from datetime import datetime

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "European Housing Price Index Dashboard"

def load_data():
    df = pd.read_csv('data/prc_hpi_q_linear_2_0.csv')

    df_clean = df[['geo', 'Geopolitical entity (reporting)', 'TIME_PERIOD', 'OBS_VALUE']].copy()
    df_clean.columns = ['country_code', 'country_name', 'time_period', 'price_index']

    df_clean = df_clean.dropna(subset=['price_index'])

    exclude_codes = ['EA', 'EA19', 'EA20', 'EU', 'EU27_2020', 'EU28']
    df_clean = df_clean[~df_clean['country_code'].isin(exclude_codes)]

    df_clean['year'] = df_clean['time_period'].str[:4].astype(int)
    df_clean['quarter'] = df_clean['time_period'].str[-2:]

    quarter_to_month = {'Q1': '01', 'Q2': '04', 'Q3': '07', 'Q4': '10'}
    df_clean['date'] = pd.to_datetime(
        df_clean['year'].astype(str) + '-' +
        df_clean['quarter'].map(quarter_to_month) + '-01'
    )

    df_clean = df_clean[(df_clean['price_index'] >= 10) & (df_clean['price_index'] <= 500)]
    df_clean = df_clean[df_clean['year'] <= 2024]
    df_clean = df_clean.sort_values(['country_name', 'date'])
    df_clean = df_clean.drop_duplicates(subset=['country_name', 'time_period'], keep='first')

    country_name_fixes = {
        'Türkiye': 'Turkey',
        'T�rkiye': 'Turkey',
        'Czechia': 'Czech Republic',
    }
    df_clean['country_name'] = df_clean['country_name'].replace(country_name_fixes)

    return df_clean

df = load_data()

countries = sorted(df['country_name'].unique())
years = sorted(df['year'].unique())
latest_year = max(years)

country_mapping = df[['country_code', 'country_name']].drop_duplicates().set_index('country_code')['country_name'].to_dict()

COLORBLIND_SAFE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
                   '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("European Housing Price Index",
                   className="text-center mb-3 mt-4",
                   style={'color': '#2c3e50', 'font-weight': 'bold', 'font-size': '2.5rem'}),
            html.P([
                "Track and compare housing price trends across 30+ European countries. ",
                html.Br(),
                "Baseline: 2010 = 100 (values above 100 indicate price increases since 2010)"
            ],
                  className="text-center mb-1",
                  style={'font-size': '1.1rem', 'color': '#555'}),
            html.P("Use the filters below to explore different time periods and compare countries",
                  className="text-center text-muted mb-4",
                  style={'font-size': '0.95rem'}),
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H6("How to Use This Dashboard", className="alert-heading mb-2"),
                html.P([
                    "• ", html.Strong("Year Range Slider"), " - Filters ALL charts to show data within the selected years",
                    html.Br(),
                    "• ", html.Strong("Country Selector"), " - Filters ALL charts to show only selected countries (leave empty to show all)",
                    html.Br(),
                    "• ", html.Strong("Hover Over Charts"), " - See detailed values and country names",
                    html.Br(),
                    "• ", html.Strong("Price Index > 100"), " = prices increased since 2010, < 100 = prices decreased",
                ], className="mb-0", style={'font-size': '0.9rem'})
            ], color="info", className="mb-4", dismissable=True)
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H5("Filters & Controls", className="card-title mb-3"),

                    html.Label([
                        html.I(className="bi bi-calendar-range me-2"),
                        "Select Time Period:"
                    ], className="fw-bold mt-2 mb-2", style={'font-size': '1rem'}),
                    html.P("Drag the handles to select the start and end year",
                          className="text-muted small mb-2"),
                    dcc.RangeSlider(
                        id='year-slider',
                        min=min(years),
                        max=max(years),
                        value=[max(years)-5, max(years)],
                        marks={str(year): {'label': str(year), 'style': {'font-size': '0.9rem'}}
                               for year in range(min(years), max(years)+1, 2)},
                        step=1,
                        tooltip={"placement": "bottom", "always_visible": True},
                        className="mb-4"
                    ),

                    html.Label([
                        html.I(className="bi bi-globe me-2"),
                        "Select Countries to Compare:"
                    ], className="fw-bold mt-3 mb-2", style={'font-size': '1rem'}),
                    html.P([
                        "Choose countries to display in ",
                        html.Strong("all charts"),
                        ". Leave empty or select all to show everything."
                    ], className="text-muted small mb-2"),
                    dcc.Dropdown(
                        id='country-dropdown',
                        options=[{'label': country, 'value': country} for country in countries],
                        value=[],
                        multi=True,
                        placeholder="Select countries (empty = show all)...",
                        style={'font-size': '0.95rem'}
                    ),
                    html.P([
                        html.Small([
                            html.Strong("Tip:"),
                            " Leave empty to see all countries, or select specific ones to focus your analysis."
                        ], className="text-info")
                    ], className="mt-2 mb-0"),
                ], style={'padding': '1.5rem'})
            ], className="mb-4", style={'box-shadow': '0 4px 6px rgba(0,0,0,0.1)'})
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(id="metric-countries", className="card-title text-primary mb-1",
                           style={'font-weight': 'bold'}),
                    html.P("Countries", className="card-text text-muted mb-0",
                          style={'font-size': '0.9rem'})
                ], className="text-center")
            ], style={'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(id="metric-highest", className="card-title text-success mb-1",
                           style={'font-weight': 'bold', 'font-size': '1.3rem'}),
                    html.P("Highest Growth", className="card-text text-muted mb-0",
                          style={'font-size': '0.9rem'})
                ], className="text-center")
            ], style={'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(id="metric-lowest", className="card-title text-danger mb-1",
                           style={'font-weight': 'bold', 'font-size': '1.3rem'}),
                    html.P("Lowest Growth", className="card-text text-muted mb-0",
                          style={'font-size': '0.9rem'})
                ], className="text-center")
            ], style={'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(id="metric-avg", className="card-title text-info mb-1",
                           style={'font-weight': 'bold'}),
                    html.P("Average Index", className="card-text text-muted mb-0",
                          style={'font-size': '0.9rem'})
                ], className="text-center")
            ], style={'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=3),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("World Map - Housing Price Index", className="text-white mb-1",
                           style={'font-weight': 'bold'}),
                    html.Small("Showing 30 European countries with housing data. Pan and zoom to explore. Includes Turkey on the eastern side",
                             className="text-white-50")
                ], style={'background-color': '#34495e', 'padding': '1rem'}),
                dbc.CardBody([
                    dcc.Graph(
                        id='price-map',
                        config={
                            'displayModeBar': True,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': ['lasso2d', 'select2d'],
                            'responsive': True
                        },
                        style={'height': '100%', 'width': '100%'}
                    )
                ], style={'padding': '0.5rem', 'min-height': '500px'})
            ], style={'box-shadow': '0 4px 8px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=7),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("Top Countries", className="text-white mb-1",
                           style={'font-weight': 'bold'}),
                    html.Small("Countries with highest price indices",
                             className="text-white-50")
                ], style={'background-color': '#34495e', 'padding': '1rem'}),
                dbc.CardBody([
                    dcc.Graph(id='price-bar-chart', config={'displayModeBar': False})
                ], style={'padding': '0.5rem'})
            ], style={'box-shadow': '0 4px 8px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=5),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("Price Trends Over Time", className="text-white mb-1",
                           style={'font-weight': 'bold'}),
                    html.Small("Compare how housing prices changed for selected countries",
                             className="text-white-50")
                ], style={'background-color': '#34495e', 'padding': '1rem'}),
                dbc.CardBody([
                    dcc.Graph(id='price-time-series', config={'displayModeBar': True})
                ], style={'padding': '0.5rem'})
            ], style={'box-shadow': '0 4px 8px rgba(0,0,0,0.1)', 'border': 'none'})
        ])
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    html.H5("Growth Analysis", className="text-white mb-1",
                           style={'font-weight': 'bold'}),
                    html.Small("Compare starting vs ending prices. Color: Green=increase, Yellow=no change, Red=decrease. Size=magnitude",
                             className="text-white-50")
                ], style={'background-color': '#34495e', 'padding': '1rem'}),
                dbc.CardBody([
                    dcc.Graph(id='growth-scatter', config={'displayModeBar': False})
                ], style={'padding': '0.5rem'})
            ], style={'box-shadow': '0 4px 8px rgba(0,0,0,0.1)', 'border': 'none'})
        ])
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.Hr(style={'margin-top': '2rem'}),
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.P([
                            html.Strong("Data Source: "),
                            "Eurostat - European Commission (Official EU Housing Statistics)",
                            html.Br(),
                            html.Strong("Team: "),
                            "DataViz Duo | Sergei Litvinov & Vladyslav Hontar",
                            html.Br(),
                            html.Strong("Coverage: "),
                            f"{min(years)}-{max(years)} (Quarterly Updates) | 30+ European Countries",
                        ], className="text-center mb-0",
                          style={'font-size': '0.9rem', 'color': '#666'})
                    ])
                ], className="py-3")
            ], style={'background-color': '#f8f9fa', 'border': 'none'})
        ])
    ], className="mt-4")

], fluid=True, style={'background-color': '#f8f9fa'})


@callback(
    [Output('metric-countries', 'children'),
     Output('metric-highest', 'children'),
     Output('metric-lowest', 'children'),
     Output('metric-avg', 'children')],
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_metrics(year_range, selected_countries):
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    if selected_countries and len(selected_countries) > 0:
        filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

    latest_data = filtered_df.sort_values('date').groupby('country_name').last()

    num_countries = len(latest_data)

    if len(latest_data) > 0:
        highest_country = latest_data['price_index'].idxmax()
        highest_value = latest_data['price_index'].max()

        lowest_country = latest_data['price_index'].idxmin()
        lowest_value = latest_data['price_index'].min()

        avg_value = latest_data['price_index'].mean()

        return (
            str(num_countries),
            f"{highest_country}: {highest_value:.1f}",
            f"{lowest_country}: {lowest_value:.1f}",
            f"{avg_value:.1f}"
        )

    return "0", "N/A", "N/A", "N/A"


@callback(
    Output('price-map', 'figure'),
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_map(year_range, selected_countries):
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    if selected_countries and len(selected_countries) > 0:
        filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

    latest_data = filtered_df.sort_values('date').groupby('country_name').last().reset_index()

    fig = px.choropleth(
        latest_data,
        locations='country_name',
        locationmode='country names',
        color='price_index',
        hover_name='country_name',
        hover_data={'country_name': False, 'price_index': ':.1f', 'time_period': True},
        color_continuous_scale='RdYlGn_r',
        labels={'price_index': 'Price Index', 'time_period': 'Quarter'},
    )

    fig.update_layout(
        geo=dict(
            showframe=True,
            showcoastlines=True,
            showcountries=True,
            projection_type='natural earth',
            bgcolor='rgba(230, 245, 255, 0.5)',
            lakecolor='rgb(200, 220, 240)',
            landcolor='rgb(250, 250, 250)',
            oceancolor='rgb(220, 235, 250)',
            countrycolor='rgb(200, 200, 200)',
            coastlinecolor='rgb(150, 150, 150)',
            coastlinewidth=0.8,
            center=dict(lat=50, lon=20),
            projection_scale=1.8,
        ),
        autosize=True,
        margin=dict(l=0, r=0, t=10, b=0, pad=0),
        coloraxis_colorbar=dict(
            title=dict(text="Price Index<br>(2010=100)", font=dict(size=11)),
            thickness=18,
            len=0.65,
            x=1.0,
            xpad=5
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_traces(
        marker_line_color='white',
        marker_line_width=1.2
    )

    return fig


@callback(
    Output('price-bar-chart', 'figure'),
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_bar_chart(year_range, selected_countries):
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    if selected_countries and len(selected_countries) > 0:
        filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

    latest_data = filtered_df.sort_values('date').groupby('country_name').last().reset_index()
    latest_data = latest_data.sort_values('price_index', ascending=True)

    if not selected_countries or len(selected_countries) == 0:
        latest_data = latest_data.tail(15)
    elif len(latest_data) > 15:
        latest_data = latest_data.tail(15)

    fig = px.bar(
        latest_data,
        y='country_name',
        x='price_index',
        orientation='h',
        color='price_index',
        color_continuous_scale='RdYlGn_r',
        labels={'country_name': 'Country', 'price_index': 'Price Index'},
        title='Top 15 Countries by Price Index'
    )

    fig.update_layout(
        height=500,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title="Price Index (2010=100)",
        yaxis_title="",
        margin=dict(l=10, r=10, t=40, b=40)
    )

    return fig


@callback(
    Output('price-time-series', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_time_series(selected_countries, year_range):
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    if not selected_countries or len(selected_countries) == 0:
        latest_data = filtered_df.sort_values('date').groupby('country_name').last()
        top_countries = latest_data.nlargest(10, 'price_index').index.tolist()
        filtered_df = filtered_df[filtered_df['country_name'].isin(top_countries)]
    else:
        filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

    fig = px.line(
        filtered_df,
        x='date',
        y='price_index',
        color='country_name',
        labels={'date': 'Year', 'price_index': 'Price Index', 'country_name': 'Country'},
        title='Housing Price Index Trends',
        color_discrete_sequence=COLORBLIND_SAFE
    )

    fig.update_layout(
        height=400,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        xaxis_title="Year",
        yaxis_title="Price Index (2010=100)",
        margin=dict(l=50, r=20, t=40, b=40)
    )

    fig.update_traces(line=dict(width=3))

    fig.add_hline(y=100, line_dash="dash", line_color="gray",
                  annotation_text="Baseline (2010)", annotation_position="right")

    return fig


@callback(
    Output('growth-scatter', 'figure'),
    [Input('year-slider', 'value'),
     Input('country-dropdown', 'value')]
)
def update_scatter(year_range, selected_countries):
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

    if selected_countries and len(selected_countries) > 0:
        filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

    growth_data = []
    for country in filtered_df['country_name'].unique():
        country_df = filtered_df[filtered_df['country_name'] == country].sort_values('date')
        if len(country_df) > 1:
            start_price = country_df.iloc[0]['price_index']
            end_price = country_df.iloc[-1]['price_index']

            if start_price > 0 and end_price > 0:
                growth_pct = ((end_price - start_price) / start_price) * 100

                growth_data.append({
                    'country_name': country,
                    'start_price': start_price,
                    'end_price': end_price,
                    'growth_pct': growth_pct,
                    'abs_growth': max(abs(growth_pct), 1)
                })

    growth_df = pd.DataFrame(growth_data)

    if len(growth_df) == 0:
        return go.Figure().update_layout(
            title='No data available for selected range',
            height=400
        )

    fig = go.Figure()

    max_abs_growth = max(growth_df['abs_growth'])
    normalized_sizes = (growth_df['abs_growth'] / max_abs_growth * 35) + 5

    max_abs_pct = max(abs(growth_df['growth_pct'].min()), abs(growth_df['growth_pct'].max()))

    fig.add_trace(go.Scatter(
        x=growth_df['start_price'],
        y=growth_df['end_price'],
        mode='markers',
        marker=dict(
            size=normalized_sizes,
            sizemode='diameter',
            color=growth_df['growth_pct'],
            colorscale='RdYlGn',
            cmid=0,
            cmin=-max_abs_pct,
            cmax=max_abs_pct,
            colorbar=dict(
                title=dict(text='Growth %', font=dict(size=12)),
                thickness=15,
                len=0.7,
                tickformat='+.0f'
            ),
            line=dict(width=1, color='white'),
            opacity=0.8
        ),
        text=growth_df['country_name'],
        customdata=growth_df['growth_pct'],
        hovertemplate='<b>%{text}</b><br>' +
                      f'Start ({year_range[0]}): %{{x:.1f}}<br>' +
                      f'End ({year_range[1]}): %{{y:.1f}}<br>' +
                      'Growth: %{customdata:+.1f}%<br>' +
                      '<extra></extra>',
        showlegend=False
    ))

    min_val = min(growth_df['start_price'].min(), growth_df['end_price'].min())
    max_val = max(growth_df['start_price'].max(), growth_df['end_price'].max())
    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            line=dict(dash='dash', color='gray', width=1),
            showlegend=False,
            hoverinfo='skip'
        )
    )

    fig.update_layout(
        xaxis_title=f'Starting Price Index ({year_range[0]})',
        yaxis_title=f'Ending Price Index ({year_range[1]})',
        height=400,
        margin=dict(l=50, r=20, t=20, b=40),
        hovermode='closest',
        plot_bgcolor='rgba(250,250,250,0.5)',
        font=dict(size=11)
    )

    fig.add_annotation(
        x=max_val * 0.7,
        y=max_val * 0.7,
        text="No change line",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="gray",
        ax=-40,
        ay=-40,
        font=dict(size=10, color="gray")
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8050)
