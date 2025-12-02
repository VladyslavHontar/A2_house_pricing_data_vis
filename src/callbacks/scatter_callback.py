from dash import Input, Output, callback
from src.visualizations import scatter_viz

def register_scatter_callback(df):
    @callback(
        Output('growth-scatter', 'figure'),
        [Input('year-slider', 'value'),
         Input('country-dropdown', 'value')]
    )
    def update_scatter(year_range, selected_countries):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if selected_countries and len(selected_countries) > 0:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        return scatter_viz.create_scatter(filtered_df, year_range)
