from dash import html
import dash_bootstrap_components as dbc

def create_header():
    return dbc.Row([
        dbc.Col([
            html.H1("European Housing Price Index",
                   className="text-center mb-3 mt-4",
                   style={'color': '#2c3e50', 'font-weight': 'bold', 'font-size': '2.5rem'}),
            html.P([
                "Track and compare housing price trends across 30+ European countries. ",
                html.Br(),
                "All prices are relative to your selected start year (100 = baseline)"
            ],
                  className="text-center mb-1",
                  style={'font-size': '1.1rem', 'color': '#555'}),
            html.P("Use the year slider to set your baseline - all values will be compared to that year",
                  className="text-center text-muted mb-4",
                  style={'font-size': '0.95rem'}),
        ])
    ])
