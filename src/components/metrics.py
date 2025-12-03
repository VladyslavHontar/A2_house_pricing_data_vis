from dash import html
import dash_bootstrap_components as dbc

def create_metrics():
    return dbc.Row([
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
                    html.P("Most Expensive Now", className="card-text text-muted mb-0",
                          style={'font-size': '0.9rem'})
                ], className="text-center")
            ], style={'box-shadow': '0 2px 4px rgba(0,0,0,0.1)', 'border': 'none'})
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H3(id="metric-lowest", className="card-title text-danger mb-1",
                           style={'font-weight': 'bold', 'font-size': '1.3rem'}),
                    html.P("Most Affordable Now", className="card-text text-muted mb-0",
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
    ], className="mb-4")
