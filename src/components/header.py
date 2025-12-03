from dash import html
import dash_bootstrap_components as dbc

def create_header():
    return dbc.Row([
        dbc.Col([
            html.H1("European Housing Price Index",
                   className="text-center mb-3 mt-4",
                   style={'color': '#2c3e50', 'font-weight': 'bold', 'font-size': '2.5rem'}),
            html.P([
                "Track and compare housing price trends across 30 European countries"
            ],
                  className="text-center mb-3",
                  style={'font-size': '1.1rem', 'color': '#555'}),

            dbc.Card([
                dbc.CardBody([
                    html.H5("How to Read This Dashboard", className="card-title mb-3",
                           style={'color': '#2c3e50', 'font-weight': '600'}),
                    html.Div([
                        html.P([
                            html.Strong("What is a Price Index? "),
                            "Think of it like a scorecard that shows how housing prices changed over time. ",
                            "The baseline year is always set to 100."
                        ], className="mb-2"),
                        html.Ul([
                            html.Li([
                                html.Strong("100"), " = Baseline year (starting point)"
                            ]),
                            html.Li([
                                html.Strong("150"), " = Prices are 50% higher than the baseline"
                            ]),
                            html.Li([
                                html.Strong("75"), " = Prices are 25% lower than the baseline"
                            ]),
                            html.Li([
                                html.Strong("200"), " = Prices doubled compared to the baseline"
                            ]),
                        ], style={'font-size': '0.95rem'}),
                        html.P([
                            html.Strong("Example: "),
                            "If you select 2015-2020 on the year slider, all countries start at 100 in 2015. ",
                            "A country showing 130 in 2020 means housing became 30% more expensive during those 5 years."
                        ], className="mb-2", style={'background-color': '#e8f4f8', 'padding': '10px', 'border-radius': '5px'}),
                        html.P([
                            html.Strong("Note: "),
                            "These are average prices for entire countries. Prices in capital cities are typically much higher than rural areas."
                        ], className="mb-0 text-muted", style={'font-size': '0.9rem'}),
                    ])
                ])
            ], className="mb-4", style={'background-color': '#f8f9fa', 'border': '1px solid #dee2e6'}),
        ])
    ])
