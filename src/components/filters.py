from dash import html, dcc
import dash_bootstrap_components as dbc

def create_filters(countries, years):
    return [
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
        ])
    ]
