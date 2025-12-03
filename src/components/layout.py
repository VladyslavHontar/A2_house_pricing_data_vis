from dash import html, dcc
import dash_bootstrap_components as dbc
from src.components import header, filters, metrics

def create_layout(countries, years):
    min_year = min(years)
    max_year = max(years)

    return dbc.Container([
        header.create_header(),
        *filters.create_filters(countries, years),
        metrics.create_metrics(),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("World Map - Housing Price Index", className="text-white mb-1",
                               style={'font-weight': 'bold'}),
                        html.Small("See which countries have the most expensive housing (red) vs most affordable (green). Higher numbers = more expensive compared to your selected baseline year",
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
                        html.Div([
                            html.Div([
                                html.H5("Top 15 Countries", className="text-white mb-0",
                                       style={'font-weight': 'bold', 'display': 'inline-block', 'margin-right': '15px'}),
                                dbc.ButtonGroup([
                                    dbc.Button("Most Expensive", id="btn-expensive", color="light", outline=False, size="sm",
                                              style={'font-weight': '500'}),
                                    dbc.Button("Most Affordable", id="btn-affordable", color="light", outline=True, size="sm",
                                              style={'font-weight': '500'})
                                ], size="sm", style={'display': 'inline-block'})
                            ], className="mb-2"),
                            html.Small("Colors match the map: red=expensive, green=affordable",
                                     className="text-white-50"),
                            dcc.Store(id='bar-chart-sort', data='expensive')
                        ])
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
                        html.Small("Watch how housing prices changed over the years. Lines going up = prices increased, lines going down = prices decreased. The gray dotted line shows the baseline (no change)",
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
                        html.Small("Each bubble is a country. Countries above the diagonal line got MORE expensive. Bigger bubbles = bigger change. Green = increase, Red = decrease",
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
                                f"{min_year}-{max_year} (Quarterly Updates) | 30+ European Countries",
                            ], className="text-center mb-0",
                              style={'font-size': '0.9rem', 'color': '#666'})
                        ])
                    ], className="py-3")
                ], style={'background-color': '#f8f9fa', 'border': 'none'})
            ])
        ], className="mt-4")

    ], fluid=True, style={'background-color': '#f8f9fa'})
