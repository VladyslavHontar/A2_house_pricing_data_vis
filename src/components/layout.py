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
                                f"{min_year}-{max_year} (Quarterly Updates) | 30+ European Countries",
                            ], className="text-center mb-0",
                              style={'font-size': '0.9rem', 'color': '#666'})
                        ])
                    ], className="py-3")
                ], style={'background-color': '#f8f9fa', 'border': 'none'})
            ])
        ], className="mt-4")

    ], fluid=True, style={'background-color': '#f8f9fa'})
