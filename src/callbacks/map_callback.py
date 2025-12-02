from dash import Input, Output, callback
from src.visualizations import map_viz
from src.data_processing import data_loader

def register_map_callback(df):
    @callback(
        Output('price-map', 'figure'),
        [Input('year-slider', 'value'),
         Input('country-dropdown', 'value')]
    )
    def update_map(year_range, selected_countries):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if selected_countries and len(selected_countries) > 0:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        latest_data = filtered_df.sort_values('date').groupby('country_name').last().reset_index()

        return map_viz.create_map(latest_data, year_range[0])
